"""Run the Chinese passages through exactly two local translation models."""

import json
from pathlib import Path

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


HERE = Path(__file__).resolve().parent
MODELS = (
    "facebook/m2m100_418M",
    "Helsinki-NLP/opus-mt-ja-en",
)
INPUT = HERE / "zhouyi_zh.json"
OUTPUT = HERE / "zhouyi_ja_en.json"


def translate_all(strings, model_name, device):
    print(f"Loading {model_name}", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device).eval()
    options = {"max_length": 128}
    if model_name == MODELS[0]:
        tokenizer.src_lang = "zh"
        options["forced_bos_token_id"] = tokenizer.get_lang_id("ja")
        # Catch a bad model or incompatible runtime before processing the book.
        probe = tokenizer(["你好。"], return_tensors="pt").to(device)
        with torch.inference_mode():
            answer = model.generate(**probe, **options)
        if "こんにちは" not in tokenizer.decode(answer[0], skip_special_tokens=True):
            raise RuntimeError("Chinese→Japanese model failed a simple smoke check")
    translated = {}
    for start in range(0, len(strings), 8):
        batch = strings[start : start + 8]
        inputs = tokenizer(batch, return_tensors="pt", padding=True).to(device)
        with torch.inference_mode():
            tokens = model.generate(**inputs, **options)
        translated.update(zip(batch, tokenizer.batch_decode(tokens, skip_special_tokens=True)))
        print(f"{model_name}: {min(start + 8, len(strings))}/{len(strings)}", flush=True)
    if model_name == MODELS[0]:
        # Short classical fragments occasionally decode to nothing. Give the
        # same Chinese→Japanese model a little context and try once more.
        for chinese, japanese in list(translated.items()):
            if japanese.strip():
                continue
            prompt = "这个字是" + chinese + "。"
            inputs = tokenizer([prompt], return_tensors="pt").to(device)
            with torch.inference_mode():
                tokens = model.generate(**inputs, **options)
            translated[chinese] = tokenizer.decode(tokens[0], skip_special_tokens=True)
            if not translated[chinese].strip():
                raise RuntimeError(f"Chinese→Japanese returned an empty string for {chinese!r}")
    del model
    return translated


def main():
    source = json.loads(INPUT.read_text())
    strings = list(dict.fromkeys(
        text
        for hexagram in source
        for text in (
            hexagram["name"],
            hexagram["judgment"],
            hexagram["image"],
            *(part for line in hexagram["lines"] for part in (line["label"], line["text"])),
            *((hexagram["special"][part] for part in ("label", "text")) if "special" in hexagram else ()),
        )
    ))
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Translating {len(strings)} distinct strings on {device}", flush=True)
    japanese = translate_all(strings, MODELS[0], device)
    # Translate each Japanese result once, including duplicates produced by step one.
    japanese_strings = list(dict.fromkeys(japanese.values()))
    english = translate_all(japanese_strings, MODELS[1], device)

    def passage(chinese):
        ja = japanese[chinese]
        return {"zh": chinese, "ja": ja, "en": english[ja]}

    result = {
        "models": {"zh_ja": MODELS[0], "ja_en": MODELS[1]},
        "hexagrams": [
            {
                "number": h["number"],
                "name": passage(h["name"]),
                "judgment": passage(h["judgment"]),
                "image": passage(h["image"]),
                "lines": [
                    {"label": passage(line["label"]), "text": passage(line["text"])}
                    for line in h["lines"]
                ],
                **({"special": {part: passage(h["special"][part]) for part in ("label", "text")}}
                   if "special" in h else {}),
            }
            for h in source
        ],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
