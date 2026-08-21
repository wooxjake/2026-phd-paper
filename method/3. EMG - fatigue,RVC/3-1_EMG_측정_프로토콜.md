# 3-1. EMG 측정 프로토콜 (전극·피부준비·수집 파라미터)

출처: `memo.md` 방법 절, `memo2.md` EMG·신호처리 절, `memo3.md` 1장. 작성일 2026-08-19.

---

## 1. 전극 부착 위치 — 선행연구 대조

### 1.1 요추기립근 (Erector Spinae, Lumbar)

| 문헌 | 부착 위치 |
| --- | --- |
| **Jia & Nussbaum (2018)** | **L3 극돌기에서 외측 3-4cm, 근섬유와 평행** |
| **Baker et al. (2018)** | 흉부 요장늑근(iliocostalis lumborum pars thoracis), **L1 극돌기 높이에서 정중선과 외측연의 중간** |
| **Waongenngarm et al. (2015b)** | 장늑근(ICL): **L1 극돌기 높이, 정중선과 신체 외측면의 중간** (SENIAM) |
| **Makhsous et al. (2009)** | 방척추근, **극돌기에서 3cm** |
| **outline.md 현재 계획** | **L3 높이 극돌기 외측 2-3cm 양측** |

> **Jia(3-4cm)와 현재 계획(2-3cm)이 다르다.** L3 높이에서 외측 2cm는 다열근 영역과 겹칠 수 있다. Jia의 3-4cm 또는 SENIAM 권고를 따르는 편이 crosstalk가 적다.

### 1.2 다열근 (Multifidus)

| 문헌 | 부착 위치 |
| --- | --- |
| **Jia & Nussbaum (2018)** | **L3/L4 극돌기에서 외측 1-2cm** |
| **Waongenngarm et al. (2015b)** | **L5 높이, 극돌기에서 2cm** (SENIAM) |
| **Areeudomwong et al. (2012)** | **L5 높이, 후상장골극과 L1-L2 극간을 잇는 가상선에 평행** |
| **O'Sullivan et al. (2012)** | **L5** |
| **Zawadka et al. (2023)** | SENIAM 프로토콜 — 후상장골극 미측 첨부에서 L1/L2 극간을 잇는 선상, **L5 극돌기 높이(정중선에서 약 2-3cm)** |

### 1.3 그 밖의 체간근 (Jia & Nussbaum, 2018)

| 근육 | 위치 |
| --- | --- |
| 흉추기립근(ET) | T9/T10 극돌기 외측 4-5cm |
| 내복사근(IO) | 배꼽 외측 10-12cm, 서혜인대 상방 |
| 외복사근(EO) | 제12늑골과 전상장골극 사이 중점 |
| 복직근(RA) | 배꼽 외측 2-3cm |

**대안 IO/TrA 위치**: **전상장골극에서 정중면 쪽으로 1cm** (Areeudomwong 2012, Waongenngarm 2015b, Jung 2021 공통)

### 1.4 근육 위치 확인 — 촉진 및 저항수축 검증 절차

전극 위치는 "뼈 지표 촉진 → 근육 확인 → 저항 수축으로 검증"의 3단계로 잡는다. 근육별 난이도가 다르므로 절차를 구분한다.

**(1) 요추기립근 — 상대적으로 용이**

1. 극돌기를 하나씩 촉진해 L3를 확인한다. 골반 최상단(장골능)이 대략 L4 높이라는 것을 보조 기준으로 쓴다.
2. **O'Sullivan et al. (2012)의 요령**: 극돌기 촉진은 **약간 굴곡된 좌위 자세**에서 시행하면 더 쉽다. 척추 굴곡 시 극돌기 사이 간격이 벌어져 뼈 돌기가 더 뚜렷하게 만져진다(원문: `spinal levels...were identified by manual palpation in a slightly flexed sitting posture`).
3. L3에서 외측 3-4cm 지점의 근육 융기부에 전극을 놓는다.

**(2) 다열근 — 까다로움(요추기립근보다 얕고 좁으며 인접 근육과의 crosstalk 위험이 크다)**

1. 양측 후상장골극(PSIS)을 촉진한다.
2. L1-L2 극간 위치를 확인한다.
3. 두 지점을 잇는 가상선을 그리고, 그 선 위에서 L5 높이·정중선 외측 2-3cm 지점에 전극을 놓는다(SENIAM/Zawadka 방식). 단순히 "L5 옆 몇 cm"가 아니라 이 방향 기준선을 따라야 다열근의 근섬유 주행과 일치해 인접 요장늑근으로부터의 crosstalk을 줄일 수 있다.

**(3) IO/TrA — 뼈 지표는 뚜렷하나 근육을 완전히 분리할 수 없다**

1. 전상장골극(ASIS)을 촉진한다 — 골반 앞쪽에서 뚜렷하게 만져지는 뼈 돌기라 난이도가 낮다.
2. ASIS에서 정중면 쪽 1cm 지점에 전극을 놓는다.
3. **주의**: 내복사근과 복횡근은 표면 EMG로 완전히 분리되지 않는다. 이 위치의 신호는 두 근육의 혼합 신호이며, 표기도 관례적으로 "IO/TrA"로 묶어 쓴다.

**(4) 공통 검증 — 저항 수축 시 신호 확인**

O'Sullivan et al. (2012)이 명시한 절차다.

> `Good electrode contact was confirmed by visually examining the sEMG output while applying manual resistance.`

전극 부착 후 해당 근육이 관여하는 동작에 **도수 저항을 가하면서 EMG 신호가 뚜렷하게 증가하는지 화면으로 확인**한다. 신호가 약하거나 다른 근육 동작에도 크게 반응하면 위치를 재조정한다.

| 근육 | 검증용 저항 동작 |
| --- | --- |
| 요추기립근 | 체간 신전(뒤로 젖히기)에 저항 |
| 다열근 | 체간 신전 + 경미한 회전 저항 |
| IO/TrA | 체간 회전 또는 복부당김기법(abdominal drawing-in maneuver)에 저항 |

### 1.5 좌우 양측 부착 이유 — 편측 측정의 문제

본 연구는 모든 근육을 **양측**(좌·우) 부착한다. 편측 측정만으로는 아래 4가지 문제가 생긴다.

**(1) 좌우 비대칭은 실제로 존재하고, 예측할 수 없다**

Jia & Nussbaum (2018)이 12개 근육을 양측 모두 측정한 결과, 같은 근육인데도 좌우 결과가 정반대로 나온 사례가 있다.

| 근육 | 좌측 | 우측 |
| --- | --- | --- |
| 외복사근(EO) | **유의** p=0.03 | 비유의 p=0.86 |
| 복직근(RA) | 비유의 p=0.12 | **유의** p=0.03 |

만약 외복사근을 우측에만 부착했다면 "변화 없음"으로, 좌측에만 부착했다면 "변화 있음"으로 결론이 뒤바뀐다. **어느 쪽을 측정하느냐가 결과 자체를 좌우한다.**

**(2) 좌식 중 하중은 비대칭적으로 걸린다**

Jung et al. (2021)이 인용한 선행 관찰이다.

> 좌식 중 만성요통 환자는 **둔부 압력 분포가 비대칭적인 패턴**을 보였다.

본 연구는 자발적 자세 변화를 무피드백으로 관찰하는 설계이므로, 참여자가 스스로 자세를 바꿀 때 순수한 시상면 이동이 아니라 한쪽으로 체중을 옮기며 비틀리는 경우가 발생할 수 있다. 편측 측정은 이 비틀림이 측정하지 않는 쪽에서 일어났을 때 신호 자체를 놓친다.

**(3) 편측 측정으로 아무것도 검출하지 못한 선행 사례가 있다**

Baker et al. (2018)은 승모근·외복사근·요추기립근·대퇴직근·대퇴이두근 5개 근육 **전부를 우측에만** 부착하였다(원문: `secured with tape over the following muscles: right side upper trapezius...`). 이 연구는 **120분을 관찰하고도 EMG 진폭·MDF 어디서도 유의한 변화를 찾지 못한** 유일한 연구다. 편측 측정이 원인이라고 단정할 수는 없으나(관찰시간·저강도 근활성 등 다른 요인도 있다), 좌우 비대칭이 확인된 근육들을 하필 한쪽만 측정한 연구에서 이런 결과가 나왔다는 점은 참고할 만하다.

**(4) 양측 측정은 전극 부착 오류의 자가 검증 수단이 된다**

편측 신호만 있으면 그 값이 실제 근활성 변화인지, 전극이 살짝 잘못 부착되어 나온 잡음인지 구분할 방법이 없다. 양측이 있으면 두 채널의 궤적을 대조해, 한쪽만 튀는 값이 나올 경우 전극 문제를 의심할 근거를 얻는다. 통계적으로도 좌우를 평균하거나 개별 채널로 모형에 투입하면 단일 채널의 측정 잡음이 결과 전체를 흔드는 영향이 줄어든다(`method/6-1` 좌우 채널 통합 방법과 연동).

---

## 2. 전극 규격과 피부 준비 — 선행연구 대조

| 문헌 | 전극 | 전극간거리 | 피부 준비 |
| --- | --- | --- | --- |
| **Areeudomwong et al. (2012)** | Ag/AgCl 원형 활성 접착식 (EL 503, BIOPAC) | **2.5cm (중심간)** | **제모 → 알코올 세정 → 고운 사포 연마, 임피던스 5kΩ 미만** (Hermens et al., 2000 인용) |
| **Waongenngarm et al. (2015b)** | 전치증폭 이극 건식 재사용 전극 (SX230, Biometrics), 접촉면 1cm² | **20mm** | 알코올 스왑, **임피던스 5kΩ 미만** |
| **Saiklang et al. (2022)** | Ag/AgCl 일회용 (EL 503), 접촉면 1cm² | **2.5cm (중심간)** | 연마 + 알코올 세정 |
| **Zawadka et al. (2023)** | Ag/AgCl 자가부착 일회용 원형, 접촉면 1cm² (SORIMEX) | **2cm** | 필요 시 제모, 알코올 세정 |
| **Baker et al. (2018)** | Ag/AgCl 자가부착 일회용, **겔 지름 6mm** (Neuroplus, Vermed) | **20mm** (승모근) | 고운 사포 연마 |
| **O'Sullivan et al. (2012)** | 이극 전치증폭 원형, **지름 12mm** | **18mm 고정** | 육안으로 접촉 확인(도수 저항 시 출력 관찰) |
| **Jia & Nussbaum (2018)** | 일회용 이극 Ag/AgCl (AccuSensor, Lynn Medical) | 명시 없음 | 명시 없음 |

**접지 전극**

- Areeudomwong: **양측 전상장골극과 장골능**에 2개
- Waongenngarm: **우측 장골능**
- Baker: **견봉**
- O'Sullivan: **척골경상돌기**

---

## 3. 수집 파라미터 — 선행연구 대조

| 문헌 | 장비 | 샘플링 | 대역통과 | 노치 | 증폭·CMRR |
| --- | --- | --- | --- | --- | --- |
| **Jia & Nussbaum (2018)** | TeleMyo 900 (Noraxon) × 2대 8채널 | 1,000Hz | **20-400Hz** | — | 하드웨어에서 **50ms 이동창 RMS** → 100Hz 다운샘플 |
| **Wong et al. (2018)** | Telemyo (Noraxon), MR 3.10.2 | 1,500Hz | 10-500Hz | — | — |
| **Waongenngarm et al. (2015a)** | — | 1,500Hz | **20-450Hz** | — | **4차 영위상 필터** |
| **Waongenngarm et al. (2015b)** | PS900 (Biometrics) | 1,000Hz | **20-450Hz** | — | 아날로그 차동증폭, **CMRR >96dB @60Hz, 총 이득 1,000** |
| **Jung et al. (2021)** | — | 1,000Hz | **20-450Hz** | — | 전파정류 후 처리 |
| **Areeudomwong et al. (2012)** | Biopac MP35 | 1,000Hz | **30-500Hz** | — | **이득 ×1,000, CMRR 85dB** |
| **Saiklang et al. (2022)** | Cometa Mini Wave Plus 16ch | **2,000Hz** | 10-500Hz | **60Hz** (태국 전원) | 원신호 **ECG 아티팩트 육안 검수** |
| **Baker et al. (2018)** | — | 2,000Hz | 10-1,000Hz (증폭기 내) | — | LabVIEW로 평균제거·정류·육안 검수 |
| **Lopez et al. (2024)** | Delsys | 2,000Hz | **20-350Hz** | — | 정류 후 10Hz 저역통과 (linear envelope) |
| **O'Sullivan et al. (2012)** | Motion Lab Systems MA-300 | 1,000Hz/채널 | **0-500Hz** | — | 이득 2,000, **CMRR >100dB @60Hz** |
| **Zawadka et al. (2023)** | Myon 무선 (동작분석 통합) | 1,000Hz | **10-450Hz 4차 무위상 Butterworth** | — | 정류 → 100ms 이동평균 |

**정리**

- **샘플링 1,000-2,000Hz**가 표준. 주파수 분석에는 1,000Hz면 충분하다(Nyquist 500Hz > 관심 대역 상한).
- **고역 하한은 20Hz가 다수.** 10Hz 이하(Baker, Zawadka, O'Sullivan)는 움직임 아티팩트와 ECG 저주파 성분을 통과시켜 **MDF를 낮추는 방향으로 오염**시킨다. 자발적 자세 재교정이 일어나는 본 연구 설계에서는 특히 문제가 된다.
- **저역 상한은 400-500Hz.** Lopez의 350Hz는 낮은 편.
- **노치 필터는 Saiklang만 사용.** 주파수 분석에서 60Hz 노치는 MDF를 왜곡할 수 있으므로, 전원 잡음이 실제로 문제일 때만 적용하고 적용 여부를 보고한다.

---

## 4. 본 연구 프로토콜(안)

### 4.1 측정 근육

| 우선순위 | 근육 | 위치 | 근거 |
| --- | --- | --- | --- |
| **필수** | **요추기립근 양측** | **L3 극돌기 외측 3-4cm, 근섬유 평행** | Jia & Nussbaum (2018) |
| **필수** | **내복사근/복횡근(IO/TrA) 양측** | **전상장골극에서 정중면 쪽 1cm** | Jia(2018, 40분·4/6 복부 채널 유의), Waongenngarm(2015b, 60분·유일하게 유의한 근육), Areeudomwong(2012, 30분·유의) — **세 편 모두에서 반응성이 확인된 유일한 복부 근육** |
| **권고** | **다열근 양측** | **L5 극돌기 외측 2-3cm, 후상장골극-L1/L2 극간 연결선에 평행** | SENIAM / Zawadka (2023), Areeudomwong (2012) |
| 선택 | 복직근(RA) 양측 | 배꼽 외측 2-3cm | Jia(2018)·Waongenngarm(2015b) 모두 비유의. 굴곡근이라 좌식 안정화 과제와 기능적으로 덜 맞음 |
| 선택(근거 약함) | 외복사근(EO) 양측 | 늑골연 최하점-반대측 치골결절 연결선 | Baker(2018) 단독 비유의, Jia(2018)에서 편측 불일치(좌 유의·우 비유의) |

> **2026-08-19 결정 — IO/TrA를 필수로 격상하였다.** 상세 근거는 `3-4_복부채널_포함여부.md` 참조. 요약: Jia & Nussbaum(2018, 본 연구와 조건이 가장 가까운 40분 무지지 의자 좌식)에서 복부 6채널 중 4채널이 유의하게 변했고, 이는 등 근육 6채널 중 5채널 유의와 거의 같은 비율이다. Waongenngarm(2015b)·Areeudomwong(2012)도 IO/TrA에서 유의한 변화를 보고하였다. **등만 측정하면 요추기립근-IO/TrA로 구성된 심부 코어 안정화 시스템의 절반을 놓친다.**

### 4.2 전극과 피부 준비

- **전극**: Ag/AgCl 일회용 이극, 접촉면 약 1cm²
- **전극간거리**: **20mm** (SENIAM 권고). Areeudomwong·Saiklang의 25mm도 허용 범위
- **피부 준비**: **제모(필요 시) → 고운 사포 연마 → 알코올 세정**, 임피던스 **5kΩ 미만** 확인 (Areeudomwong, Waongenngarm 공통)
- **위치 확인**: 촉진으로 뼈 지표를 먼저 찾고, **도수 저항 수축 시 EMG 신호 증가를 육안으로 확인**한 뒤 전극을 고정한다 — 절차는 1.4절 참조
- **부착 측**: **양측(좌·우) 전부 부착** — 편측 측정의 문제는 1.5절 참조
- **접지**: 장골능 또는 견봉
- **고정**: 양면테이프로 전극과 리드선을 고정해 세션 중 이탈·움직임 방지 (Waongenngarm)

### 4.3 수집 파라미터 (확정안)

| 항목 | 값 | 근거 |
| --- | --- | --- |
| 샘플링레이트 | **1,000Hz** (장비가 지원하면 2,000Hz) | Jia, Waongenngarm, Jung |
| 대역통과 | **20-450Hz** | Waongenngarm(a·b), Jung — **하한 20Hz 고정** |
| 필터 유형 | **4차 영위상(zero-phase) Butterworth** | Waongenngarm (2015a), Zawadka (2023) |
| 노치 | **기본 미적용.** 전원 잡음이 확인되면 60Hz 적용하고 보고 | Saiklang(적용) vs 나머지(미적용) |
| 아티팩트 검수 | **원신호를 ECG 아티팩트에 대해 육안 검수** | Saiklang (2022), Baker (2018) |
| 진폭 처리 | 정류 후 **RMS 이동창** — 창 길이 확정 필요 | Jia 50ms(하드웨어) |
| 동기화 | RMS EMG를 **IMU 샘플링레이트에 맞춰 다운샘플** | Jia — 100Hz로 다운샘플해 운동학과 시간축 정렬 |

### 4.4 제외·결측 처리

- **BMI 30 초과 제외** — 표면 EMG 측정 곤란 (Jia & Nussbaum, 2018)
- 육안 검수 결과 아티팩트가 있는 **특정 참여자·특정 시점의 채널 자료를 개별 제외**하고 그 수를 보고한다 (Baker: 요추기립근 1명, 대퇴이두근 5명, 외복사근 2명 제외를 명시)
- 이상치(**IQR 1.5배 초과**) 제거 (Baker, 2018)
- **저활성 에포크 제외 기준은 별도 문서 3-3에서 정의한다.**

---

## 5. 참고문헌

- Areeudomwong, P., Puntumetakul, R., Kaber, D. B., Wanpen, S., Leelayuwat, N., & Chatchawan, U. (2012). Effects of handicraft sitting postures on lower trunk muscle fatigue. *Ergonomics*, 55(6), 693-703. https://www.researchgate.net/publication/223135407_Effects_of_handicraft_sitting_postures_on_lower_trunk_muscle_fatigue
- Baker, R., Coenen, P., Howie, E., Williamson, A., & Straker, L. (2018). The short term musculoskeletal and cognitive effects of prolonged sitting during office computer work. *IJERPH*, 15(8), 1678. https://doi.org/10.3390/ijerph15081678 · https://www.mdpi.com/1660-4601/15/8/1678
- Jia, B., & Nussbaum, M. A. (2018). *Ergonomics*, 61(12), 1671-1684. https://doi.org/10.1080/00140139.2018.1497815
- Jung, K.-S., Jung, J.-H., In, T.-S., & Cho, H.-Y. (2021). *Medicina*, 57(1), 3. https://doi.org/10.3390/medicina57010003
- Lopez, E. J., Lohman, E. B., Daher, N., Alameri, M., & Dudley, R. I. (2024). *International Journal of Exercise Science*, 17(1), 1280-1293. https://pmc.ncbi.nlm.nih.gov/articles/PMC11728583/
- Makhsous, M., et al. (2009). *BMC Musculoskeletal Disorders*, 10, 17. https://doi.org/10.1186/1471-2474-10-17
- O'Sullivan, K., McCarthy, R., White, A., O'Sullivan, L., & Dankaerts, W. (2012). Can we reduce the effort of maintaining a neutral sitting posture? A pilot study. *Manual Therapy*, 17(6), 566-571. https://doi.org/10.1016/j.math.2012.05.016
- Saiklang, P., Puntumetakul, R., & Chatprem, T. (2022). *IJERPH*, 19(3), 1904. https://doi.org/10.3390/ijerph19031904
- Waongenngarm, P., Rajaratnam, B. S., & Janwantanakul, P. (2015a). *Journal of Physical Therapy Science*, 27(7), 2183-2187. https://doi.org/10.1589/jpts.27.2183
- Waongenngarm, P., Rajaratnam, B. S., & Janwantanakul, P. (2015b). *Safety and Health at Work*, 7(1), 49-54. https://doi.org/10.1016/j.shaw.2015.08.001
- Wong, A. Y. L., et al. (2018). *Gait & Posture*. https://doi.org/10.1016/j.gaitpost.2018.10.028
- Zawadka, M., et al. (2023). *Ergonomics*, 66(1), 101-112. https://doi.org/10.1080/00140139.2022.2061051

### 확보 필요 문헌 (전극 표준)

- **Hermens, H. J., Freriks, B., Disselhorst-Klug, C., & Rau, G. (2000). Development of recommendations for SEMG sensors and sensor placement procedures. *Journal of Electromyography and Kinesiology*, 10(5), 361-374.**
  - PubMed: https://pubmed.ncbi.nlm.nih.gov/11018445/
  - 기관 리포지터리: https://research.utwente.nl/en/publications/development-of-recommendations-for-semg-sensors-and-sensor-placem/
  - SENIAM 원문서 PDF: http://www.seniam.org/pdf/contents5.PDF
  - **Areeudomwong(2012)이 피부 준비 절차의 근거로, Waongenngarm(2015b)·Zawadka(2023)가 전극 위치의 근거로 인용한 문헌.** 방법 절에 "SENIAM 권고에 따라 부착하였다"고 쓰려면 반드시 필요하다.

- **Merletti, R., & Cerone, G. L. (2020). Tutorial. Surface EMG detection, conditioning and pre-processing: Best practices. *Journal of Electromyography and Kinesiology*, 54, 102440.**
  - PubMed 검색: https://pubmed.ncbi.nlm.nih.gov/?term=Surface+EMG+detection+conditioning+and+pre-processing+Best+practices
  - 구글 검색: https://www.google.com/search?q=%22Surface+EMG+detection%2C+conditioning+and+pre-processing%3A+Best+practices%22+Merletti
  - 필터 설정과 아티팩트 처리의 최신 권고. 20Hz 고역 하한 선택의 근거로 쓸 수 있다.

---

## 6. 미결 사항

| # | 항목 |
| --- | --- |
| 1 | 요추기립근 부착 위치를 L3 외측 2-3cm(현 계획)에서 **3-4cm(Jia)**로 변경할지 결정 |
| 2 | ~~IO/TrA 채널 추가 여부~~ → **2026-08-19 확정: 필수 포함.** 남은 것은 IO/TrA 전용 RVC 과제 확정(`3-4` 미결 2) |
| 3 | 다열근 포함 여부 및 위치(L3/L4 Jia vs L5 SENIAM) 확정 |
| 4 | 장비 확정(Noraxon TeleMyo 계열 검토 중) 및 실제 샘플링·필터 사양 확인 |
| 5 | RMS 이동창 길이 확정 |
| 6 | 노치 필터 적용 여부를 예비측정의 전원 잡음 수준으로 결정 |
| 7 | 좌우 채널 통합 방법(평균 vs 각각 분석) 확정 — 1.5절에서 Jia(2018)의 좌우 반대 결과 사례를 확인했으므로 **평균보다 개별 채널 분석을 우선 검토**할 근거가 생겼다 |
| 8 | EMG-IMU 동기화 방식(공통 타임스탬프 또는 동기화 신호) 확정 |
