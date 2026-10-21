# -*- coding: utf-8 -*-
"""본문에 등장하는 단어장 단어를 전부 빈칸 후보로 자동 추출"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vocab import WORDS, SYN, ANT
from passage import S
from sim import gset

# 단어장 표제어 → 본문에서 찾을 표현들
EXTRA = {   # 표제어가 본문에서 다른 형태로 나오는 경우 직접 지정
  "be likely to": ["likely to"], "fail to": ["failed to"],
  "pay attention to": ["paying attention to", "pay attention to"],
  "chances are (that)": ["chances are"], "eureka moment": ["eureka moments"],
  "occur": ["occurring"], "challenge": ["challenge"],
  "experience": ["experience", "experienced"],
}
# 본문에서 두 덩어리로 떨어져 나오는 숙어는 빈칸으로 뚫지 않는다
SKIP = {"with ~ in mind", "hold up A against B", "replace A with B"}

def forms(w):
    """단어 하나의 굴절형 후보"""
    if w in EXTRA: return EXTRA[w]
    if " " in w or "-" in w: return [w]
    out = {w}
    if w.endswith("e"):   out |= {w+"d", w+"s", w[:-1]+"ing", w+"r", w[:-1]+"al"}
    elif w.endswith("y"): out |= {w[:-1]+"ies", w[:-1]+"ied", w+"ing", w+"s"}
    else:                 out |= {w+"s", w+"es", w+"ed", w+"ing", w+"ly", w+"d"}
    return sorted(out, key=len, reverse=True)

# 한 단어가 속한 의미 묶음 (vocab.py에서 동의어·반의어 짝 + 직접 묶은 것)
from vocab import _G

def build():
    out, seen = [], set()
    for sid, en, ko in S:
        low = en.lower()
        hits = []
        for head, _, pos in WORDS:
            if head in SKIP: continue
            for f in forms(head):
                for m in re.finditer(r'(?<![A-Za-z\-\'])' + re.escape(f.lower()) + r'(?![A-Za-z\-\'])', low):
                    hits.append((m.start(), m.end(), head, pos))
                break_outer = False
        # 겹치는 매칭은 긴 것 우선
        hits.sort(key=lambda h: (h[0], -(h[1]-h[0])))
        taken, picked = [], []
        for st, ed, head, pos in hits:
            if any(not (ed <= a or st >= b) for a, b in taken): continue
            taken.append((st, ed)); picked.append((st, ed, head, pos))
        for st, ed, head, pos in picked:
            tgt = en[st:ed]
            if len(tgt) < 3: continue                    # 너무 짧은 건 제외
            key = (sid, tgt.lower(), st)
            if key in seen: continue
            seen.add(key)
            g = [_G(head)]
            out.append({"sid": sid, "ans": tgt, "head": head, "p": pos, "g": g,
                        "pre": en[:st], "post": en[ed:], "ko": ko})
    return out

if __name__ == '__main__':
    B = build()
    from collections import Counter
    print("빈칸 후보:", len(B), "| 문장 수:", len({b['sid'] for b in B}), "| 서로 다른 정답:", len({b['ans'].lower() for b in B}))
    c = Counter(b['sid'] for b in B)
    print("문장당 빈칸 수:", dict(Counter(c.values())))
    found = {b['head'] for b in B}
    print("본문에서 못 찾은 단어:", [w for w, _, _ in WORDS if w not in found and w not in SKIP])
    for b in B: print(f"   {b['sid']:4s} {b['ans']:22s} <- {b['head']}")
