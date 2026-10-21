# mock2606_quiz_interactive.html 소스

송우고 1학년 2학기 수행평가 — 2026 6월 고1 학력평가(부산) 22·23·24·32번 단어 시험.
배포 HTML은 여기서 생성한다. HTML을 직접 고치지 말고 이 파일들을 고친 뒤 다시 빌드할 것.

| 파일 | 내용 |
|---|---|
| `vocab.py` | 단어 뜻 84 / 동의어 49 / 반의어 46 / 범위 밖 오답풀 57 + 의미 묶음(MERGE) |
| `passage.py` | 본문 4지문 29문장 (영어 + 해석) |
| `blanks.py` | 본문에서 단어표 단어를 찾아 빈칸 자리 추출 (113개) |
| `sim.py` · `make_data.py` · `build.py` · `template.html` | Lesson 2 앱과 동일 구조 |
| `verify.py` | **원본 PDF ↔ data.json 글자 단위 검수.** 빌드 후 반드시 실행 |

## 빌드 + 검수

```bash
cd src && python3 make_data.py && python3 build.py && python3 verify.py
```

## 원본과 다르게 둔 것 (verify.py 예외)

- 단어 뜻의 `[명]`·`[형]` 품사 표시 제거, PDF 줄바꿈 깨짐 `보상하 다` → `보상하다`
- 반의어(1)의 `pop up`·`outcome`은 반의어(2)에 짝이 없어 제외
- 반의어(1)의 `erode` → `corrode` (본문 23번·단어표 표기, 원장님 확인)
- 36번 지문 제외 (단어표가 22~32번 범위라 빈칸이 1개뿐이었음, 원장님 요청)
- 본문 빈칸 제외: `with ~ in mind`, `hold up A against B`, `replace A with B` (본문에서 떨어져 나오는 숙어)
