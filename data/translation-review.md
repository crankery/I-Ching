# Repeated English output to investigate later

These 20 passages were flagged during a read-through of `zhouyi_ja_en.json`.
The quoted phrases are identifying excerpts from the review, not replacements
for the generated text. Keep the comic mistranslations; investigate only the
repetition when we revisit the translator.

Hexagram numbers are in King Wen order. Line numbers count from the bottom, as
they do in `zhouyi_zh.json` and `zhouyi_ja_en.json`. For example, 6 → line 3 is
`hexagrams[5].lines[2].text`.

| Location | Repeated English excerpt | Severity |
| --- | --- | --- |
| 4 → judgment | “I love you, love you, love you…” | — |
| 6 → line 3 | “You can eat it, you can eat it…” | — |
| 11 → line 6 | “It's a town… It's a city…” | — |
| 27 → line 3 | “Ten, ten, ten…” | — |
| 35 → name | “I'm sorry, I'm sorry…” | — |
| 41 → judgment | “Two, two, two…” | — |
| 42 → image | “Let's do good, let's do good…” | — |
| 46 → line 5 | “It's going up in Saudi Arabia, it's going up…” | — |
| 51 → line 1 | “It's funny, it's funny…” | — |
| 55 → line 3 | “On the right, on the right…” | — |
| 2 → judgment | “Jesus Christ Christ Christ…” | Severe |
| 29 → line 6 | “Three three three three…” | Severe |
| 64 → line 2 | “Lucky, Lucky, Lucky…” | Severe |
| 60 → image | “No, no, no, no…” | Severe |
| 28 → line 2 | “The wife of the wife of the wife…” | Severe |
| 54 → image | “Jesus Christ Christ Christ…” | Severe |
| 26 → line 3 | “Good luck, good luck…” | Severe |
| 29 → image | “No water, no water…” | Severe |
| 39 → judgment | “Jesus Christ Christ Christ…” | Severe |
| 8 → name | “No, no, no, no…” | Severe |

When revisiting, compare each Japanese intermediate with its English output to
find which translation pass introduced the repetition. The existing short-token
loop retry only runs during the Chinese→Japanese pass.
