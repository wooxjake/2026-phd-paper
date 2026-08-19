# 참고문헌 작업 메모

## 하위 폴더 대조 메모

2026-08-13에 `references/`와 하위 폴더를 대조하였다.

- `references/Cited Papers/`에는 현재 안내용 `README.md`만 있으며, `cited` 상태 문헌의 원문 PDF는 아직 주로 `references/` 루트에 보관되어 있다. 본문 인용 상태는 이 문서의 `cited` 표기를 기준으로 판단하며, PDF의 `Cited Papers/` 이전은 별도 정리 작업이 필요하다.
- `references/introduce/`에는 아직 이 문서에 등록하지 않은 PDF가 있다. 아래 자료는 원문 PDF만 확보된 상태이며, 저자·연도·저널·표본·절차·장비·URL을 원문에서 검증한 뒤 `candidate` 항목으로 등록한다.
  - `Evidence for sitting time standard guidelines a narrative review of sedentary behavior.pdf` — 2026-08-13 텍스트 추출 시도 결과 12쪽 전부 이미지 스캔본이어서 본문을 읽을 수 없다. 등록하려면 OCR 또는 KCI 원문(https://doi.org/10.21797/ksme.2020.22.4.001) 확보가 필요하다. 서지사항은 조정환, 송금주 (2020). 좌식행동 가이드라인 기준 개발을 위한 기초연구. 한국체육측정평가학회지, 22(4), 1-12로 확인되며, 원저가 아니라 내러티브 리뷰이므로 좌식시간 수치의 근거가 아니라 지표·패턴 논의의 인용으로만 사용한다.
  - `Global, regional, and national burden of low back pain, 1990–2020, its attributable risk factors, and projections to 2050 a systematic analysis of the Global Burden of Disease.pdf`
- 2026-08-13에 `The contribution of office work to sedentary behaviour associated risk.pdf`를 원문에서 검증하여 `33. Parry & Straker (2013)` 항목으로 등록하였다. `.txt` 추출본을 같은 폴더에 함께 보관한다.
- 2026-08-13에 청소년 스마트폰 관련 PDF 2편(`Association between Problematic Smartphone Use and Physical Activity among Adolescents…`, `Relationship between smartphone use and sedentary behavior a school-based study with adolescents`)을 삭제하였다. 서론의 좌식시간 근거로 검토했으나 (1) 대상이 청소년이어서 본 연구의 성인 표본과 불일치하고, (2) 두 편 모두 단면조사여서 좌식시간의 증가 추세를 뒷받침하지 못하며, (3) Jeong et al. (2023)은 경로모형에서 좌식시간이 원인 변수이고 결과가 신체활동이므로 "스마트폰 사용이 좌식시간을 늘린다"는 방향의 근거가 아니기 때문이다.
- 2026-08-13에 `references/introduce/`의 아래 2편을 원문에서 검증하여 `31. Smith et al. (2015)`, `32. Clemes et al. (2014)` 항목으로 등록하였다. 두 PDF는 각각 `.txt` 추출본을 같은 폴더에 함께 보관한다.
  - `Office workers' objectively measured sedentary behavior and physical activity during and outside working hours.pdf`
  - `Weekday and weekend patterns of objectively measured sitting, standing, and stepping in a sample of office-based workers the active buildings study.pdf`
- `introduce/`의 마지막 GBD 자료는 이 문서의 `GBD 2021 Low Back Pain Collaborators (2023)` 항목과 제목상 동일한 원문으로 보인다. 다만 PDF 파일명만으로는 동일성, 판본 및 보관 이력을 확정하지 않았으므로 현재 항목의 보관 위치는 갱신하지 않는다.

---

## 해결 완료 — Kett et al. (2021) 재인용의 원출처 3편

2026-08-13에 원출처 3편을 모두 확보하여 `34. Healy et al. (2011)`, `35. Clemes, Patel, Mahon, & Griffiths (2014)`, `36. van der Velde et al. (2017)` 항목으로 등록하고, 서론 문단 1의 재인용 표기를 직접 인용으로 교체하였다. 각 PDF와 `.txt` 추출본은 `references/introduce/`에 보관한다.

**8.4~9.3시간 범위의 정체가 확인되었다.** Kett et al. (2021)의 해당 문장은 세 연구의 평균값 중 최소와 최대를 묶은 범위였다.

| 문헌 | 표본 | 측정 | 보고값 |
| --- | --- | --- | --- |
| Healy et al. (2011) | 미국 20세 이상 N=4,757 (NHANES 2003-06) | ActiGraph 7164, <100 cpm | **8.44시간/일 (SD 1.45)** — 착용시간 14.6시간의 약 58% |
| Clemes, Patel, Mahon, & Griffiths (2014) | 영국 사무직 N=72 | 만보계 + 자가기입 일지 | 근무일 517±144분(8시간 37분) / 비근무일 339±137분(5시간 37분) |
| van der Velde et al. (2017) | 네덜란드 40-75세 N=2,024 | activPAL3 (자세 판별) | **9.3시간/일 (SD 1.6)** — 남 9.8, 여 8.8 |

하한 8.44는 Healy, 상한 9.3은 van der Velde에서 나온다.

**인용 방침.** 서론 문단 1의 일일 좌식시간 범위는 Healy et al. (2011)과 van der Velde et al. (2017) 두 편만 직접 인용한다. Clemes, Patel, Mahon, & Griffiths (2014)의 8시간 37분은 근무일에 한정된 값이고 측정도 자가기입 일지이므로 전일 평균을 제시하는 두 편과 성격이 달라 범위 인용에서 제외하였다. 다만 이 문헌은 **직장 좌식이 하루 총 좌식시간의 63%를 차지한다**는 별도 근거로 같은 문단에 인용한다.

**32번 처리.** `32. Clemes, O'Connell, & Edwardson (2014)`(_JOEM_)은 원출처가 아니었으며, 2026-08-13에 서론 문단 1에서 인용을 제외하고 상태를 `candidate`로 되돌렸다. 근무시간 좌식 비율은 `33. Parry & Straker (2013)`(81.8%)이 담당한다. 35번과 제1저자·연도가 같으므로 향후 두 문헌을 함께 인용할 경우 APA 7에 따라 공저자를 밝혀 구분한다.

**확보 과정의 오류 기록.** 2026-08-13에 원출처를 찾는 과정에서 제1저자와 연도만 보고 `Clemes, O'Connell, & Edwardson (2014, JOEM)`을 원출처로 잘못 확보하였다. 해당 연구의 근무일 좌식시간이 중앙값 580분(약 9.7시간)으로 8.4~9.3시간 범위 밖이라는 점에서 오류가 드러났고, Kett 원문의 참고문헌 목록을 직접 확인하여 바로잡았다. **재인용을 직접 인용으로 교체할 때에는 인용 문헌의 참고문헌 목록에서 서지사항 전체를 확인한다.**

---

## 2026-08-19 — EMG·IMU 선행연구 대조와 미등록 문헌 정리

지속 좌식 프로토콜(1시간 이내)에서 EMG 또는 IMU를 사용한 문헌을 전수 대조하고, 그 과정에서 확인된 자료 문제 3건을 처리하였다.

### 1. 파일명 불일치 수정

`references/Immediate Effects of Dynamic Sitting Exercise on the Lower Back Mobility of Sedentary Young Adults.pdf`와 동명 `.txt`의 **실제 내용이 Zawadka et al. (2023)**(20번 항목)이었다. PDF 첫 페이지를 pypdf로 추출해 확인한 결과 *Ergonomics* 게재본 표지와 저자명이 나왔다. 두 파일을 `The influence of sedentary behaviour on lumbar-pelvic kinematics during squatting and forward bending among physically active students.pdf/.txt`로 변경하고, 전문을 근거로 20번 상세 파일의 「원문 확인이 필요하다」 표기를 모두 검증된 값으로 교체하였다. 원래 받으려던 `Immediate Effects of Dynamic Sitting Exercise…`는 확보되어 있지 않다.

**교훈.** PDF를 저장할 때 파일명을 수동으로 입력하면 다른 논문의 제목이 들어갈 수 있다. 등록 전 첫 페이지의 제목·저자를 반드시 대조한다.

### 2. 8번(Baker et al., 2018) 장비 기재 보완

상세 파일에 운동학 장비가 「골반 움직임」으로만 적혀 있었으나, 원문 확인 결과 **3 Space Fastrak(Polhemus Navigation Sciences Division), 25Hz, 10초 표본, 센서 T12·L1·S2 극돌기**를 사용하였고 **요부 각도를 시상면상 T12-S2 상대각**으로 산출하였다. 두 가지를 상세 파일에 반영하였다.

- 이 정의는 **본 연구의 IMU 기반 요추각(T12-S2)과 산출 구조가 동일**하므로 측정 변인 정의의 선례로 사용할 수 있다.
- 다만 **전자기식 추적 장치이지 IMU가 아니므로** "IMU 선행연구"로 인용하지 않는다. 각도 수치도 본 연구 값과 직접 비교하지 않는다.

### 3. 미등록 문헌 3편 등록

`references/`에 원문이 있으나 색인에 없던 3편을 원문에서 검증하여 등록하였다.

| 번호 | 문헌 | 등록 사유 |
| --- | --- | --- |
| 37 | Alshehri et al. (2025), _J Clin Med_ 14(21), 7518 | IMU 요추각 신호처리 절차(자이로 바이어스 보정, Gradient Descent Filter, 쿼터니언 ZXY 변환)와 **기립 요추각 중앙값을 기준 0°로 정의**한 방식 |
| 38 | Zarnegar et al. (2026), _BMC Sports Sci Med Rehabil_ 18, 289 | 30분 구부정 좌식 프로토콜의 표준화(견봉-L1-대전자 93°±3°)와 운동군-비운동군 비교 설계 |
| 39 | Paloschi et al. (2021), _Sensors_ 21(19), 6610 | **T12-S1 상대각 기반 전만각의 측정 타당도(광학식 대비 최대 RMSE 5.6°)** |

3편 모두 `candidate`이며 아직 본문에 인용하지 않았다.

### 4. 대조 결과 — EMG 피로 지표의 검출 실패 패턴

지속 좌식 중 EMG 피로 지표(MDF/MPF)의 검출 여부를 산출법별로 정리하면 아래와 같다. 본 연구가 30분 세션에서 피로를 결과변인으로 삼을지 결정할 때의 근거다.

| 산출법 | 문헌 | 좌식 시간 | 요부 신전근 결과 |
| --- | --- | --- | --- |
| 첫 5분 vs 마지막 5분 | 10. Jung et al. (2021) | 30분 | **유의차 없음** |
| 첫 5분 vs 마지막 5분 | 23. Jia & Nussbaum (2018) | 40분 | 일부 검출(무지지 + 전기자극 반응 병행) |
| 10분 블록 6구간 | 13. Waongenngarm et al. (2015b) | 60분 | **유의차 없음**(IO/TrA만 구부정 자세에서 감소) |
| 30분 간격 5회 | 8. Baker et al. (2018) | 120분 | **유의차 없음**(요부 각도·골반 움직임도 유의차 없음) |
| **정규화 중앙주파수 회귀기울기** | 11. Areeudomwong et al. (2012) | **30분** | **검출** |
| 10분 블록 3구간 | 19. Saiklang et al. (2022) | 41분 | 검출(만성요통군, 2000Hz, ECG 아티팩트 육안 검수) |

**첫-끝 2점 비교는 30분·60분·120분에서 모두 실패했고, 회귀기울기 방식은 30분에서 검출에 성공하였다.** 본 연구에서 EMG 피로를 산출한다면 첫-끝 비교가 아니라 다구간 블록의 회귀기울기를 일차 산출법으로 삼는다.

### 5. EMG와 IMU를 함께 사용한 문헌

수집 문헌 전체에서 **2편뿐**이다.

- **23. Jia & Nussbaum (2018)** — EMG 12근육(TeleMyo 900, 1000Hz) + IMU(Xsens MVN, 100Hz, **T10·S1**), 40분
- **4. Wong et al. (2018)** — EMG 6근육(Telemyo Noraxon, 1500Hz) + IMU(MyoMOTION, 100Hz, **T12·S1**), 20분

**T12-S2 조합으로 EMG를 함께 측정한 선행연구는 수집 문헌 안에 없다.** 본 연구의 신규성 지점으로 서론·연구방법에서 사용할 수 있다.

---
## 2026-08-19 (2) — method 폴더 구성과 방법론 문헌 확보 목록

`memo.md`(Areeudomwong 2012 정독), `memo2.md`(Jia & Nussbaum 2018 정독), `memo3.md`(RVC·LLA·EMG/IMU 대조)의 방법론 내용을 `method/`의 6개 주제 폴더에 분배하였다. 각 파일은 「선행연구 대조표 → 본 연구 프로토콜(안) → 참고문헌 → 미결 사항」 구조를 공통으로 갖는다.

| 폴더 | 파일 |
| --- | --- |
| 1. Subjects | `1-1_피험자_선정_및_집단정의.md` |
| 2. Sitting Time | `2-1_좌식_세션_프로토콜.md` |
| 3. EMG - fatigue,RVC | `3-1_EMG_측정_프로토콜.md`, `3-2_정규화_RVC.md`, `3-3_피로지표_산출.md` |
| 4. IMU - LLA | `4-1_IMU_측정_프로토콜.md`, `4-2_LLA_산출변인.md` |
| 5. Survey | `5-1_설문_및_주관적_지표.md` |
| 6. Statistic | `6-1_통계분석_설계.md` |

### 확보해야 할 방법론 문헌 (우선순위순)

| 순위 | 문헌 | 용도 | 링크 |
| --- | --- | --- | --- |
| ~~1~~ | ~~**Cotter, Nairn, & Drake (2014).**~~ → **2026-08-19 확보 완료.** `40. Cotter, Nairn, & Drake (2014)`로 등록 | **해결: 요추는 기립 기준** | https://doi.org/10.1016/j.jbiomech.2014.04.023 |
| 2 | **Dankaerts et al. (2004).** Reliability of EMG measurements for trunk muscles during maximal and sub-maximal voluntary isometric contractions in healthy controls and CLBP patients. _JEK_, 14(3), 333-342 | 체간근 RVC 정규화 채택의 직접 근거 | https://www.google.com/search?q=%22Reliability+of+EMG+measurements+for+trunk+muscles+during+maximal+and+sub-maximal+voluntary+isometric+contractions%22 |
| 3 | **Hermens et al. (2000).** Development of recommendations for SEMG sensors and sensor placement procedures. _JEK_, 10(5), 361-374 | 전극 위치·피부준비의 국제 표준(SENIAM). 수집 문헌 3편이 인용 | https://pubmed.ncbi.nlm.nih.gov/11018445/ · http://www.seniam.org/pdf/contents5.PDF |
| 4 | **Cifrek et al. (2009).** Surface EMG based muscle fatigue evaluation in biomechanics. _Clin Biomech_, 24(4), 327-340 | MDF 회귀기울기를 피로 지수로 쓰는 방식의 근거 | https://www.clinbiomech.com/article/S0268-0033(09)00025-4/abstract |
| 5 | **Riddick et al. (2023).** Estimation of human spine orientation with IMU at low sampling rate: How low can we go? _J Biomech_, 157, 111726 | IMU 샘플링레이트 하한 근거 | https://www.google.com/search?q=%22Estimation+of+human+spine+orientation+with+inertial+measurement+units%22+%22How+low+can+we+go%22 |
| 6 | **van Dieën et al. (1993)** | MPF 산출 절차의 직접 근거(Jia가 인용) | https://www.google.com/search?q=van+Dieen+1993+EMG+median+power+frequency+back+muscle+fatigue |
| 7 | **Faul et al. (2007).** G*Power 3. _Behav Res Methods_, 39(2), 175-191 | 표본크기 산출 근거. `etc/g-power/`에 프로그램만 있고 문헌 미등록 | https://www.google.com/search?q=%22G*Power+3%3A+A+flexible+statistical+power+analysis+program%22 |
| 8 | **Luttmann, Jäger, & Laurig (2000).** Electromyographical indication of muscular fatigue in occupational field studies | JASA(진폭-주파수 결합 분석) 원출처 | https://www.google.com/search?q=%22Electromyographical+indication+of+muscular+fatigue+in+occupational+field+studies%22+Luttmann |
| 9 | **Borg (1990)**, **Corlett & Bishop (1976)**, **Kuorinka et al. (1987)**, **Craig et al. (2003)** | 불편감 척도(Borg CR-10, 신체부위 불편감, NMQ)와 IPAQ의 원출처 | `method/5. Survey/5-1_설문_및_주관적_지표.md` 참조 |
| 10 | **Burden (2010)**, **Mathiassen, Winkel, & Hägg (1995)** | 정규화 방법론 일반 리뷰 및 RVC 개념 원출처 | `method/3. EMG - fatigue,RVC/3-2_정규화_RVC.md` 참조 |
| 11 | **Merletti & Cerone (2020).** Tutorial. Surface EMG detection, conditioning and pre-processing | 20Hz 고역 하한 선택 근거 | https://www.google.com/search?q=%22Surface+EMG+detection%2C+conditioning+and+pre-processing%3A+Best+practices%22+Merletti |
| 12 | **Madgwick, Harrison, & Vaidyanathan (2011).** Gradient descent algorithm for IMU/MARG orientation | 쿼터니언 처리를 택할 경우 필요 | https://www.google.com/search?q=%22Estimation+of+IMU+and+MARG+orientation+using+a+gradient+descent+algorithm%22 |

### 설계상 확인된 충돌 2건

**(1) 「표준 직립자세 기준 RVC」는 근거 문헌이 없다.** `outline.md` III-4의 EMG 진폭 정규화 계획이 이에 해당한다. 수집 문헌 전수 검색 결과 **표면 EMG를 기립 자세 근활성으로 정규화한 문헌은 0편**이며, 조용한 기립에서 요추기립근 활성이 노이즈 수준이라 분모가 불안정해지는 방법론적 문제가 있다. Baker et al. (2018)의 하위최대 RVC 과제(복와위 슬관절 90° 굴곡, 양 무릎 5cm 거상, 3초 × 3회)로 대체할 것을 권고한다. 표준 직립자세는 **IMU 기준각 산출용으로만** 사용한다.

**(2) Slump 역치를 Chen & Zhang (2025)의 MDC로 잡을 수 없다.** `outline.md` III-4 (2)의 계획이 이에 해당한다. Chen & Zhang은 **광학 동작분석(BTS Smart-D140, 100Hz), 반사마커 5개(이주·견봉·대전자·슬관절 외측상과·외측복사뼈), 체간 각도(TA), 5초 측정**으로 본 연구의 T12-S2 IMU 요추각과 장비·부착 위치·산출 변인이 모두 다르다. 대안으로 Paloschi et al. (2021)의 **T12-S1 상대각 광학식 대비 최대 RMSE 5.6°**를 보수적 하한으로 쓰거나, IMU 요추각의 MDC/SEM을 보고한 문헌을 별도로 탐색해야 한다.

### 연도 정정

`02. Kim et al.`의 게재 연도가 여러 문서에 **2025**로 표기되어 있었다. 원문 확인 결과 `J. Clin. Med. 2024, 13, 2728`(투고 2024-03-27, 게재 2024-05-06)이므로 **2024**가 맞다. `references/entries/02-kim-et-al-2024.md`, `outline.md`(2곳), `references/참고우선순위.md`를 정정하였다.

---

## 2026-08-19 (3) — Cotter, Nairn, & Drake (2014) 확보와 기준자세 확정

같은 날 `Should a standing or seated reference posture be used when normalizing seated spine kinematics.pdf`가 `references/`에 추가되어 원문을 검증하고 **`40. Cotter, Nairn, & Drake (2014)`**로 등록하였다. `.txt` 추출본을 같은 폴더에 함께 보관한다.

**서지**: Cotter, B. D., Nairn, B. C., & Drake, J. D. M. (2014). _Journal of Biomechanics_, 47(10), 2371-2377. https://doi.org/10.1016/j.jbiomech.2014.04.023 · https://www.sciencedirect.com/science/article/pii/S0021929014002486

### 결론 — 요추는 기립 기준자세다

남성 13명, Vicon MX 카메라 7대 50Hz, 강체판 8개(T1·T4·T5·T8·T9·T12·L1·PSIS)로 척추를 4분절로 나누고 좌위 ROM을 `%STAND`와 `%SIT`로 각각 정규화해 2×6 반복측정 ANOVA로 비교하였다.

| 각도 유형 | 권고 기준자세 |
| --- | --- |
| 전역각 — 모든 분절·모든 평면 | **기립** |
| 상대각 굴곡 — 상부흉추 · 하부흉추 · **요추(L1-PSIS)** | **기립** |
| 상대각 굴곡 — 중부흉추(T5-T8) | **착석** (유일한 예외, 본 연구 범위 밖) |
| 상대각 측굴·회전 — 모든 분절 | **기립** |

저자 권고는 **"착석과 기립 기준자세를 모두 수집해 분절별로 더 큰 각도를 채택하되, 하나만 수집해야 한다면 기립으로 충분하다"**이다. 본 연구가 표준 직립자세와 좌식 시작값을 모두 기록하려던 계획과 일치한다.

### 반드시 구분해야 할 점

Cotter가 답한 것은 **분모(최대 ROM)를 어느 자세에서 얻는가**이지, 시계열 각도의 **기준 오프셋(0°)을 어디에 두는가**가 아니다. Cotter 자신은 0점을 **착석용·기립용으로 각각 따로** 잡았다 — 각 시행의 **첫 1초 자료를 평균**해 참여자·분절별로 산출했고, 그 결과 0°(=0%Max)가 각 자세의 직립과 동등해진다.

- **%ROM 방식**(Wong·O'Sullivan 계열) → 분모는 **기립 최대 ROM**
- **절대 각도 편차 방식**(Kim의 LLA_dev 계열) → 0점은 **좌식 시작값(LLA_start)**, 기립 값은 별도 기술통계
- 두 방식을 모두 산출해 함께 보고하는 것이 가장 안전하다.

### 함께 갱신한 문서

`memo3.md` 1.4(c)·1.5(3)·1.6·4장, `method/4. IMU - LLA/4-1_IMU_측정_프로토콜.md` 3절, `method/4. IMU - LLA/4-2_LLA_산출변인.md` 미결 4번, `method/3. EMG - fatigue,RVC/3-2_정규화_RVC.md` 4(b)·미결 1번.

**부수 확인**: 이 문헌으로 「표준 직립자세」의 용도가 명확해졌다. **IMU 요추각의 기준자세로는 근거가 확보되었고**(Cotter), **EMG 진폭 정규화 기준으로는 여전히 근거가 없다**(수집 문헌 0편). `outline.md`의 "표준 직립자세 기준 RVC(%RVC)"는 두 용도를 분리해 수정해야 한다.

---
