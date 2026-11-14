# Chinese I Ching text

`zhouyi_zh.json` contains the traditional Chinese passages shown on the
[Ludobench I Ching book](https://ludobench.com/fortunes/iching/book), in King
Wen order. That page identifies [Chinese Wikisource's 周易](https://zh.wikisource.org/wiki/周易)
as its public-domain Chinese source.

Each entry has the hexagram number and name, its judgment, its image, and six
line texts. The line texts are ordered from the bottom line to the top line.
Hexagrams 1 and 2 also have their special `用九` and `用六` passages. The `image`
passages are traditionally part of the later commentaries rather than the
oldest Zhouyi text, but are included because they appear on the linked page.

This is source text for future translation experiments. The Pico program does
not use it yet.

`translate_zhouyi.py` runs two local models, directly from Chinese to Japanese
and then from Japanese to English. To regenerate `zhouyi_ja_en.json` on a Mac:

```sh
python3 -m venv .venv-translate
.venv-translate/bin/python -m pip install torch 'transformers==4.57.1' sentencepiece
HF_HOME=.translation-cache .venv-translate/bin/python data/translate_zhouyi.py
```

The first run downloads the model weights; later runs can use the local cache.
The generated file keeps the Chinese, Japanese, and English for every name,
judgment, image, line label, line text, and special passage. These translations
are unedited machine output except for a second decoding attempt when the
Chinese→Japanese model repeats the same one or two tokens six times in a row.
That retry uses the same model with a three-token repeat limit. Model details
and licenses are at
[Chinese→Japanese](https://huggingface.co/facebook/m2m100_418M)
and [Japanese→English](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en).

`zhouyi_ja_en_broken.json` preserves the first, particularly absurd run. Its
Chinese→Japanese model was independently reported as broken and fails its own
published examples; see the [model discussion](https://huggingface.co/Helsinki-NLP/opus-mt-tc-big-zh-ja/discussions/4).

See `translation-review.md` for passages with repeated English output to
investigate later.
