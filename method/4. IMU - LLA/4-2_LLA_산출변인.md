# 4-2. LLA 산출 변인 및 파생 변인

출처: `memo3.md` 2.4-2.5절, `outline.md` III-4 (2)·(3). 작성일 2026-08-19.

---

## 1. Kim et al. (2024)의 2변인 체계 — 채택 기반

Kim은 3분 시계열에서 두 변인을 뽑는다. **본 연구가 직접 준용할 정의다.**

### (1) LLA_avg — 전만의 크기

> **Sum_LLA를 검사 시간으로 나눈 값.** Sum_LLA는 **사다리꼴 공식(trapezoidal rule)으로 LLA를 시간 가중 적분**한 값.

### (2) LLA_dev — 전만의 유지도

> **LLA_start**(검사 시작 시점의 LLA)로부터의 편차. 각 시점의 LLA와 LLA_start의 차이를 전 시간에 대해 적분한 뒤(**Sum_dev**) 검사 시간으로 나눈다.

**⚠ 부호 해석 주의**

> 대부분의 검사에서 시간에 따라 감소 경향이 나타나므로, **LLA_dev가 클수록(0에 가까울수록) 유지가 좋고, 작을수록(더 음수일수록) 후만 방향 이동이 크다.**

### Kim의 결과 — 직관과 반대다

| 조건 | LLA_avg (크기) | LLA_dev (유지도) |
| --- | --- | --- |
| **곧게 앉기(I_upright)** | **9.9 ± 12.0°** (큼, p<0.001, **d=1.6**, power=1.00) | **−3.7 ± 3.9°** (유지 **나쁨**) |
| 평소대로 앉기(I_usual) | −6.6 ± 15.4° | −1.2 ± 2.4° (유지 좋음, p=0.001, r=0.59, power=0.85) |
| **사무용 의자** | 큼 (p<0.001) | **−0.4 ± 1.1°** (유지 좋음, p=0.033) |
| 스툴 | — | −3.2 ± 7.1° |
| 키보드 / 마우스 / 필기 | **키보드 최대** (p<0.001) | −1.2 / −1.8 / −2.9° (p=0.067, 유의하지 않음) |

**곧게 앉으라고 지시하면 전만 크기는 커지지만 유지는 오히려 나빠진다. 3분만에 나타나는 결과다.**

> **본 연구의 30분 설계는 이 붕괴 과정을 시간축으로 관찰하는 것이 된다.** Kim은 3분 단일 값이지만 본 연구는 궤적을 볼 수 있다.

---

## 2. 그 밖의 선행연구 변인

| 문헌 | 변인 |
| --- | --- |
| **Alshehri et al. (2025)** | 시상면 요추각 평균 / **GMM 기반 자세 모드**(1순위·2순위 빈발 자세, 근접 자세) / 좌석 RMS 속도·변위 / **요추 협응(coherence)** — L5/S1과 T12/L1 신호 간 상관을 0-0.5Hz 및 0.5-1Hz 대역에서 산출 |
| **Claus et al. (2016)** | 흉요추각, 요추각, **전역 정렬 = T1-S2 시상면 거리(mm)** |
| **Chen & Zhang (2025)** | 조건당 5회 측정의 평균값과 **범위(range = max−min)** — 자세 변동성 지표 |
| **Jia & Nussbaum (2018)** | 체간 굴곡각의 **평균과 표준편차**를 첫 5분·마지막 5분에서 산출 |
| **Baker et al. (2018)** | 요부 각도(시상면 T12-S2), 골반 움직임(S2 횡단면 변위 cm) |
| **Paloschi et al. (2021)** | 전만각·후만각, 분절 ROM, **요추-골반 기여율 41.8±8.6%** |

---

## 3. 본 연구 변인 체계(안)

### 3.1 일차 결과변인

| 변인 | 정의 | 근거 |
| --- | --- | --- |
| **LLA_avg** | 사다리꼴 적분한 Sum_LLA ÷ 세션 시간 | Kim et al. (2024) |
| **LLA_dev** | (각 시점 LLA − LLA_start)의 적분 ÷ 세션 시간 | Kim et al. (2024) |
| **시간 경과 변화** | 위 두 변인의 시간·집단·시간×집단 효과 | — |

**30분 세션에 맞춘 확장**: Kim은 단일 값이지만, 본 연구는 **5분 블록 6구간별 LLA_avg·LLA_dev**를 함께 산출해 시간적 궤적을 본다. EMG 블록 구간과 시간축을 일치시킨다.

### 3.2 이차 결과변인

| 변인 | 정의 | 미결 |
| --- | --- | --- |
| **누적 요추굴곡량 (AUC of LLA deficit)** | 기준각 대비 요추각 감소량의 시간 적분 | 기준각, 부호, 단위, 결측구간 처리, 자세 재교정 후 계산 방법 `[확인 필요]` |
| **LLA 기울기 (°/min)** | 시간에 대한 선형회귀 기울기 | R² 병행 보고 |
| **Slump 발생 잠재시간 (Time-to-Threshold)** | 요추각이 사전 정의한 역치를 처음 초과한 시점 | **역치와 최소 지속시간** `[확인 필요]` |
| **총·비율 Slump 지속시간** | 역치 초과 상태의 총 시간 및 세션 대비 비율 | 위와 동일 |
| **자발적 자세 재교정 횟수** | 지시 없이 요추각이 붕괴 상태에서 기준각 근처로 복귀한 사건 수 | 복귀 판정 범위 `[확인 필요]` |

### 3.3 탐색 결과변인

- 최대굴곡 도달시간 (Time-to-Peak Flexion)
- **요추각 변동성 (moving SD)** — Chen & Zhang의 range 지표와 대응
- 머리각도, 표준 직립자세-편한 직립자세 간 IMU·EMG 편차
- **요추 협응(coherence)** — Alshehri 방식. 센서가 2개뿐이면 산출 가능
- PCA·군집분석 기반 변화 유형

---

## 4. ⚠ Slump 역치 설정 — 미해결 핵심 쟁점

`outline.md`는 역치를 **"Chen & Zhang (2025)의 MDC값을 참고"**하도록 되어 있다. 다음을 먼저 확인해야 한다.

| 확인 항목 | 현재 상태 |
| --- | --- |
| Chen & Zhang의 측정 장비 | **광학 동작분석(BTS Smart-D140, 100Hz)** — IMU가 아니다 |
| 부착 위치 | **반사마커 5개**(이주·견봉·대전자·슬관절 외측상과·외측복사뼈) — 척추 극돌기가 아니다 |
| 산출 변인 | **체간 각도(TA)** — T12-S2 요추각이 아니다 |
| 측정 시간 | **5초 × 5회** |

> **Chen & Zhang의 MDC를 본 연구의 T12-S2 IMU 요추각 역치로 그대로 쓸 수 없다.** 장비·부착 위치·산출 변인이 모두 다르다.

**대안 근거**

| 후보 | 값 | 출처 | 성격 |
| --- | --- | --- | --- |
| **측정 오차 기반** | **5.6°** | Paloschi et al. (2021) — T12-S1 상대각의 광학식 대비 최대 RMSE | 이 값 미만은 오차와 구분 불가 |
| 실무 임계 | **5°** | Wong et al. (2018) — 5° 이탈 시 피드백을 제공한 실험적 기준 | 임의 기준이나 선행 사용례 |
| 개인 기준 | LLA_start 대비 상대 편차 | Kim et al. (2024) | 개인별 기준각 방식과 정합 |

> **MDC는 측정오차를 초과하는 변화량이지, 임상적·생체역학적으로 의미 있는 붕괴 기준이 아니다.** 둘을 동일하게 취급하지 않는다.

**추가로 정해야 할 것**

1. **최소 지속시간** — 역치를 순간적으로 넘는 것과 지속적으로 넘는 것을 구분해야 한다 (예: 역치 초과가 10초 이상 지속될 때만 slump 사건으로 판정)
2. **이벤트 시작·종료 규칙** — 히스테리시스를 둘지(진입 역치 > 이탈 역치)
3. **사건 미발생 참여자 처리** — 생존분석의 검열(censoring) 규칙

---

## 5. 참고문헌

- Alshehri, M. A., Riddick, R., Besomi, M., van den Hoorn, W., Klyne, D. M., & Hodges, P. W. (2025). *Journal of Clinical Medicine*, 14(21), 7518. https://doi.org/10.3390/jcm14217518 · https://www.mdpi.com/2077-0383/14/21/7518
- Baker, R., et al. (2018). *IJERPH*, 15(8), 1678. https://doi.org/10.3390/ijerph15081678
- Chen, Y.-L., & Zhang, L.-P. (2025). Postural variability in sitting: Comparing comfortable, habitual, and correct strategies across chairs. *Applied Sciences*, 15, 7239. https://doi.org/10.3390/app15137239
- Claus, A. P., Hides, J. A., Moseley, G. L., & Hodges, P. W. (2016). *Applied Ergonomics*, 53(Pt A), 161-168. https://doi.org/10.1016/j.apergo.2015.09.006
- Jia, B., & Nussbaum, M. A. (2018). *Ergonomics*, 61(12), 1671-1684. https://doi.org/10.1080/00140139.2018.1497815
- Kim, J. C., Kim, J.-G., Kim, B. S., Kim, C. K., Choi, M., Lee, J., & Chung, S. G. (2024). *Journal of Clinical Medicine*, 13(9), 2728. https://doi.org/10.3390/jcm13092728 · https://pmc.ncbi.nlm.nih.gov/articles/PMC11084529/
- Paloschi, D., Bravi, M., Schena, E., Miccinilli, S., Morrone, M., Sterzi, S., Saccomandi, P., & Massaroni, C. (2021). *Sensors*, 21(19), 6610. https://doi.org/10.3390/s21196610 · https://www.mdpi.com/1424-8220/21/19/6610
- **Cotter, B. D., Nairn, B. C., & Drake, J. D. M. (2014). Should a standing or seated reference posture be used when normalizing seated spine kinematics? *Journal of Biomechanics*, 47(10), 2371-2377. https://doi.org/10.1016/j.jbiomech.2014.04.023 · https://www.sciencedirect.com/science/article/pii/S0021929014002486**
- Wong, A. Y. L., et al. (2018). *Gait & Posture*. https://doi.org/10.1016/j.gaitpost.2018.10.028

### 확보 필요 문헌

1. **IMU 기반 요추각의 MDC(minimal detectable change) 또는 SEM을 보고한 문헌** — 현재 미확보. Chen & Zhang은 장비·변인이 달라 대체할 수 없다.
   - 구글 검색: https://www.google.com/search?q=%22minimal+detectable+change%22+lumbar+angle+inertial+measurement+unit+sitting
   - 구글 검색: https://www.google.com/search?q=inertial+sensor+lumbar+lordosis+%22standard+error+of+measurement%22+reliability+sitting
   - **없으면 Paloschi의 RMSE 5.6°를 보수적 하한으로 쓰고 그 한계를 제한점에 명시한다.**

---

## 6. 미결 사항

| # | 항목 |
| --- | --- |
| 1 | **Slump 역치 확정** — Chen & Zhang MDC는 사용 불가. Paloschi RMSE 5.6° 또는 Wong 5° 검토 |
| 2 | **역치 초과의 최소 지속시간** 및 이벤트 시작·종료 규칙(히스테리시스) 확정 |
| 3 | 자발적 재교정의 **복귀 판정 범위** 확정 |
| 4 | AUC의 기준각·부호·단위·결측 처리·재교정 후 계산 방법 확정 — **기준각은 Cotter et al. (2014)에 따라 기립 기준을, 시계열 0점은 좌식 시작값(LLA_start)을 쓰고 둘 다 보고한다** |
| 5 | 블록 구간 수 확정 (5분 × 6구간 안) 및 EMG 블록과의 시간축 정합 |
| 6 | 사건 미발생 참여자의 검열 규칙 확정 |
| 7 | IMU 요추각의 MDC/SEM 근거 문헌 탐색 또는 예비실험으로 자체 산출 |
| 8 | PCA·군집분석의 배치(본문 탐색분석 / 부록 / 후속 연구) 결정 |
