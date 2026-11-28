# 요리 레시피 북 — 에이전트 작업 안내

이 폴더는 어떤 AI 에이전트(Claude Code, Codex, Cursor, Gemini CLI 등)로도, 사람이 직접으로도 다룰 수 있게 만들었다.
특정 플랫폼 런타임 없이 브라우저 하나로 돌아간다. 설치할 것은 없다.

## 구조

| 경로 | 역할 | 손대는 경우 |
| --- | --- | --- |
| `data/recipes.json` | 레시피 420개. 한 줄에 레시피 하나. **단일 원본(source of truth)** | 레시피 추가·수정·삭제 |
| `src/template.html` | 화면(CSS + JS). 데이터 자리에 `/*@@RECIPES@@*/[]` 자리표시 | UI·기능 변경 |
| `build.py` | 검증 후 데이터를 템플릿에 넣어 `index.html` 생성 (Python 3 표준 라이브러리만) | 스키마 바꿀 때 |
| `index.html` | 빌드 결과. 더블클릭으로 열린다 (`file://` OK) | **직접 수정 금지** — 빌드로 다시 만든다 |
| `icons/`, `manifest.webmanifest` | 파비콘·홈 화면 아이콘. 원본은 `icons/icon.svg` | 아이콘 바꿀 때 (아래 명령으로 PNG 재생성) |
| `src/sw.js` → `sw.js` | 오프라인 지원 서비스 워커. 빌드가 배포 파일 해시를 캐시 버전으로 넣는다 | 캐시 대상·전략 바꿀 때 (`sw.js`는 직접 수정 금지) |
| `.github/workflows/check.yml` | 푸시마다 `build.py --check` + `index.html`·`sw.js` 최신 여부 검사 | 검사 규칙 바꿀 때 |
| `tools/nutrition_gaps.py` → `reports/` | 영양 정보 없는 레시피 목록·우선순위 (`nutrition-gaps.md`, `.csv`) | 영양 정보를 채운 뒤 다시 실행 |

## 배포

- `main`에 푸시하면 GitHub Pages(https://movtrength.github.io/recipe-book/)에 1~2분 안에 반영된다.
- CI가 실패하면(형식 오류, 또는 `index.html`·`sw.js`를 다시 빌드하지 않음) 오류 메시지대로 고친다.
- 오프라인: 한 번 접속하면 앱·아이콘·사용한 글꼴이 저장돼 데이터 없이도 열린다. 새 배포는 다음 접속 때 백그라운드로 받아 그다음 접속부터 보인다. 새로 추가한 정적 파일을 오프라인에 포함하려면 `src/sw.js`의 `PRECACHE`와 `build.py`의 `SHIPPED`에 같이 넣는다.
- 아이콘 PNG 재생성: `rsvg-convert -w 192 -h 192 icons/icon.svg -o icons/icon-192.png` (512도 같은 방식). `apple-touch-icon.png`는 모서리 없는 정사각형(`rx="0"`), `icon-maskable-512.png`는 가운데 80% 안에 그림을 둔다.

## 작업 순서 (필수)

1. `data/recipes.json` 또는 `src/template.html`을 고친다.
2. `python3 build.py` 실행. 오류가 나면 메시지대로 고치고 다시 실행한다.
3. `index.html`을 브라우저로 열어 확인한다 (`open index.html`).

검증만: `python3 build.py --check`

## 레시피 스키마

```json
{"t":"요리명","en":"English name(선택)","sv":2,"yl":"완성량(선택, sv가 null일 때 표시)",
 "min":10,"heat":"약불 → 강불","c":"밥","cu":"태국","kid":false,
 "tags":["밥"],"al":["계란"],"mise":["팬: 28cm 이상"],
 "ing":[["재료명","2","큰술","메모"]],
 "subs":[["원재료","대체재","메모"]],
 "st":[["조리 단계 문장",1,2,"타이머 종료 알림 문구"]],
 "done":["완성 기준"],"cau":["주의·보관"],"notes":["메모"],
 "src":["출처 이름","https://출처 URL 또는 빈 문자열"],
 "nu":{"sv":"1/2 분량","kcal":350,"na":800,"k":300,"p":150}}
```

| 키 | 의미 | 규칙 |
| --- | --- | --- |
| `t` | 요리명 | 필수. 중복은 경고만 (출처가 다른 같은 요리 허용) |
| `c` | 분류 | `아침 밥 면 국 메인 반찬 샐러드 소스 간식 디저트 음료 기타` 중 하나 |
| `sv` / `min` | 기준 인분 / 총 시간(분) | 양의 정수 또는 `null` |
| `cu` / `heat` | 국가·스타일 / 불 세기 | 문자열 (빈 문자열 가능) |
| `kid` | 콩팥(신장) 식단 레시피 여부 | `true`/`false`, "콩팥 레시피만" 필터에 쓰인다 |
| `ing` | 재료 `[이름, 양, 단위, 메모]` | 모두 문자열. 양은 `"2"`, `"1.5"`, `"2-3"`이면 인분 변경 시 자동 환산, 그 밖의 값(`"약간"`)은 그대로 |
| `st` | 단계 `[문장, 최소분, 최대분, 알림]` | 타이머 없는 단계는 `["문장"]`만. 최소 ≤ 최대, 소수 가능(1.5) |
| `subs` | 대체 재료 `[원재료, 대체재, 메모]` | |
| `nu` | 1회 제공량 영양 정보 또는 `null` | 숫자 키: `kcal carb protein fat satfat chol na k p ca fiber sugar`; `sv`(제공량 설명, 문자열), `approx`(근삿값 여부) |
| `tags` `al` `mise` `done` `cau` `notes` | 문자열 목록 | 빈 목록 가능 |

## 원칙

- 영양 수치·출처는 원문에 있는 값만 넣는다. 추정값은 `notes`에 "제안값"이라고 밝힌다.
- 레시피 하나 = 한 줄 형식을 유지한다 (diff·grep이 쉽다).
- 외부 의존성은 Google Fonts뿐이다. 오프라인이면 시스템 글꼴로 대체되고 기능은 그대로다.
- 데이터는 브라우저 안에서만 쓰인다. 서버·API·로그인·AI 호출이 없다.
