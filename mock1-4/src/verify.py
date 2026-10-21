# -*- coding: utf-8 -*-
"""검수: 원본 PDF 5종 + 본문 PDF ↔ data.json 을 한 글자씩 대조한다.

원본에서 일부러 바꾼 것만 예외로 둔다(아래 NORMALIZE / ANT_FIX / ANT_DROP).
그 밖의 차이가 하나라도 있으면 실패.
"""
import fitz, os, re, json, unicodedata, sys

D = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/")
here = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(here, "data.json"), encoding="utf-8"))

def pdf(prefix):
    for f in os.listdir(D):
        if unicodedata.normalize("NFC", f).startswith(prefix):
            return fitz.open(D + f)
    sys.exit("원본 없음: " + prefix)

def rows(prefix):
    out = []
    for p in pdf(prefix):
        bl = [b for b in p.get_text("blocks") if 70 < b[1] < 790]
        bl.sort(key=lambda b: (b[0] > 300, b[1]))       # 왼쪽 열 → 오른쪽 열
        for b in bl:
            w, m = (b[4].strip().split("\n", 1) + [""])[:2]
            out.append((w.strip(), " ".join(m.split())))
    return out

def norm_mean(m):
    m = re.sub(r"^\[[명형동부]\]\s*", "", m)              # [명]/[형] 품사 표시 제거
    return m.replace("보상하 다", "보상하다")               # PDF 줄바꿈 깨짐

ANT_DROP = {"pop up", "outcome"}                          # 반의어(2)에 짝 없음
ANT_FIX = {"erode": "corrode"}                            # 본문·단어표 표기로 통일

errs = []
def chk(tag, a, b):
    if a != b: errs.append(f"[{tag}] 원본 {a!r} ≠ 앱 {b!r}")

# 1) 단어 뜻
src = [(w, norm_mean(m)) for w, m in rows("(수행) 모의고사 1-4(22번~32번)")]
app = [(x["w"], x["m"]) for x in data["words"]]
chk("단어뜻 개수", len(src), len(app))
for i, (s, a) in enumerate(zip(src, app), 1): chk(f"단어뜻 {i}", s, a)

# 2) 동의어
s1, s2 = rows("(수행) 모의고사 1-4 동의어(1)"), rows("(수행) 모의고사 1-4 동의어(2)")
chk("동의어 (1)(2) 개수", len(s1), len(s2))
src = [(a[0], a[1], b[0], b[1]) for a, b in zip(s1, s2)]
app = [(x["w"], x["wm"], x["a"], x["am"]) for x in data["syn"]]
chk("동의어 개수", len(src), len(app))
for i, (s, a) in enumerate(zip(src, app), 1): chk(f"동의어 {i}", s, a)

# 3) 반의어 — (1)에서 짝 없는 2개를 빼면 (2)와 칸이 맞는다
a1 = [r for r in rows("(수행) 모의고사 1-4 반의어(1)") if r[0] not in ANT_DROP]
a2 = rows("(수행) 모의고사 1-4 반의어(2)")
chk("반의어 (1)(2) 개수", len(a1), len(a2))
src = [(ANT_FIX.get(a[0], a[0]), a[1], b[0], b[1]) for a, b in zip(a1, a2)]
app = [(x["w"], x["wm"], x["a"], x["am"]) for x in data["ant"]]
chk("반의어 개수", len(src), len(app))
for i, (s, a) in enumerate(zip(src, app), 1): chk(f"반의어 {i}", s, a)

# 4) 본문 — 영문 전체를 공백만 정리해서 비교
doc = pdf("송우고1-2 2606")
paras = data["passage"]["paras"]
chk("본문 지문 수", len(doc), len(paras))
for k, (p, para) in enumerate(zip(doc, paras)):
    en = " ".join(b[4] for b in sorted(p.get_text("blocks"), key=lambda b: b[1]) if b[0] < 300 and 120 < b[1] < 790)
    chk(f"본문 {data['passage']['labels'][k]}번 영문", " ".join(en.split()), " ".join(s["en"] for s in para))
    ko = "".join(b[4] for b in sorted(p.get_text("blocks"), key=lambda b: b[1]) if b[0] > 300 and 120 < b[1] < 790)
    chk(f"본문 {data['passage']['labels'][k]}번 해석(공백 제외)", re.sub(r"\s", "", ko), re.sub(r"\s", "", "".join(s["ko"] for s in para)))

# 5) 본문 빈칸 정답은 본문 원문 글자 그대로여야 한다
sent = {s["id"]: s["en"] for para in paras for s in para}
for b in data["blanks"]:
    chk(f"빈칸 {b['sid']} {b['ans']}", sent[b["sid"]], b["pre"] + b["ans"] + b["post"])
    if b["head"] not in {x["w"] for x in data["words"]}: errs.append(f"[빈칸] 단어표에 없는 표제어 {b['head']}")

# 6) 오답 보기 안전: 범위 밖 오답풀(EXT)에 단어표·동의어·반의어 단어가 섞이면 안 된다
inscope = {x["w"].lower() for x in data["words"]} | {x[k].lower() for t in ("syn", "ant") for x in data[t] for k in ("w", "a")}
for e in data["ext"]:
    if e["w"].lower() in inscope: errs.append(f"[오답풀] 범위 단어가 섞임: {e['w']}")

print(f"단어뜻 {len(data['words'])} / 동의어 {len(data['syn'])} / 반의어 {len(data['ant'])} / 본문 {len(paras)}지문 · 빈칸 {len(data['blanks'])}")
if errs:
    print(f"불일치 {len(errs)}건"); [print("  " + e) for e in errs]; sys.exit(1)
print("검수 통과: 원본과 전부 일치 (예외: [명]/[형] 표시 제거, '보상하 다' 줄바꿈, 반의어 pop up·outcome 제외, erode→corrode)")
