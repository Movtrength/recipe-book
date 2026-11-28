# 영양 정보 보완 대상

레시피 420개 중 153개에 영양 정보(`nu`)가 없다 (있는 267개 출처: kidney.org 225, davita.com 24, kidneycareuk.org 18).
먼저 채울 것은 A등급 0개(원문에 나트륨·칼륨·인이 있다), 다음은 B등급 콩팥 레시피 0개다.

`python3 tools/nutrition_gaps.py`로 다시 만든다. 원문을 직접 연 41개는 `tools/nutrition_checked.json` 결과를, 나머지는 출처 사이트 샘플(1~2쪽) 기준 등급을 쓴다.

| 등급 | 뜻 | 개수 | 콩팥 레시피 | 채우는 방법 |
| --- | --- | ---: | ---: | --- |
| A | 원문에 신장 핵심값 | 0 | 0 | 1회분 표에 나트륨·칼륨·인까지 있음. 그대로 옮기면 된다 |
| B | 원문에 일부 값 | 85 | 0 | 열량·탄수화물 등 일부만, 또는 칼륨·인 없음. 있는 값만 옮긴다 |
| C | 원문 확인 필요 | 0 | 0 | 샘플을 못 봤거나 값이 있을지 불확실 |
| D | 원문에 값 없음 | 68 | 3 | SNS·영상·개인 기록. 채우려면 식품 성분 DB로 직접 계산(추정값 표시) |

| 출처 | 개수 | 등급별 | 원문에 있는 값 |
| --- | ---: | --- | --- |
| dishingouthealth.com | 56 | B56 | 열량·나트륨 등 (저자 계산), 인 없음 |
| instagram.com | 24 | D24 |  |
| (URL 없음) | 15 | D15 |  |
| justonecookbook.com | 10 | B10 | 열량·나트륨·칼륨 등, 인 없음 |
| 10000recipe.com | 9 | D9 | 영양 정보 없음 |
| rachelcooksthai.com | 3 | B3 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| thewoksoflife.com | 3 | B3 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| ksn.or.kr | 3 | D3 | 영양 정보 없음 (재료가 g 단위라 계산하기 쉬움) |
| koreanbapsang.com | 3 | D3 | 영양 정보 없음 |
| youtu.be | 3 | D3 |  |
| youtube.com | 3 | D3 |  |
| chinasichuanfood.com | 2 | B2 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| hungryinthailand.com | 2 | B2 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| recipetineats.com | 2 | B2 | 열량 (인 없음) |
| aaronandclaire.com | 1 | B1 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| christieathome.com | 1 | B1 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| pupswithchopsticks.com | 1 | B1 | 열량·탄수화물·단백질·나트륨 (인 없음) |
| redhousespice.com | 1 | B1 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| thaicaliente.com | 1 | B1 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| theheirloompantry.co | 1 | B1 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| thewoodenskillet.com | 1 | B1 | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| banjo.co.jp | 1 | D1 | 영양 정보 없음 |
| beyondkimchee.com | 1 | D1 | 영양 정보 없음 |
| hot-thai-kitchen.com | 1 | D1 | 영양 정보 없음 |
| japan.recipetineats.com | 1 | D1 | 영양 정보 없음 |
| mrpantry.com | 1 | D1 | 영양 정보 없음 |
| thai-foodie.com | 1 | D1 | 영양 정보 없음 |
| threads.com | 1 | D1 |  |
| usa.lkk.com | 1 | D1 | 영양 정보 없음 |

값은 있지만 신장 핵심값이 빠진 레시피:

- #136 아라비아타 소시지 파스타: na, k, p 없음
- #137 BBQ 풀드포크 버거: na, k, p 없음
- #138 브로콜리·콜리플라워 치즈: na, k, p 없음
- #139 치킨 채소 라자냐: na, k, p 없음
- #140 치킨 파히타 (Kidney Care UK): na, k, p 없음
- #141 치킨 핫팟: na, k, p 없음
- #142 치킨 브로콜리 크림 파스타: na, k, p 없음
- #143 시금치 치즈 크림 탈리아텔레: na, k, p 없음
- #144 바삭 채소 프리터: na, k, p 없음
- #145 간단 소고기 채소 누들: na, k, p 없음
- #146 그린 맥 앤 치즈: na, k, p 없음
- #147 지중해식 치킨 피타: na, k, p 없음
- #148 참치 올리브 푸타네스카 스파게티: na, k, p 없음
- #149 구운 홍피망 치킨 파스타 베이크: na, k, p 없음
- #150 소시지 앤 매시 파이: na, k, p 없음
- #151 소시지 앤 매시: na, k, p 없음
- #152 심플 라자냐: na, k, p 없음
- #153 시금치 파인너트 라자냐: na, k, p 없음
- #267 가지 딥: p 없음
- #374 매콤 닭고기 샐러드: p 없음

## 원칙

- A·B는 원문 수치만 옮기고 1회 제공량(`nu.sv`)을 원문대로 적는다.
- D를 계산으로 채울 때는 `nu.approx: true`로 두고 `notes`에 계산 근거(사용한 DB)를 남긴다.
- 출처에 없는 값을 추정해서 A·B 레시피에 섞지 않는다.

## A. 원문에 신장 핵심값 (0개)

| # | 콩팥 | 요리 | 분류 | 출처 | 원문에 있는 값 |
| ---: | :---: | --- | --- | --- | --- |

## B. 원문에 일부 값 (85개)

| # | 콩팥 | 요리 | 분류 | 출처 | 원문에 있는 값 |
| ---: | :---: | --- | --- | --- | --- |
| 78 |  | 된장 닭구이 | 메인 | [Aaron and Claire](https://aaronandclaire.com/doenjang-dakgui-doenjang-marinated-chicken/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 81 |  | 두반장 생선조림 | 메인 | [China Sichuan Food](https://www.chinasichuanfood.com/braised-spicy-fish-sichuan-style/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 86 |  | 사천식 소고기 셀러리 볶음 | 메인 | [China Sichuan Food](https://www.chinasichuanfood.com/shredded-beef-szechuan-style/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 70 |  | 팟키마오 | 면 | [Christie at Home](https://christieathome.com/blog/thai-drunken-noodles-pad-kee-mao/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 1 |  | 원팟 터메릭 치킨 라이스 | 밥 | [Dishing Out Health](https://dishingouthealth.com/turmeric-chicken-and-rice/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 2 |  | 스위트포테이토 부리토 볼 | 밥 | [Dishing Out Health](https://dishingouthealth.com/sweet-potato-burrito-bowls/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 3 |  | 베트남 새우 쌀국수면 볼 | 면 | [Dishing Out Health](https://dishingouthealth.com/30-minute-vietnamese-shrimp-and-rice-noodle-bowls/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 4 |  | 참깨 쌀국수면 샐러드 | 면 | [Dishing Out Health](https://dishingouthealth.com/rice-noodle-salad/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 6 |  | 골든 칠면조 라이스 스킬렛 | 밥 | [Dishing Out Health](https://dishingouthealth.com/ground-turkey-and-rice-skillet/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 7 |  | 세이지 칠면조 미트볼 호박 오르조 | 메인 | [Dishing Out Health](https://dishingouthealth.com/sage-turkey-meatballs-with-pumpkin-orzo/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 8 |  | 치킨 라이스 수프 | 국 | [Dishing Out Health](https://dishingouthealth.com/immune-boosting-chicken-and-rice-soup/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 9 |  | 30분 브로콜리 볶음밥 강황 타히니 소스 | 밥 | [Dishing Out Health](https://dishingouthealth.com/30-minute-broccoli-fried-rice-with-turmeric-tahini-sauce/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 10 |  | 갈릭 파르메산 구운 콜리플라워 | 반찬 | [Dishing Out Health](https://dishingouthealth.com/parmesan-roasted-cauliflower/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 11 |  | 구운 주키니 파스타샐러드 | 메인 | [Dishing Out Health](https://dishingouthealth.com/roasted-zucchini-pasta-salad/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 12 |  | 구운 채소 글로우볼 | 메인 | [Dishing Out Health](https://dishingouthealth.com/roasted-veggie-glow-bowls/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 13 |  | 레몬 그릭 병아리콩 수프 | 국 | [Dishing Out Health](https://dishingouthealth.com/greek-chickpea-soup/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 14 |  | 레몬 렌틸 구운 가지 샐러드 | 메인 | [Dishing Out Health](https://dishingouthealth.com/lentil-and-roasted-eggplant-salad/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 15 |  | 망고 미소 연어 볼 | 밥 | [Dishing Out Health](https://dishingouthealth.com/mango-miso-salmon-bowls/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 16 |  | 베스트 렌틸 수프 | 국 | [Dishing Out Health](https://dishingouthealth.com/lentil-soup-recipe/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 17 |  | 브로콜리 볶음 | 반찬 | [Dishing Out Health](https://dishingouthealth.com/sauteed-broccoli-recipe/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 18 |  | 사과 오트밀 브레드 | 간식 | [Dishing Out Health](https://dishingouthealth.com/apple-harvest-oatmeal-bread/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 19 |  | 새우 스캄피 오르조 | 메인 | [Dishing Out Health](https://dishingouthealth.com/shrimp-scampi-orzo/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 20 |  | 새우 채소 로메인 볶음면 | 면 | [Dishing Out Health](https://dishingouthealth.com/shrimp-and-veggie-lo-mein/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 21 |  | 새우 타코 크리미 살사 베르데 | 메인 | [Dishing Out Health](https://dishingouthealth.com/easy-shrimp-tacos/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 22 |  | 스킬렛 포블라노 호박 엔칠라다 | 메인 | [Dishing Out Health](https://dishingouthealth.com/skillet-poblano-and-pumpkin-enchiladas/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 23 |  | 시금치 아티초크 스킬렛 엔칠라다 | 메인 | [Dishing Out Health](https://dishingouthealth.com/spinach-artichoke-skillet-enchiladas/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 24 |  | 시금치 아티초크 연어 스킬렛 | 메인 | [Dishing Out Health](https://dishingouthealth.com/spinach-artichoke-salmon-skillet/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 25 |  | 시트러스 미소 진저 당근 샐러드 | 반찬 | [Dishing Out Health](https://dishingouthealth.com/carrot-salad/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 26 |  | 시트팬 버터넛 소시지 뇨끼 | 메인 | [Dishing Out Health](https://dishingouthealth.com/sheet-pan-butternut-squash-and-sausage-gnocchi/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 27 |  | 시트팬 치킨소시지 채소구이 | 메인 | [Dishing Out Health](https://dishingouthealth.com/sheet-pan-chicken-sausage-and-veggies/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 28 |  | 시트팬 칠리 레몬 연어 | 메인 | [Dishing Out Health](https://dishingouthealth.com/sheet-pan-chili-lemon-salmon/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 29 |  | 시트팬 페스토 뇨끼 | 메인 | [Dishing Out Health](https://dishingouthealth.com/sheet-pan-pesto-gnocchi/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 30 |  | 연어 타코 아보카도 크레마 | 메인 | [Dishing Out Health](https://dishingouthealth.com/salmon-tacos/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 31 |  | 오렌지 메이플 글레이즈 연어 | 메인 | [Dishing Out Health](https://dishingouthealth.com/orangemapleglazedsalmon/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 32 |  | 와일드라이스 버섯 수프 | 국 | [Dishing Out Health](https://dishingouthealth.com/wild-rice-mixed-mushroom-soup/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 33 |  | 원스킬렛 레몬 페퍼 새우 오르조 | 메인 | [Dishing Out Health](https://dishingouthealth.com/one-skillet-lemon-pepper-shrimp-and-orzo/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 34 |  | 원팟 스페인식 콩밥 | 밥 | [Dishing Out Health](https://dishingouthealth.com/spanish-rice-and-beans-one-pot/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 35 |  | 원팟 토스카나 소시지 렌틸콩 | 메인 | [Dishing Out Health](https://dishingouthealth.com/sausage-and-lentils/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 36 |  | 원팟 하리사 새우 페타 오르조 | 메인 | [Dishing Out Health](https://dishingouthealth.com/one-pot-harissa-shrimp-and-feta-orzo/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 37 |  | 원팬 옥수수 코코넛 만두 | 메인 | [Dishing Out Health](https://dishingouthealth.com/one-pan-sweet-corn-coconut-dumplings/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 38 |  | 원팬 크리미 토마토 파스타 | 면 | [Dishing Out Health](https://dishingouthealth.com/one-pan-pasta/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 39 |  | 지중해 렌틸 샐러드 | 반찬 | [Dishing Out Health](https://dishingouthealth.com/mediterranean-lentil-salad/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 40 |  | 지중해 파스타 | 면 | [Dishing Out Health](https://dishingouthealth.com/mediterranean-pasta/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 41 |  | 치킨 소시지 오르조 방울토마토 | 메인 | [Dishing Out Health](https://dishingouthealth.com/one-pan-chicken-sausage-orzo/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 42 |  | 치킨 엔칠라다 퀴노아 베이크 | 메인 | [Dishing Out Health](https://dishingouthealth.com/easy-chicken-enchilada-quinoa-bake/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 43 |  | 치킨 캐슈 크런치 샐러드 | 메인 | [Dishing Out Health](https://dishingouthealth.com/chicken-cashew-salad/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 44 |  | 치폴레 비네그레트 | 소스 | [Dishing Out Health](https://dishingouthealth.com/copycat-chipotle-vinaigrette/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 45 |  | 치폴레 새우 타코 아보카도 망고 살사 | 메인 | [Dishing Out Health](https://dishingouthealth.com/chipotle-shrimp-tacos/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 46 |  | 퀴노아 채소 파워볼 | 메인 | [Dishing Out Health](https://dishingouthealth.com/quinoa-power-bowls-with-maple-chipotle-brussels-and-smoky-butternut-squash/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 47 |  | 크리스피 치폴레 블랙빈 타코 | 메인 | [Dishing Out Health](https://dishingouthealth.com/black-bean-tacos/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 48 |  | 태국식 땅콩 치킨 퀴노아 | 메인 | [Dishing Out Health](https://dishingouthealth.com/thai-peanut-chicken-quinoa/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 49 |  | 토마토 버터빈 스튜 | 국 | [Dishing Out Health](https://dishingouthealth.com/butter-bean-stew/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 50 |  | 토스카나 칠면조 흰강낭콩 스킬렛 | 메인 | [Dishing Out Health](https://dishingouthealth.com/tuscan-turkey-and-white-bean-skillet/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 51 |  | 파스타 에 체치 병아리콩 스튜 | 국 | [Dishing Out Health](https://dishingouthealth.com/pasta-e-ceci/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 52 |  | 하베스트 가을 샐러드 캐러멜 샬롯 드레싱 | 메인 | [Dishing Out Health](https://dishingouthealth.com/harvest-fall-salad/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 53 |  | 허니 세서미 치킨 시트팬 | 메인 | [Dishing Out Health](https://dishingouthealth.com/honey-sesame-chicken/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 54 |  | 호박 프로틴 팬케이크 | 간식 | [Dishing Out Health](https://dishingouthealth.com/pumpkin-protein-pancakes/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 55 |  | 흰강낭콩 레몬 수프 | 국 | [Dishing Out Health](https://dishingouthealth.com/white-bean-soup/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 163 |  | 발사믹 두부 | 메인 | [Dishing Out Health](https://dishingouthealth.com/balsamic-tofu-20-minutes/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 164 |  | 데리야키 두부 브로콜리 | 메인 | [Dishing Out Health](https://dishingouthealth.com/teriyaki-tofu-and-broccoli/) | 열량·나트륨 등 (저자 계산), 인 없음 (사이트 샘플 기준) |
| 58 |  | 치킨 파인애플 카레 볶음밥 | 밥 | [Hungry in Thailand](https://hungryinthailand.com/chicken-pineapple-fried-rice/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 59 |  | 카이란 치킨 볶음밥 | 밥 | [Hungry in Thailand](https://hungryinthailand.com/chicken-thai-fried-rice/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 61 |  | 오야코동 | 밥 | [Just One Cookbook](https://www.justonecookbook.com/oyakodon/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 62 |  | 규동 | 밥 | [Just One Cookbook](https://www.justonecookbook.com/gyudon/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 72 |  | 데리야키 돼지고기 덮밥 | 밥 | [Just One Cookbook](https://www.justonecookbook.com/teriyaki-pork-donburi/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 73 |  | 장어덮밥 | 밥 | [Just One Cookbook](https://www.justonecookbook.com/unagi-don/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 82 |  | 메기 카바야키 덮밥 | 밥 | [Just One Cookbook](https://www.justonecookbook.com/catfish-kabayaki/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 83 |  | 방어 데리야끼 | 메인 | [Just One Cookbook](https://www.justonecookbook.com/yellowtail-teriyaki/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 87 |  | 소고기 데리야끼 스테이크 | 메인 | [Just One Cookbook](https://www.justonecookbook.com/beef-teriyaki/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 89 |  | 연어 데리야끼 | 메인 | [Just One Cookbook](https://www.justonecookbook.com/teriyaki-salmon-recipe/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 93 |  | 카바야키 타레 | 소스 | [Just One Cookbook](https://www.justonecookbook.com/homemade-unagi-sauce/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 161 |  | 두부 닭고기 함박스테이크 | 메인 | [Just One Cookbook](https://www.justonecookbook.com/chicken-tofu-hamburger-steak/) | 열량·나트륨·칼륨 등, 인 없음 (사이트 샘플 기준) |
| 69 |  | 소고기 차우펀 | 면 | [Pups with Chopsticks](https://pupswithchopsticks.com/beef-chow-fun/) | 열량·탄수화물·단백질·나트륨 (인 없음) |
| 56 |  | 카오팟까이 닭고기 볶음밥 | 밥 | [Rachel Cooks Thai](https://rachelcooksthai.com/khao-pad-gai/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 67 |  | 팟씨유 | 면 | [Rachel Cooks Thai](https://rachelcooksthai.com/pad-see-ew/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 68 |  | 랏나 | 면 | [Rachel Cooks Thai](https://rachelcooksthai.com/rad-na/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 77 |  | 데리야끼 치킨 미트볼 | 메인 | [RecipeTin Eats](https://www.recipetineats.com/teriyaki-chicken-meatballs/) | 열량 (인 없음) |
| 88 |  | 어향가지 돼지고기 볶음 | 메인 | [RecipeTin Eats](https://www.recipetineats.com/chinese-eggplant-and-minced-pork/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 75 |  | 대만식 우육면 | 면 | [Red House Spice](https://redhousespice.com/taiwanese-beef-noodle-soup/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 57 |  | 태국식 치킨 토마토 볶음밥 | 밥 | [Thai Caliente](https://thaicaliente.com/thai-fried-rice-with-chicken-khao-phat-gai/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 63 |  | 데리야키 치킨 덮밥 | 밥 | [The Heirloom Pantry](https://theheirloompantry.co/teriyaki-chicken-bowl-donburi/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 71 |  | 회과육 | 메인 | [The Woks of Life](https://thewoksoflife.com/twice-cooked-pork/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 85 |  | 사천 삼초계 | 메인 | [The Woks of Life](https://thewoksoflife.com/sichuan-three-pepper-chicken/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 162 |  | 가상두부 돼지고기 두부볶음 | 메인 | [The Woks of Life](https://thewoksoflife.com/home-style-tofu-stir-fry/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |
| 76 |  | 데리야끼 새우 | 메인 | [The Wooden Skillet](https://thewoodenskillet.com/teriyaki-shrimp/) | 열량·탄수화물·단백질·나트륨·칼륨 (인 없음) |

## C. 원문 확인 필요 (0개)

| # | 콩팥 | 요리 | 분류 | 출처 | 원문에 있는 값 |
| ---: | :---: | --- | --- | --- | --- |

## D. 원문에 값 없음 (68개)

| # | 콩팥 | 요리 | 분류 | 출처 | 원문에 있는 값 |
| ---: | :---: | --- | --- | --- | --- |
| 109 | ● | 우엉밥 | 밥 | [대한신장학회](https://ksn.or.kr/upload/general/ebook/1%EA%B6%8C%20%ED%88%AC%EC%84%9D%20%EC%A0%84%20%EB%8B%A8%EA%B3%84%EC%9D%98%20%EB%A7%8C%EC%84%B1%EC%BD%A9%ED%8C%A5%EB%B3%91%20%ED%99%98%EC%9E%90%EB%A5%BC%20%EC%9C%84%ED%95%9C%20%EC%98%81%EC%96%91-%EC%8B%9D%EC%83%9D%ED%99%9C%20%EA%B4%80%EB%A6%AC.pdf) | 영양 정보 없음 (재료가 g 단위라 계산하기 쉬움) |
| 110 | ● | 닭가슴살 샐러드, 가지구이와 발사믹 소스 | 메인 | [대한신장학회](https://ksn.or.kr/upload/general/ebook/1%EA%B6%8C%20%ED%88%AC%EC%84%9D%20%EC%A0%84%20%EB%8B%A8%EA%B3%84%EC%9D%98%20%EB%A7%8C%EC%84%B1%EC%BD%A9%ED%8C%A5%EB%B3%91%20%ED%99%98%EC%9E%90%EB%A5%BC%20%EC%9C%84%ED%95%9C%20%EC%98%81%EC%96%91-%EC%8B%9D%EC%83%9D%ED%99%9C%20%EA%B4%80%EB%A6%AC.pdf) | 영양 정보 없음 (재료가 g 단위라 계산하기 쉬움) |
| 111 | ● | 저염오이김치 | 반찬 | [대한신장학회](https://ksn.or.kr/upload/general/ebook/1%EA%B6%8C%20%ED%88%AC%EC%84%9D%20%EC%A0%84%20%EB%8B%A8%EA%B3%84%EC%9D%98%20%EB%A7%8C%EC%84%B1%EC%BD%A9%ED%8C%A5%EB%B3%91%20%ED%99%98%EC%9E%90%EB%A5%BC%20%EC%9C%84%ED%95%9C%20%EC%98%81%EC%96%91-%EC%8B%9D%EC%83%9D%ED%99%9C%20%EA%B4%80%EB%A6%AC.pdf) | 영양 정보 없음 (재료가 g 단위라 계산하기 쉬움) |
| 0 |  | 태국식 계란 볶음밥 | 밥 | 직접 기록 |  |
| 95 |  | 치킨 알프레도 스파게티스쿼시 | 메인 | - |  |
| 96 |  | 치킨 페타 원팬 파스타 | 메인 | - |  |
| 97 |  | 크리미 레몬 치킨 파스타 | 메인 | - |  |
| 98 |  | 페스토 치킨 파스타 베이크 | 메인 | - |  |
| 99 |  | 레몬 페타 치킨 오르조 | 메인 | - |  |
| 100 |  | 지중해 토마토 올리브 치킨 | 메인 | - |  |
| 101 |  | 크리미 치킨 펜네 | 메인 | - |  |
| 102 |  | 레몬그라스 치킨 쌀국수면 볼 | 면 | - |  |
| 103 |  | 분짜 돼지고기 미트볼 | 면 | - |  |
| 104 |  | 치킨 포 가 | 면 | - |  |
| 172 |  | 갈아서 만드는 감자구이 | 반찬 | [사용자 붙여넣기 텍스트 "갈아서 만드는 감자구이 (+ 고구마 버전)"](user-paste) |  |
| 173 |  | 고구마구이 | 반찬 | [사용자 붙여넣기 텍스트 "갈아서 만드는 감자구이 (+ 고구마 버전)" 메모](user-paste) |  |
| 406 |  | 연어장 | 반찬 | 지인 레시피 |  |
| 417 |  | 수비드 풀드포크 | 메인 | 직접 기록 |  |
| 64 |  | 닭가슴살 덮밥 | 밥 | [만개의레시피](https://www.10000recipe.com/recipe/7007123) | 영양 정보 없음 |
| 65 |  | 소고기 덮밥 | 밥 | [만개의레시피](https://www.10000recipe.com/recipe/6968408) | 영양 정보 없음 |
| 66 |  | 돼지고기 김치찌개 | 국 | [만개의레시피](https://www.10000recipe.com/recipe/6961294) | 영양 정보 없음 |
| 79 |  | 된장 삼겹살구이 | 메인 | [만개의레시피](https://www.10000recipe.com/recipe/7017228) | 영양 정보 없음 |
| 108 |  | 볶음쌀국수 | 면 | [만개의레시피](https://www.10000recipe.com/recipe/6892011) | 영양 정보 없음 |
| 157 |  | 간장 두부조림 | 반찬 | [만개의레시피](https://www.10000recipe.com/recipe/6885373) | 영양 정보 없음 |
| 158 |  | 두부계란덮밥 | 밥 | [만개의레시피](https://www.10000recipe.com/recipe/7065344) | 영양 정보 없음 |
| 159 |  | 닭가슴살 두부 동그랑땡 | 반찬 | [만개의레시피](https://www.10000recipe.com/recipe/7008424) | 영양 정보 없음 |
| 160 |  | 두부 데리야끼 덮밥 | 밥 | [만개의레시피](https://www.10000recipe.com/recipe/7055257) | 영양 정보 없음 |
| 411 |  | 연어 새우 초밥 케이크 | 밥 | [BANJO FOODS "Sushi cake" + chef-choice 블로그(간장새우 소스)](https://banjo.co.jp/en/recipes/206) | 영양 정보 없음 |
| 80 |  | 된장 연어구이 | 메인 | [Beyond Kimchee](https://www.beyondkimchee.com/soybean-paste-glazed-salmon/) | 영양 정보 없음 |
| 107 |  | 꾸어이띠여우 쿠어 까이 | 면 | [Hot Thai Kitchen](https://hot-thai-kitchen.com/rice-noodles-chicken-guay-tiew-kua-gai/) | 영양 정보 없음 |
| 105 |  | 소고기 무 솥밥 | 밥 | [Instagram @dailybbokki](https://www.instagram.com/reel/DeEUaPmq5Am/) |  |
| 106 |  | 매콤 우삼겹 갈비탕 | 국 | [Instagram @jjongal.kim](https://www.instagram.com/reel/DeGwsKYzEYT/) |  |
| 155 |  | 감바스 짜파게티 | 면 | [Instagram reel @sudal_foodie (캡션+음성 전사)](https://www.instagram.com/reel/Des9lWCIQsL/) |  |
| 156 |  | 오징어볶음 | 반찬 | [Instagram reel (캡션+화면 자막, 음성 트랙 없음)](https://www.instagram.com/reel/DeREh8OzGu7/) |  |
| 166 |  | 지도리우동 | 면 | [Instagram reel (캡션+화면 자막, 음성 트랙 없음)](https://www.instagram.com/reel/De6DaURhZg4/) |  |
| 167 |  | 니꾸쟈가 | 메인 | [Instagram reel @sagwa.haus (캡션 레시피, 음성 트랙 없음)](https://www.instagram.com/reel/Deyjg4GSYGD/) |  |
| 168 |  | 고구마 맛탕 | 간식 | [Instagram reel (캡션+화면 자막, 음성은 음악뿐)](https://www.instagram.com/reel/DdXpHoYSU2k/) |  |
| 170 |  | 돈테키 | 메인 | [Instagram reel @plate_on_ (캡션 레시피, 음성 트랙 없음)](https://www.instagram.com/reel/DaUehSQMawx/) |  |
| 174 |  | 마라샹궈 | 메인 | [Instagram @sukkitchen_ "집에서 하이디라오"](https://www.instagram.com/reel/DfHeoSRzTK-/) |  |
| 175 |  | 계란김밥 | 메인 | [Instagram @sukkitchen_ "집에서 하이디라오"](https://www.instagram.com/reel/DfHeoSRzTK-/) |  |
| 176 |  | 버터치킨카레 | 메인 | [Instagram @eongcook "버터치킨카레"](https://www.instagram.com/reel/DeeDuGAMzKw/) |  |
| 177 |  | 알배추수육 | 메인 | [Instagram @32_cactus "초간단 20분 알배추수육"](https://www.instagram.com/reel/DdafanXz88C/) |  |
| 179 |  | 우삼겹들깨수제비 | 메인 | [Instagram @jaytable_ "초초간단 우삼겹 들깨수제비" (캡션만 사용, 댓글 미사용)](https://www.instagram.com/reel/DfO5eDehFqh/) |  |
| 180 |  | 계란참치주먹밥 | 간식 | [Instagram @bop.pt (밥피티), 레시피 출처 @food.recipe942](https://www.instagram.com/reel/DewFdl5KOxU/) |  |
| 407 |  | 닭고기 부추 계란덮밥 | 밥 | [인스타그램 @꽁이네 집밥사랑](https://www.instagram.com/reel/Dfwgvk5IqDe/) |  |
| 408 |  | 집코바 | 메인 | [인스타그램 @dule.table](https://www.instagram.com/reel/DfieIVdP4W8/) |  |
| 409 |  | 부타노가쿠니 (삼겹살 간장조림) | 메인 | [인스타그램 @salim.hwang](https://www.instagram.com/reel/DfrMhOQhhIv/) |  |
| 410 |  | 대왕 연어초밥 (대만 스타일) | 밥 | [인스타그램 @yummandu_](https://www.instagram.com/reel/DeDlWm4hQBA/) |  |
| 412 |  | 마늘폭탄갈비살 | 메인 | [인스타그램 릴스](https://www.instagram.com/reel/Df0vcSKCs3Y/) |  |
| 413 |  | 전자레인지 김파스타 | 면 | [인스타그램 @food_radio_](https://www.instagram.com/reel/Df17y4XTEaL/) |  |
| 414 |  | 가리비 솥밥 | 밥 | [인스타그램 @di_yori](https://www.instagram.com/reel/Df2BbMuTsnK/) |  |
| 415 |  | 고등어 솥밥 | 밥 | [인스타그램 @sonmeallog](https://www.instagram.com/reel/Df4EiyGBPMm/) |  |
| 416 |  | 갈비 솥밥 | 밥 | [인스타그램 @soo.sumi](https://www.instagram.com/reel/Df1rq3ISU4A/) |  |
| 419 |  | 대왕 연어초밥 (간장소스) | 밥 | [인스타그램 @livelong_food](https://www.instagram.com/reel/DdYvn2WyW07/) |  |
| 92 |  | 정어리 카바야키 | 메인 | [RecipeTin Japan](https://japan.recipetineats.com/sardine-kabayaki-grilled-sardines-with-sweet-soy-glaze/) | 영양 정보 없음 |
| 74 |  | 맥적 | 메인 | [Korean Bapsang](https://www.koreanbapsang.com/dwaejigogi-doenjang-gui/) | 영양 정보 없음 |
| 84 |  | 보쌈 수육 | 메인 | [Korean Bapsang](https://www.koreanbapsang.com/bossam-boiled-pork-wraps/) | 영양 정보 없음 |
| 94 |  | 해물 된장찌개 | 국 | [Korean Bapsang](https://www.koreanbapsang.com/seafood-doenjang-jjigae/) | 영양 정보 없음 |
| 90 |  | 연어 카바야키 덮밥 | 밥 | [Mr Pantry](https://www.mrpantry.com/recipes/salmon-kabayaki-don-japanese-glazed-salmon-rice-bowl) | 영양 정보 없음 |
| 60 |  | 태국식 카오팟 치킨 채소 볶음밥 | 밥 | [Thai Foodie](https://thai-foodie.com/thaifood/thai-stir-fried-rice-recipe-khaw-pad-gai/) | 영양 정보 없음 |
| 171 |  | 닭다리살 양송이 버터볶음 | 메인 | [Threads @todaynote_j "닭다리살 양송이 버터볶음" (본문 텍스트)](https://www.threads.com/@todaynote_j/post/DfChtoHH7hj) |  |
| 91 |  | 장어소스 닭꼬치 | 메인 | [Lee Kum Kee](https://usa.lkk.com/en/foodservices/recipes/yakitori-recipe) | 영양 정보 없음 |
| 5 |  | 홍석천 팟타이 | 면 | [백만뷰 집쿡라이브 CJ ENM 200816 (영상 댓글 레시피)](https://youtu.be/7KcX-u5b_tc) |  |
| 165 |  | 수비드 통삼겹살 | 메인 | [YouTube 영상 설명란 레시피 (자막 없음)](https://youtu.be/PSyXy-aoTcw) |  |
| 418 |  | 호텔식 스크램블 에그 | 아침 | [YouTube 라꼰즈 | Rakkonz (집밥 백선생 편집)](https://youtu.be/aazMtxj2UZk) |  |
| 154 |  | 닭똥집 볶음 | 반찬 | [-](https://youtube.com/shorts/pSFEQGJPfvo) |  |
| 169 |  | 통삼겹 카레 | 메인 | [YouTube Shorts "최강록 셰프식 통삼겹 카레" (한국어 자막+화면)](https://youtube.com/shorts/n0uG9D3gDFg) |  |
| 178 |  | 아게다시도후 | 반찬 | [YouTube 후니아재 hoonilife "일본에서 유명한 두부요리 아게다시도후"](https://www.youtube.com/watch?v=BatOSAfC_Vg) |  |
