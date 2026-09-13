# -*- coding: utf-8 -*-
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vocab, passage as P
from sim import SIM, toks, SG, AG, gset

sd = {s[0]: (s[1], s[2]) for s in P.S}

from blanks import build as build_blanks
blanks = build_blanks()

# 빈칸 단어의 품사·뜻 (채점 후 해설용)
POS_KO = {"n": "명사", "v": "동사", "adj": "형용사", "adv": "부사", "phr": "숙어"}
MEAN = {w: m for w, m, _ in vocab.WORDS}
for b in blanks:
    b["pk"] = POS_KO.get(b["p"], "")
    b["hm"] = MEAN.get(b["head"], "")

# 단어별로 '목록 밖 오답'으로 써도 되는 EXT 인덱스 (의미 묶음 충돌 / 뜻 겹침 제외)
XS = []
for w, m, _ in vocab.WORDS:
    lw, tm = w.lower(), toks(m)
    mine = SG.get(lw, set()) | AG.get(lw, set())
    XS.append([j for j, (ew, em, _, eg) in enumerate(vocab.EXT)
               if not (gset(eg) & mine) and not (tm & toks(em))])

data = {
    "lesson": {
        "id": "lesson2",
        "title": "Lesson 2 단어 시험",
        "sub": "2학기 · YBM(김은형) 공통영어2 · K-Delivery",
        "school": "송우고등학교",
    },
    "words": [{"w": w, "m": m, "p": p, "s": SIM[i], "x": XS[i]}
              for i, (w, m, p) in enumerate(vocab.WORDS)],
    "ext":   [{"w": w, "m": m, "p": p, "g": [g]} for w, m, p, g in vocab.EXT],
    "syn":   [{"w": w, "wm": wm, "a": a, "am": am, "g": sorted(gset(g))} for w, wm, a, am, g in vocab.SYN],
    "ant":   [{"w": w, "wm": wm, "a": a, "am": am, "g": sorted(gset(g))} for w, wm, a, am, g in vocab.ANT],
    "passage": {
        "titleEn": P.TITLE_EN, "titleKo": P.TITLE_KO,
        "paras": [[{"id": i, "en": sd[i][0], "ko": sd[i][1]} for i in para] for para in P.PARAS],
    },
    "blanks": blanks,
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
print("data.json 생성:", os.path.getsize(out), "bytes")
print("  단어뜻", len(data["words"]), "/ 유의어", len(data["syn"]), "/ 반의어", len(data["ant"]), "/ 본문빈칸", len(data["blanks"]))
