# -*- coding: utf-8 -*-
"""본문에 등장하는 '단어장 130개 단어'를 전부 빈칸 후보로 자동 추출"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vocab import WORDS, SYN, ANT
from passage import S
from sim import gset

# 단어장 표제어 → 본문에서 찾을 표현들
EXTRA = {   # 표제어가 본문에서 다른 형태로 나오는 경우 직접 지정
  "be likely to": ["will likely"], "be charged with": ["charged with"],
  "be based on": ["was based on"], "be filled with": ["were filled with", "was filled with"],
  "know like the back of one's hand": ["like the back of his hand"],
  "pave the way for": ["paved the way for"], "flock to": ["flocked to"],
  "fall apart": ["fell apart"], "stack on": ["stacked on"],
  "speed up": ["speed up"], "more and more": ["more and more"],
  "rule of thumb": ["rule of thumb"], "by leaps and bounds": ["by leaps and bounds"],
  "such as": ["such as"], "due to": ["due to"], "thanks to": ["thanks to"],
  "at least": ["at least"], "on average": ["on average"], "for a fee": ["for a fee"],
  "driving force": ["driving forces"], "entrance exam": ["entrance exam"],
  "public service": ["public service"], "cloth bag": ["cloth bags"],
  "e-commerce": ["e-commerce"], "rule of thumb": ["rule of thumb"],
  "foot-powered": ["foot-powered"],
  "app": ["apps", "applications"], "million": ["millions"], "order": ["order", "ordered", "orders"],
  "need": ["need"], "review": ["review"], "score": ["scores"], "range": ["range"],
  "return": ["returned"], "receive": ["receives", "received"], "contact": ["contacted"],
  "divide": ["divided"], "drive": ["driven"], "develop": ["developed", "has developed"],
  "progress": ["progressed"], "trust": ["trust", "trusted"], "function": ["function"],
  "address": ["address"], "period": ["period"], "price": ["prices", "price"],
  "boost": ["boosted"], "indicate": ["indicating"], "determine": ["determined"],
  "extend": ["extended"], "enable": ["enabled"], "introduce": ["introduced"],
  "maintain": ["maintain"], "prioritize": ["prioritizes"], "concentrate": ["concentrated"],
  "deliver": ["delivered", "delivering", "deliver"], "rank": ["rank"],
  "transportation": ["transportation"], "vehicle": ["vehicles"], "equipment": ["equipment"],
  "caterer": ["caterers"], "bundle": ["bundles"], "tray": ["trays"], "scholar": ["scholar"],
  "diary": ["diary"], "entry": ["entry"], "document": ["document"], "residence": ["residence"],
  "schedule": ["schedule"], "distance": ["distance"], "professionals": ["professionals"],
  "logistics": ["Logistics", "logistics"], "possibility": ["possibility"],
  "automation": ["automation"], "urbanization": ["urbanization"], "liberation": ["liberation"],
  "upheaval": ["upheavals"], "labor": ["labor"], "hunger": ["hunger"], "culture": ["culture"],
  "industry": ["industry"], "century": ["centuries"], "technology": ["technology"],
  "advancement": ["advancements"], "growth": ["growth"], "development": ["development"],
  "delivery": ["delivery", "deliveries"], "fee": ["fee"], "popularity": ["popularity"],
  "standard": ["standards"], "various": ["various"], "speedy": ["speedy"],
  "purchased": ["purchased"], "literally": ["literally"], "nearly": ["nearly"],
  "within": ["within"], "limited": ["limited"], "mistake": ["mistakes"],
  "unfailingly": ["unfailingly"], "honest": ["honest"], "accurate": ["accurate"],
  "unique": ["unique"], "mutual": ["mutual"], "modern": ["modern"], "local": ["local"],
  "colonial": ["colonial"], "historical": ["historical"], "rare": ["rare"],
  "express": ["express"], "daily": ["daily"], "remarkable": ["remarkable"],
  "reasonable": ["reasonable"], "phenomenal": ["phenomenal"], "specific": ["specific"],
  "further": ["further"], "autonomous": ["autonomous"], "advanced": ["advanced"],
  "fair": ["fair"], "persistent": ["persistent"], "effort": ["efforts"],
  "reliability": ["reliability"], "adoption": ["adoption"], "forward": ["forward"],
  "late": ["late"], "rapidly": ["rapidly"], "rapid": ["rapid"], "affordable": ["affordable"],
  "urban": ["urban"], "scale": ["scale"], "whatever": ["whatever"], "whenever": ["whenever"],
  "wherever": ["wherever"],
}
SKIP = set()   # 단어장 130개 전부를 빈칸 후보로 삼는다

def forms(w):
    """단어 하나의 굴절형 후보"""
    if w in EXTRA: return EXTRA[w]
    if " " in w or "-" in w: return [w]
    out = {w}
    if w.endswith("e"):   out |= {w+"d", w+"s", w[:-1]+"ing", w+"r", w[:-1]+"al"}
    elif w.endswith("y"): out |= {w[:-1]+"ies", w[:-1]+"ied", w+"ing", w+"s"}
    else:                 out |= {w+"s", w+"es", w+"ed", w+"ing", w+"ly", w+"d"}
    return sorted(out, key=len, reverse=True)

# 한 단어가 속한 의미 묶음 (유의어표 + 반의어표)
GRP = {}
for TBL in (SYN, ANT):
    for w, _, a, _, g in TBL:
        GRP.setdefault(w.lower(), set()).update(gset(g))
        GRP.setdefault(a.lower(), set()).update(gset(g))

# 유의어/반의어표만으로는 안 걸러지는데 본문 해석 때문에 헷갈리는 짝을 직접 묶는다.
# autonomous(s43)의 교과서 해석이 "자동화 로봇"이라 automation을 보기에 넣으면
# 해석을 근거로 automation을 고르게 된다.
GRP_MERGE = [
    {"autonomous", "automation"},
    {"delivery", "deliver"},
    {"development", "develop"},
    {"urban", "urbanization"},
]
for grp in GRP_MERGE:
    tag = "X_PAIR_" + "_".join(sorted(grp)).upper()
    for w in grp:
        GRP.setdefault(w, set()).add(tag)

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
            g = sorted(GRP.get(head.lower(), set()) or {"X_" + head.replace(" ", "_").upper()})
            out.append({"sid": sid, "ans": tgt, "head": head, "p": pos, "g": g,
                        "pre": en[:st], "post": en[ed:], "ko": ko})
    return out

if __name__ == '__main__':
    B = build()
    from collections import Counter
    print("빈칸 후보:", len(B), "| 문장 수:", len({b['sid'] for b in B}), "| 서로 다른 정답:", len({b['ans'].lower() for b in B}))
    c = Counter(b['sid'] for b in B)
    print("문장당 빈칸 수:", dict(Counter(c.values())))
    print("\n샘플 (s47):")
    for b in B:
        if b['sid'] == 's47': print(f"   {b['ans']:16s} [{','.join(b['g'])}]")
    print("\n샘플 (s5):")
    for b in B:
        if b['sid'] == 's5': print(f"   {b['ans']:16s} [{','.join(b['g'])}]")
