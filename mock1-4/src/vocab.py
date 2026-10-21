# -*- coding: utf-8 -*-
"""송우고 1학년 수행평가 — 모의고사 1-4 (22번~32번) 어휘 데이터

원본: iCloud Drive
  (수행) 모의고사 1-4(22번~32번).pdf   → WORDS (84)
  (수행) 모의고사 1-4 동의어(1)/(2).pdf → SYN  (49쌍, 같은 칸끼리 짝)
  (수행) 모의고사 1-4 반의어(1)/(2).pdf → ANT  (46쌍)
    반의어(1)은 48개, (2)는 46개다. (1)의 pop up · outcome 은 (2)에 짝이 없어서 뺐다.
    반의어(1)의 erode는 본문(23번)·단어표 표기인 corrode로 바꿨다.
뜻은 원본 표기 그대로 두고, [명]/[형] 표시와 줄바꿈 깨짐(보상하 다)만 정리했다.
"""

# ── 1) 단어 뜻 ────────────────────────────────────────────────
# (word, meaning, pos)  pos: n/v/adj/adv/phr
WORDS = [
    ("spot", "장소, 지점", "n"),
    ("variety", "다양성", "n"),
    ("rich", "풍부한", "adj"),
    ("reinforce", "강화하다", "v"),
    ("rather than", "~라기보다는", "phr"),
    ("nook", "아늑한 구석", "n"),
    ("reflect", "반영하다", "v"),
    ("numerous", "수많은", "adj"),
    ("experiment", "실험", "n"),
    ("at least", "적어도", "phr"),
    ("be likely to", "~할 가능성이 있다", "phr"),
    ("trial", "시험, 시도", "n"),
    ("counterpart", "상대방, 대응 관계에 있는 사람", "n"),
    ("amount", "양", "n"),
    ("divide", "나누다", "v"),
    ("recall", "기억해 내다, 상기하다", "v"),
    ("association", "연상, 연관", "n"),
    ("connection", "연결, 관계", "n"),
    ("form", "형성되다, 만들다", "v"),
    ("background", "배경", "n"),
    ("consciously", "의식적으로", "adv"),
    ("occur", "발생하다, 일어나다", "v"),
    ("scroll", "(화면을) 스크롤하다, 넘겨보다", "v"),
    ("social media", "소셜 미디어", "n"),
    ("immediately", "즉시, 곧바로", "adv"),
    ("increase", "증가하다, 늘어나다", "v"),
    ("incredibly", "엄청나게, 믿을 수 없을 정도로", "adv"),
    ("pleasure", "쾌락, 즐거움", "n"),
    ("challenge", "문제, 난제", "n"),
    ("universe", "우주, 세상", "n"),
    ("physics", "물리학", "n"),
    ("seek", "찾다, 추구하다", "v"),
    ("homeostasis", "항상성 (체내 균형 상태)", "n"),
    ("with ~ in mind", "~을 염두에 두고", "phr"),
    ("achieve", "달성하다, 이루다", "v"),
    ("drop", "떨어지다, 급락하다", "v"),
    ("equal", "동일한, 같은", "adj"),
    ("baseline", "기준선, 기저 수준", "n"),
    ("rebalance", "다시 균형을 잡다", "v"),
    ("experience", "경험하다, 느끼다", "v"),
    ("in order to", "~하기 위해서", "phr"),
    ("shame", "수치심, 부끄러움", "n"),
    ("guilt", "죄책감", "n"),
    ("guilty", "죄책감을 느끼는", "adj"),
    ("hold up A against B", "A를 B에 견주어보다", "phr"),
    ("behavior", "행동, 태도", "n"),
    ("fail to", "~하지 못하다", "phr"),
    ("uncomfortable", "불편한", "adj"),
    ("apologize", "사과하다", "v"),
    ("make amends", "(잘못에 대해) 사죄하다, 보상하다", "phr"),
    ("motivator", "동기 부여 요소, 자극제", "n"),
    ("powerful", "강력한", "adj"),
    ("effect", "효과, 영향", "n"),
    ("positive", "긍정적인", "adj"),
    ("destructive", "파괴적인", "adj"),
    ("replace A with B", "A를 B로 대체하다", "phr"),
    ("research", "연구, 조사", "n"),
    ("corrode", "부식시키다, (마음을) 좀먹다", "v"),
    ("believe", "믿다, 생각하다", "v"),
    ("suppose", "가정하다, 생각하다", "v"),
    ("solution", "해결책", "n"),
    ("challenging", "힘든, 도전적인", "adj"),
    ("pay attention to", "~에 유의하다", "phr"),
    ("encounter", "마주치다, 접하다", "v"),
    ("be related to", "~와 관련이 있다", "phr"),
    ("chances are (that)", "~일 가능성이 크다", "phr"),
    ("pop up", "갑자기 떠오르다", "phr"),
    ("eureka moment", "유레카의 순간 (깨달음의 순간)", "n"),
    ("insight", "통찰력, 깊은 이해", "n"),
    ("take place", "일어나다, 발생하다", "phr"),
    ("unexpected", "예상치 못한", "adj"),
    ("enhance", "향상시키다, 높이다", "v"),
    ("spontaneous", "자발적인, 즉흥적인", "adj"),
    ("potentially", "잠재적으로, 어쩌면", "adv"),
    ("valuable", "가치있는, 값비싼", "adj"),
    ("outcome", "결과, 성과", "n"),
    ("narrow down", "(범위를) 좁히다", "phr"),
    ("interest", "관심, 흥미", "n"),
    ("specific", "특정한", "adj"),
    ("on the contrary", "그와는 반대로", "phr"),
    ("breadth", "폭, 넓이", "n"),
    ("scope", "범위, 영역", "n"),
    ("likewise", "마찬가지로", "adv"),
    ("harmful", "해로운", "adj"),
]

# ── 2) 동의어 (단어, 단어뜻, 동의어, 동의어뜻) ─────────────────────
SYN_RAW = [
    ("spot", "장소, 지점", "place", "장소"),
    ("variety", "다양성", "diversity", "다양성"),
    ("rich", "풍부한", "abundant", "풍부한"),
    ("reinforce", "강화하다", "strengthen", "강화하다"),
    ("numerous", "수많은", "countless", "셀 수 없이 많은"),
    ("experiment", "실험", "test", "실험, 시험"),
    ("at least", "적어도", "at minimum", "최소한"),
    ("trial", "시험, 시도", "attempt", "시도"),
    ("amount", "양", "quantity", "양, 수량"),
    ("divide", "나누다", "separate", "분리하다"),
    ("recall", "기억해 내다, 상기하다", "remember", "기억하다"),
    ("association", "연상, 연관", "connection", "연결, 연관"),
    ("connection", "연결, 관계", "link", "연결, 관계"),
    ("form", "형성되다, 만들다", "create", "만들다"),
    ("background", "배경", "setting", "배경, 환경"),
    ("consciously", "의식적으로", "deliberately", "의도적으로"),
    ("occur", "발생하다, 일어나다", "happen", "발생하다"),
    ("immediately", "즉시, 곧바로", "instantly", "즉시"),
    ("increase", "증가하다, 늘어나다", "rise", "증가하다"),
    ("pleasure", "쾌락, 즐거움", "enjoyment", "즐거움"),
    ("challenge", "문제, 난제", "difficulty", "어려움, 난제"),
    ("universe", "우주, 세상", "cosmos", "우주"),
    ("seek", "찾다, 추구하다", "pursue", "추구하다"),
    ("homeostasis", "항상성", "balance", "균형"),
    ("achieve", "달성하다, 이루다", "accomplish", "성취하다"),
    ("drop", "떨어지다, 급락하다", "decrease", "감소하다"),
    ("equal", "동일한, 같은", "equivalent", "동등한"),
    ("experience", "경험하다, 느끼다", "undergo", "경험하다, 겪다"),
    ("in order to", "~하기 위해서", "so as to", "~하기 위해서"),
    ("guilt", "죄책감", "remorse", "후회, 죄책감"),
    ("behavior", "행동, 태도", "conduct", "행동"),
    ("uncomfortable", "불편한", "uneasy", "불안한, 불편한"),
    ("motivator", "동기 부여 요소, 자극제", "incentive", "동기, 자극"),
    ("powerful", "강력한", "strong", "강력한"),
    ("effect", "효과, 영향", "impact", "영향"),
    ("positive", "긍정적인", "optimistic", "낙관적인"),
    ("replace A with B", "A를 B로 대체하다", "substitute B for A", "A를 B로 바꾸다"),
    ("in fact", "사실은, 실제로는", "actually", "실제로"),
    ("research", "연구, 조사", "investigation", "조사, 연구"),
    ("suppose", "가정하다, 생각하다", "assume", "가정하다"),
    ("solution", "해결책", "answer", "해결책, 답"),
    ("challenging", "힘든, 도전적인", "difficult", "어려운"),
    ("encounter", "마주치다, 접하다", "come across", "우연히 만나다, 접하다"),
    ("pop up", "갑자기 떠오르다", "appear", "나타나다"),
    ("unexpected", "예상치 못한", "unforeseen", "예측하지 못한"),
    ("enhance", "향상시키다, 높이다", "improve", "향상시키다"),
    ("potentially", "잠재적으로, 어쩌면", "possibly", "아마, 가능성 있게"),
    ("specific", "특정한", "particular", "특정한"),
    ("spontaneous", "자발적인, 즉흥적인", "impulsive", "충동적인, 즉흥적인"),
]

# ── 3) 반의어 (단어, 단어뜻, 반의어, 반의어뜻) ─────────────────────
ANT_RAW = [
    ("variety", "다양성", "uniformity", "획일성"),
    ("rich", "풍부한", "poor", "빈약한"),
    ("reinforce", "강화하다", "weaken", "약화시키다"),
    ("numerous", "수많은", "few", "소수의"),
    ("likely to", "~할 가능성이 있다", "unlikely to", "~할 가능성이 없다"),
    ("divide", "나누다", "unite", "합치다"),
    ("recall", "기억해 내다", "forget", "잊다"),
    ("association", "연상, 연관", "disconnection", "단절, 무관"),
    ("form", "형성하다", "destroy", "파괴하다"),
    ("consciously", "의식적으로", "unconsciously", "무의식적으로"),
    ("occur", "발생하다", "disappear", "사라지다"),
    ("immediately", "즉시", "eventually", "결국, 마침내"),
    ("increase", "증가하다", "decrease", "감소하다"),
    ("pleasure", "즐거움", "pain", "고통"),
    ("challenge", "난제, 도전", "ease", "용이함"),
    ("seek", "찾다, 추구하다", "avoid", "피하다"),
    ("homeostasis", "항상성", "imbalance", "불균형"),
    ("with ~ in mind", "~을 염두에 두고", "without considering ~", "~을 고려하지 않고"),
    ("achieve", "달성하다", "fail", "실패하다"),
    ("drop", "떨어지다, 감소하다", "rise", "상승하다"),
    ("equal", "동일한", "unequal", "동일하지 않은"),
    ("guilty", "죄책감을 느끼는", "innocent", "무죄의, 결백한"),
    ("fail to", "~하지 못하다", "succeed in", "~에 성공하다"),
    ("uncomfortable", "불편한", "comfortable", "편안한"),
    ("apologize", "사과하다", "blame", "비난하다"),
    ("motivator", "동기 부여 요소", "discouragement", "의욕 저하"),
    ("powerful", "강력한", "powerless", "무력한"),
    ("effect", "효과, 영향", "cause", "원인"),
    ("positive", "긍정적인", "negative", "부정적인"),
    ("destructive", "파괴적인", "constructive", "건설적인"),
    ("negative", "부정적인", "positive", "긍정적인"),
    ("corrode", "약화시키다, 좀먹다", "strengthen", "강화하다"),
    ("believe", "믿다", "doubt", "의심하다"),
    ("suppose", "가정하다", "know for certain", "확실히 알다"),
    ("solution", "해결책", "problem", "문제"),
    ("challenging", "힘든, 도전적인", "easy", "쉬운"),
    ("pay attention to", "~에 주의를 기울이다", "ignore", "무시하다"),
    ("be related to", "~와 관련이 있다", "be unrelated to", "~와 관련이 없다"),
    ("chances are (that)", "~일 가능성이 크다", "it is unlikely that", "~일 가능성이 낮다"),
    ("unexpected", "예상치 못한", "expected", "예상된"),
    ("enhance", "향상시키다", "diminish", "감소시키다"),
    ("spontaneous", "자발적인, 즉흥적인", "planned", "계획된"),
    ("potentially", "잠재적으로", "definitely", "확실히"),
    ("valuable", "가치 있는", "worthless", "가치 없는"),
    ("narrow down", "범위를 좁히다", "broaden", "범위를 넓히다"),
    ("interest", "관심, 흥미", "indifference", "무관심"),
]

# ── 의미 묶음(group) ──────────────────────────────────────────
# 같은 묶음끼리는 서로 오답 선지가 되지 않는다.
# 동의어·반의어 짝으로 이어지는 단어는 자동으로 한 묶음이 되고,
# 짝으로는 안 이어지지만 '이것도 답 같다'가 될 수 있는 것만 아래에서 직접 묶는다.
MERGE = [
    # 강화/약화·증가/감소 축: enhance의 반의어 문제에 weaken·decrease가 보기로 나오면 답이 둘
    {"reinforce", "corrode", "enhance", "improve", "diminish", "powerful", "powerless", "increase", "drop"},
    # 긍정/부정·건설/파괴 축: destructive의 반의어 보기에 positive가 나오면 답이 둘
    {"positive", "destructive", "harmful", "valuable", "worthless", "form", "destroy"},
    # 가능성 축
    {"be likely to", "likely to", "chances are (that)", "potentially", "possibly", "definitely"},
    # 예상/계획 축
    {"unexpected", "spontaneous", "pop up", "occur", "take place", "encounter", "experience"},
    # 어려움 축
    {"challenge", "challenging", "solution", "problem"},
    # 실패/성공 축
    {"achieve", "fail to"},
    # 실험·연구
    {"experiment", "trial", "research"},
    # 많음/풍부
    {"rich", "numerous", "amount", "at least"},
    # 연결/관련
    {"association", "be related to"},
    # 주의/무관심
    {"pay attention to", "interest", "with ~ in mind", "seek"},
    # 믿음/가정
    {"believe", "suppose"},
    # 죄책감/사과
    {"guilt", "guilty", "shame", "apologize", "make amends"},
    # 균형
    {"homeostasis", "rebalance", "equal", "baseline"},
    # 즉시/결국
    {"immediately", "incredibly"},
    # 범위
    {"narrow down", "scope", "breadth"},
    # 우주·물리
    {"universe", "physics"},
    # 마찬가지/반대로
    {"likewise", "on the contrary", "rather than"},
    # 동기·효과·결과
    {"motivator", "effect", "outcome"},
    # 깨달음
    {"insight", "eureka moment"},
    # 장소
    {"spot", "nook", "background"},
]


def _groups():
    par = {}
    def f(x):
        par.setdefault(x, x)
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    def u(a, b): par[f(a)] = f(b)
    for w, _, a, _ in SYN_RAW + ANT_RAW: u(w.lower(), a.lower())
    for s in MERGE:
        s = [x.lower() for x in s]
        for x in s[1:]: u(s[0], x)
    for w, _, _ in WORDS: f(w.lower())
    names = {}
    return lambda w: "G%02d" % names.setdefault(f(w.lower()), len(names))

_G = _groups()
SYN = [(w, wm, a, am, _G(w)) for w, wm, a, am in SYN_RAW]
ANT = [(w, wm, a, am, _G(w)) for w, wm, a, am in ANT_RAW]


# ── 4) 목록 밖 오답 풀 (어려운 선지 모드) ───────────────────────
# (영단어, 한글뜻, 품사, group)
# 이번 범위 단어·동의어·반의어와 뜻이 겹칠 수 있는 단어는 넣지 않았다.
EXT = [
    # 동사
    ("hesitate",    "망설이다",           "v", "X_DOUBT"),
    ("pretend",     "~인 척하다",         "v", "X_FAKE"),
    ("complain",    "불평하다",           "v", "X_COMPLAIN"),
    ("betray",      "배신하다",           "v", "X_TRUST"),
    ("regulate",    "규제하다",           "v", "X_LIMIT"),
    ("endure",      "견디다",             "v", "X_KEEP"),
    ("wander",      "돌아다니다",         "v", "X_MOVE"),
    ("imitate",     "모방하다",           "v", "X_COPY"),
    ("interrupt",   "방해하다",           "v", "X_BLOCK"),
    ("negotiate",   "협상하다",           "v", "X_DEAL"),
    ("convince",    "설득하다",           "v", "X_PERSUADE"),
    ("deliver",     "배달하다",           "v", "X_CARRY"),
    ("borrow",      "빌리다",             "v", "X_LEND"),
    ("obey",        "복종하다",           "v", "X_OBEY"),
    ("vanish",      "사라지다",           "v", _G("occur")),
    # 형용사
    ("reluctant",   "꺼리는, 주저하는",   "adj","X_UNWILLING"),
    ("humble",      "겸손한",             "adj","X_HUMBLE"),
    ("stubborn",    "고집 센",            "adj","X_PERSIST"),
    ("fragile",     "부서지기 쉬운",      "adj","X_WEAK"),
    ("hollow",      "속이 빈",            "adj","X_EMPTY"),
    ("shallow",     "얕은",               "adj","X_DEPTH"),
    ("fierce",      "사나운, 격렬한",     "adj","X_FIERCE"),
    ("durable",     "내구성 있는",        "adj","X_PERSIST"),
    ("clumsy",      "서투른",             "adj","X_SKILL"),
    ("greedy",      "탐욕스러운",         "adj","X_GREED"),
    ("cautious",    "조심스러운",         "adj","X_CAREFUL"),
    ("awkward",     "어색한",             "adj","X_SKILL"),
    ("vital",       "필수적인",           "adj","X_VITAL"),
    ("weary",       "지친",               "adj","X_TIRED"),
    ("vivid",       "생생한",             "adj","X_VIVID"),
    ("sincere",     "진심 어린",          "adj","X_HONEST"),
    ("brutal",      "잔인한",             "adj","X_FIERCE"),
    ("dense",       "밀집한, 빽빽한",     "adj","X_DENSE"),
    ("ancient",     "고대의",             "adj","X_OLD"),
    # 명사
    ("burden",      "부담, 짐",           "n",  "X_BURDEN"),
    ("threat",      "위협",               "n",  "X_FEAR"),
    ("rumor",       "소문",               "n",  "X_TALK"),
    ("insult",      "모욕",               "n",  "X_INSULT"),
    ("privilege",   "특권",               "n",  "X_RIGHT"),
    ("obstacle",    "장애물",             "n",  "X_BLOCK"),
    ("sacrifice",   "희생",               "n",  "X_GIVE"),
    ("dispute",     "분쟁, 논쟁",         "n",  "X_CONFLICT"),
    ("shortage",    "부족",               "n",  _G("rich")),
    ("virtue",      "미덕",               "n",  "X_MORAL"),
    ("famine",      "기근",               "n",  "X_HUNGER"),
    ("tradition",   "전통",               "n",  "X_CUSTOM"),
    ("harvest",     "수확",               "n",  "X_FARM"),
    ("debt",        "빚, 부채",           "n",  "X_DEBT"),
    ("rival",       "경쟁자",             "n",  "X_RIVAL"),
    ("ceremony",    "의식, 식",           "n",  "X_EVENT"),
    # 부사
    ("barely",      "간신히, 겨우",       "adv","X_BARELY"),
    ("frequently",  "자주",               "adv","X_OFTEN"),
    ("thoroughly",  "철저히",             "adv","X_CAREFUL"),
    ("sincerely",   "진심으로",           "adv","X_HONEST"),
    ("rarely",      "드물게, 좀처럼 ~않는", "adv","X_OFTEN"),
    ("gradually",   "서서히",             "adv","X_SPEED"),
    ("nearly",      "거의",               "adv","X_BARELY"),
]

if __name__ == "__main__":
    from collections import defaultdict
    G = defaultdict(set)
    for w, _, a, _, g in SYN + ANT: G[g] |= {w, a}
    for w, _, _ in WORDS: G[_G(w)].add(w)
    for g, s in sorted(G.items(), key=lambda x: -len(x[1])):
        print(g, len(s), sorted(s))
    print(len(WORDS), len(SYN), len(ANT), len(EXT))
