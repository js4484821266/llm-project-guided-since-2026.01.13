from load_data import DATA
from pathlib import Path
import re, json

v = []
for key in DATA:
    law = article_n = article_title = article_text = None
    law = Path(key).stem
    for item in DATA[key]:
        i = re.split(r"조 |\) ", item, maxsplit=1)
        article_text = i[1]
        i = i[0]
        article_n = int(re.findall(r"\d+", i)[0])
        i = i.split("(", maxsplit=1)
        try:
            article_title = i[1]
        except:
            article_title = ""
        v.append(
            {
                "law": law,
                "article_n": article_n,
                "article_title": article_title,
                "article_text": article_text,
            }
        )
with open(f"data.json", "w", encoding="utf-8") as f:
    json.dump(v, f, ensure_ascii=False, indent=4)
