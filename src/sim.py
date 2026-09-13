# -*- coding: utf-8 -*-
"""단어 뜻 문제용 오답 선지 후보 계산

원칙: '정답이 둘'이 되면 안 된다.
  아래는 전부 후보에서 제외한다.
   ① 뜻 조각이 하나라도 겹치는 단어
   ② 은서쌤 유의어표에서 같은 묶음인 단어      (발전/발달, 빠른/신속한 …)
   ③ 은서쌤 반의어표에서 같은 묶음인 단어      (같은 의미축 위의 단어)
   ④ 같은 어근에서 파생된 단어                 (advance-ment / advance-d, rapid / rapid-ly)
  남은 후보 중에서 '같은 품사 + 같은 의미 영역 + 비슷한 길이'를 우선한다.
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vocab import WORDS, SYN, ANT

def toks(m):
    out = set()
    for t in re.split(r'[,;/]', m):
        t = re.sub(r'^\[[^\]]*\]\s*', '', t.strip().strip('.'))
        if t: out.add(t)
    return out

def lcp(a, b):
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]: n += 1
    return n

def lev(a, b):
    if a == b: return 0
    prev = list(range(len(b)+1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j]+1, cur[j-1]+1, prev[j-1] + (ca != cb)))
        prev = cur
    return prev[-1]

def bigrams(s):
    s = re.sub(r'[^가-힣]', '', s)
    return {s[i:i+2] for i in range(len(s)-1)}

# ── 유의어/반의어표에서 '같은 묶음' 관계 추출 ──────────────────
def gset(grp):
    return set(grp.split('|'))

def group_map(TABLE):
    g = {}
    for w, wm, a, am, grp in TABLE:
        g.setdefault(w.lower(), set()).update(gset(grp))
        g.setdefault(a.lower(), set()).update(gset(grp))
    return g
SG, AG = group_map(SYN), group_map(ANT)

def groups_of(w):
    # 유의어표 묶음 + 반의어표 묶음을 합쳐서 본다.
    # (rapid는 유의어표에만, express는 반의어표에만 있어서 따로 보면 SPEED가 안 겹쳤다)
    return SG.get(w, set()) | AG.get(w, set())

def same_group(a, b):
    return bool(groups_of(a) & groups_of(b))

N = len(WORDS)
T = [toks(m) for _, m, _ in WORDS]
B = [bigrams(m) for _, m, _ in WORDS]
SIM, REJ = [], {}
for i, (wi, mi, pi) in enumerate(WORDS):
    a = wi.lower()
    cands, rej = [], []
    for j, (wj, mj, pj) in enumerate(WORDS):
        if i == j: continue
        b = wj.lower()
        if T[i] & T[j]:        rej.append((wj, '뜻 겹침')); continue
        if same_group(a, b):   rej.append((wj, '유/반의어표 같은 묶음')); continue
        if lcp(a, b) >= 5:     rej.append((wj, '같은 어근 파생어')); continue
        sc = 0.0
        if pi == pj: sc += 6
        if B[i] and B[j]: sc += len(B[i] & B[j]) / len(B[i] | B[j]) * 8
        sc += (1 - lev(a, b) / max(len(a), len(b))) * 3
        if abs(len(a) - len(b)) <= 2: sc += 1
        cands.append((sc, j))
    cands.sort(key=lambda x: (-x[0], x[1]))
    SIM.append([j for _, j in cands[:20]])
    REJ[wi] = rej

if __name__ == '__main__':
    for w in ['advancement','rapid','development','express','entry','scholar','maintain','urban']:
        i = next(k for k, x in enumerate(WORDS) if x[0] == w)
        print(f'\n■ {w} — 정답: {WORDS[i][1]}')
        print('   선지 후보(상위 6):')
        for j in SIM[i][:6]:
            print(f'     · {WORDS[j][1]}   ({WORDS[j][0]})')
        if REJ[w]:
            print('   제외됨:', ', '.join(f'{x}({y})' for x, y in REJ[w][:5]))
