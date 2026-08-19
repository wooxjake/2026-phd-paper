# 4-1. IMU 측정 프로토콜 (센서 위치·수집·각도 산출)

출처: `memo3.md` 2장, `memo2.md` 몸통 운동학 절. 작성일 2026-08-19.

---

## 1. 센서 위치와 각도 정의 — 선행연구 대조

| 문헌 | 장비 | 부착 위치 | 각도 정의 | 샘플링 |
| --- | --- | --- | --- | --- |
| **Kim et al. (2024)** ★ | IMU 2개, **MTw Awinda (Xsens)**, AHRS + Xsens Kalman Filter, Strap-Down Integration | **T12 극돌기**(제12늑골 따라 촉진) · **S2**(양측 후상장골극 중점). **의료용 테이프** 고정 | **단순 차감법.** 두 센서의 X(장축)·Y(내외측축)·Z(전후축) 각을 각각 차감. **Y축 값 = LLA**(후만-전만), X축 = 축회전, Z축 = 측굴 | **40Hz** 무선 |
| **Alshehri et al. (2025)** | dorsaVi | **T12/L1 이행부** · **L5/S1 이행부** · 우측 대퇴 전면. 좌석 뒷면에도 1개(불안정 좌식용) | 한 센서 쿼터니언 × 다른 센서 **켤레 쿼터니언** → **ZXY 순서 오일러각** | 실험실 100Hz→20Hz, 실환경 20Hz(자기계 10Hz) |
| **Paloschi et al. (2021)** | MIMU 3개, **MetaMotionR (MBIENTLAB)**, 온보드 센서퓨전 | **T3 · T12 · S1** | **전만각 = T12-S1 각도차**, 후만각 = T3-T12 각도차. **쿼터니언**(짐벌락 회피) | **100Hz**, 제조사 공표 **정확도 <1° RMS** |
| **Wong et al. (2018)** | IMU 2개, **MyoMOTION (Noraxon)**, 정적 정확도 **1°**·동적 **2°** | **T12 · S1 극돌기**, 양면테이프 | 두 IMU 방향에서 상대 요추각 도출 | **100Hz** |
| **Jia & Nussbaum (2018)** | IMU 2개, **MVN (Xsens)** | **T10 · S1** 등쪽. 두 IMU의 **Y축을 상방으로 정렬** | 체간 분절-골반 **상대각**(Xsens 소프트웨어). 시상면 외 움직임은 무시 가능으로 가정 | 100Hz → **4Hz 4차 Butterworth 양방향** 저역통과 |
| **Baker et al. (2018)** | **3 Space Fastrak (Polhemus) — 전자기식, IMU 아님** | **T12 · L1 · S2** 극돌기 | **시상면상 T12-S2 사이 각** | **25Hz, 10초 표본** |
| **Koca & Koca (2025)** | IMU | **C1 · C7 · T5 · T12 · L5** | 직립 자세와 이완 자세의 각 변화량 | — |
| **Tanthuwapathom et al. (2025)** | SMART IMU | 목·체간 | RULA 점수 자동 산출 | — |

**본 연구는 T12-S2다. 정확히 같은 조합을 쓴 것은 Kim et al. (2024) 하나뿐이다.** Baker도 T12-S2지만 전자기식이다.

---

## 2. 부호 규약 — 문헌마다 반대다

| 문헌 | 양수(+) | 음수(−) |
| --- | --- | --- |
| **Kim et al. (2024)** | **전만(lordotic)** | 후만(kyphotic) |
| **Claus et al. (2016)** | **후만**(kyphotic surface curve) | 전만(lordotic). 0 = 평평 |
| **Alshehri et al. (2025)** | 기립 대비 **굴곡** | 기립 대비 신전 |
| **Baker et al. (2018)** | — | 전만 (기준선 −5.9°, 120분 −0.5°) |

> **본문에 수치를 인용할 때 반드시 부호 규약을 확인해야 한다.** 같은 "−5°"가 문헌에 따라 전만 5°일 수도, 신전 5°일 수도 있다. 본 연구는 규약을 **연구방법에 명시**하고 전 문서에서 일관되게 유지한다. **Kim의 프로토콜을 준용하므로 Kim의 규약(양수=전만)을 채택할 것을 권고한다.**

---

## 3. 기준각(0°) 설정 — 4가지 계열

| 방식 | 문헌 | 절차 |
| --- | --- | --- |
| **A. 센서 병렬 캘리브레이션** | **Kim et al. (2024)** | 부착 전 두 센서를 **실험실 구석에 나란히 놓고** 세 출력각을 0으로 초기화. **차감값이 0에 근접함을 확인**한 뒤 부착. 이후 변화는 **좌식 시작값(LLA_start)** 기준 |
| **B. 기립 자세 기준** | Wong (2018) | 기립 자세에서 **이주(귓불)를 견봉쇄골관절에 정렬**, **양발 어깨너비**. 이어 체간 최대 굴곡·신전 2회로 총 ROM 평균 산출 |
| | Alshehri (2025) | 실험실·실환경 **각각의 모든 기립 구간 요추각의 중앙값을 0°** |
| | Claus (2016) | 기립을 별도 조건으로 측정해 비교 |
| **C. 개인별 ROM 백분율** | Wong (2018) | 좌식 굴곡각을 **최대 굴곡각 대비 백분율**로 표현 |
| | O'Sullivan (2012) | 좌위에서 최대 전방골반경사·최대 전만 = **0%**, 최대 후방경사·완전 굴곡 = **100%**. 5회 반복 캘리브레이션 |
| **D. 기준 착석 자세** | Makhsous (2009) | 특정 착석 자세(Normal)를 기준으로 정규화 |

Wong은 **B와 C를 함께** 쓴다.

### ✅ 이 쟁점은 해결되었다 — Cotter, Nairn, & Drake (2014)

2026-08-19에 원문을 확보하여 검토하였다(`references/entries/40-cotter-nairn-drake-2014.md`).

**연구 개요**: 남성 13명, Vicon MX 카메라 7대 50Hz, 강체판 8개(T1·T4·T5·T8·T9·T12·L1·PSIS)로 척추를 4분절(상부흉추 T1-T4 / 중부흉추 T5-T8 / 하부흉추 T9-T12 / **요추 L1-PSIS**)로 나누고, 좌위 자세의 ROM을 **최대 기립 ROM 대비(%STAND)**와 **최대 착석 ROM 대비(%SIT)**로 각각 정규화해 2×6 반복측정 ANOVA로 비교하였다.

**결론**

| 각도 유형 | 권고 기준자세 |
| --- | --- |
| **전역각(global)** — 모든 분절·모든 평면 | **기립** |
| **상대각 굴곡** — 상부흉추 · 하부흉추 · **요추** | **기립** |
| **상대각 굴곡** — 중부흉추(T5-T8) | **착석** (유일한 예외) |
| **상대각 측굴·회전** — 모든 분절 | **기립** |

> 저자 권고 원문 요지: **"이상적으로는 착석과 기립 기준자세를 모두 수집해 분절별로 더 큰 각도를 채택한다. 하나만 수집해야 한다면 기립 기준자세로 충분하며, 다만 중부흉추 상대 굴곡각 해석에는 주의한다."**

**본 연구에 대한 함의**

1. **기립 기준자세를 채택한다.** 본 연구의 T12-S2는 Cotter의 요추 분절(L1-PSIS)에 가장 가깝고, 이 분절의 상대 굴곡각은 기립 기준이 권고된다. 예외로 지목된 중부흉추(T5-T8)는 **본 연구의 측정 범위 밖**이다.
2. **착석 기준값도 함께 수집한다.** 저자가 제시한 이상적 절차와 일치하며, 현재 계획(표준 직립자세 + 좌식 시작값 모두 기록)을 유지하면 된다.
3. **⚠ 두 문제를 혼동하지 말 것.** Cotter가 답한 것은 **분모(최대 ROM)를 어느 자세에서 얻는가**이지, 시계열 각도의 **기준 오프셋(0°)을 어디에 두는가**가 아니다. Cotter 자신은 0점을 **착석용·기립용으로 각각 따로** 잡았다 — 각 시행의 **첫 1초 자료를 평균**해 참여자·분절별로 산출했고, 그 결과 0°(=0%Max)가 각 자세의 직립과 동등해진다.
   - 본 연구가 **%ROM 방식**(Wong·O'Sullivan 계열)을 쓴다면 → 분모는 **기립 최대 ROM**
   - 본 연구가 **절대 각도 편차 방식**(Kim의 LLA_dev 계열)을 쓴다면 → 0점은 **좌식 시작값(LLA_start)**이 자연스럽고, 기립 값은 별도 기술통계로 보고
   - **두 방식을 모두 산출해 함께 보고하는 것이 가장 안전하다.**

---

## 4. 본 연구 프로토콜(안)

### 4.1 센서 부착

| 항목 | 내용 | 근거 |
| --- | --- | --- |
| 센서 수 | **2개** (요추각) + 선택 1개(머리각) | Kim, Wong |
| 위치 | **T12 극돌기** — 제12늑골을 따라 촉진해 결정<br>**S2** — 양측 후상장골극의 중점 | Kim et al. (2024) |
| 고정 | **의료용 테이프** | Kim |
| 촉진 | 해부학적 지표를 **촉진으로 결정**하고, 가능하면 2인이 교차 검증 | Kim(촉진), Chen & Zhang(2인 교차 검증) |

**머리각 IMU는 부착 위치를 확정해야 한다.** `outline.md`는 "이마 또는 C7"로 되어 있으나 **이 둘은 서로 다른 해부학적 분절**이므로 같은 변수로 대체할 수 없다. Koca & Koca (2025)는 C1·C7을 별개 센서로 두었다. 부착 위치·기준 분절·상대각 계산식·축·부호를 하나의 프로토콜로 확정해야 한다 `[확인 필요]`.

### 4.2 캘리브레이션 (Kim 방식 채택)

```
1. 부착 전, 두 센서를 실험실 코너에 나란히(병렬) 배치
2. 세 출력각(X·Y·Z)을 0으로 초기화
3. 두 센서의 차감값이 0에 근접함을 확인
4. T12·S2에 의료용 테이프로 부착
5. 표준 직립자세 측정 (기립 기준값 확보)
6. 편한 직립자세 측정 (기준자세 간 차이 확인용)
7. 착석 후 표준화된 바른 자세 → 안정화 구간 → LLA_start 산출
```

> **기립 값과 좌식 시작값을 모두 기록한다.** Cotter et al. (2014)이 제시한 이상적 절차와 일치한다. 기립 값은 **Wong 방식**(이주-견봉쇄골관절 정렬, 양발 어깨너비)으로 표준화하고, **Cotter 방식으로 각 시행 첫 1초를 평균**해 참여자·분절별 직립 0점을 산출한다. %ROM 정규화를 쓸 경우 분모는 **기립 최대 ROM**을 채택한다.

### 4.3 수집 파라미터

| 항목 | 값 | 근거 |
| --- | --- | --- |
| 샘플링레이트 | **40Hz** 이상 | Kim 40Hz, Alshehri 20Hz(실환경)로도 충분하다고 정당화 |
| 저역통과 | **4Hz 4차 Butterworth 양방향(무위상)** | Jia & Nussbaum (2018) |
| 동기화 | **EMG RMS를 IMU 레이트에 맞춰 다운샘플** | Jia — 100Hz로 맞춰 시간축 정렬 |

### 4.4 각도 산출 — 단순 차감 + 시상면 외 움직임 병행 기록

**Kim의 단순 차감법을 채택하되, 그 가정을 자료로 검증한다.**

Kim은 "검사 조건에서 센서가 주로 시상면 내에서 움직일 것으로 예상되므로" 3차원 오일러각 대신 단순 차감을 썼다. 본 연구는 **외부 피드백 없이 자발적 자세 변화를 관찰**하므로 축회전·측굴이 섞일 가능성이 Kim(3분 정적 유지)보다 크다.

| 선택지 | 내용 | 평가 |
| --- | --- | --- |
| **A (권고)** | 단순 차감을 쓰되 **X축(축회전)·Z축(측굴) 값을 함께 기록**해 시상면 외 움직임이 작음을 자료로 보인다 | Kim과의 직접 비교가 가능하고, 가정이 검증된 것이 된다 |
| B | Alshehri 방식(쿼터니언 곱 → ZXY 오일러각)으로 처음부터 3차원 처리 | 정확하지만 Kim과 수치 비교가 어려워진다 |

### 4.5 측정 타당도와 해석 한계

| 근거 | 내용 |
| --- | --- |
| **Paloschi et al. (2021)** | **T12-S1 상대각 전만각의 광학식 대비 최대 RMSE 5.6°.** 본 연구가 유의미하다고 주장할 수 있는 **각도 변화량의 하한선**이다. **5.6° 미만의 변화는 측정 오차와 구분되지 않는다고 보수적으로 해석한다.** 단 검증 과제가 전방 굴곡·기립착석이라는 **동적 과제**이므로 정적 좌식의 정확도를 그대로 보장하지 않는다 |
| **Wong et al. (2018)** | MyoMOTION의 제조사 공표 정적 정확도 1°, 동적 2° |
| **Kim et al. (2024)** | 방사선영상의 Cobb angle(T12 하종판-S1 상종판)과 **원리가 다르다.** IMU 측정치를 해부학적 LLA와 동일시하지 않는다 |

> **본 연구는 「IMU 기반 요추각」으로 표기하고 방사선 요추전만각과 구분한다** (`introduce.md` 4절 용어의 정의와 일치).

---

## 5. 참고문헌

- Alshehri, M. A., Riddick, R., Besomi, M., van den Hoorn, W., Klyne, D. M., & Hodges, P. W. (2025). Exploring lumbar spine posture and movement in sitting: A comparison between laboratory and real-world measures. *Journal of Clinical Medicine*, 14(21), 7518. https://doi.org/10.3390/jcm14217518 · HTML 전문 https://www.mdpi.com/2077-0383/14/21/7518
- Baker, R., et al. (2018). *IJERPH*, 15(8), 1678. https://doi.org/10.3390/ijerph15081678
- Chen, Y.-L., & Zhang, L.-P. (2025). Postural variability in sitting: Comparing comfortable, habitual, and correct strategies across chairs. *Applied Sciences*, 15, 7239. https://doi.org/10.3390/app15137239
- Claus, A. P., Hides, J. A., Moseley, G. L., & Hodges, P. W. (2016). *Applied Ergonomics*, 53(Pt A), 161-168. https://doi.org/10.1016/j.apergo.2015.09.006
- **Cotter, B. D., Nairn, B. C., & Drake, J. D. M. (2014). Should a standing or seated reference posture be used when normalizing seated spine kinematics? *Journal of Biomechanics*, 47(10), 2371-2377. https://doi.org/10.1016/j.jbiomech.2014.04.023 · https://www.sciencedirect.com/science/article/pii/S0021929014002486 · 초록 https://pubmed.ncbi.nlm.nih.gov/24856889/**
- Jia, B., & Nussbaum, M. A. (2018). *Ergonomics*, 61(12), 1671-1684. https://doi.org/10.1080/00140139.2018.1497815
- Kim, J. C., Kim, J.-G., Kim, B. S., Kim, C. K., Choi, M., Lee, J., & Chung, S. G. (2024). Assessing the preservation of lumbar lordotic curvature in everyday sitting conditions assessed with an inertial measurement system. *Journal of Clinical Medicine*, 13(9), 2728. https://doi.org/10.3390/jcm13092728 · PMC 전문 https://pmc.ncbi.nlm.nih.gov/articles/PMC11084529/
- Koca, R., & Koca, Y. B. (2025). Anatomy-based assessment of spinal posture using IMU sensors and machine learning. *Sensors*, 25(19), 5963. https://doi.org/10.3390/s25195963
- Makhsous, M., et al. (2009). *BMC Musculoskeletal Disorders*, 10, 17. https://doi.org/10.1186/1471-2474-10-17
- O'Sullivan, K., et al. (2012). *Manual Therapy*, 17(6), 566-571. https://doi.org/10.1016/j.math.2012.05.016
- Paloschi, D., Bravi, M., Schena, E., Miccinilli, S., Morrone, M., Sterzi, S., Saccomandi, P., & Massaroni, C. (2021). Validation and assessment of a posture measurement system with magneto-inertial measurement units. *Sensors*, 21(19), 6610. https://doi.org/10.3390/s21196610 · HTML 전문 https://www.mdpi.com/1424-8220/21/19/6610
- Tanthuwapathom, R., Manupibul, U., Jarumethitanont, W., Limroongreungrat, W., Ongwattanakul, S., & Charoensuk, W. (2025). Reliability of sitting posture between physical therapist video-based evaluation and SMART IMU system using rapid upper limb assessment (RULA). *Scientific Reports*, 15, 1441. https://doi.org/10.1038/s41598-025-85159-z
- Wong, A. Y. L., et al. (2018). *Gait & Posture*. https://doi.org/10.1016/j.gaitpost.2018.10.028

### 확보 필요 문헌

1. **Riddick, R., Smits, E., Faber, G., Shearwin, C., Hodges, P., & van den Hoorn, W. (2023). Estimation of human spine orientation with inertial measurement units (IMU) at low sampling rate: How low can we go? *Journal of Biomechanics*, 157, 111726.**
   - PubMed 검색: https://pubmed.ncbi.nlm.nih.gov/?term=Estimation+of+human+spine+orientation+with+inertial+measurement+units+at+low+sampling+rate
   - 구글 검색: https://www.google.com/search?q=%22Estimation+of+human+spine+orientation+with+inertial+measurement+units%22+%22How+low+can+we+go%22
   - Alshehri의 참고문헌 28번. **IMU 척추 방향 추정의 샘플링레이트 하한을 직접 검증한 문헌.** 본 연구의 40Hz 선택 근거.

2. **Madgwick, S. O. H., Harrison, A. J. L., & Vaidyanathan, R. (2011). Estimation of IMU and MARG orientation using a gradient descent algorithm. *IEEE International Conference on Rehabilitation Robotics*.**
   - 구글 검색: https://www.google.com/search?q=%22Estimation+of+IMU+and+MARG+orientation+using+a+gradient+descent+algorithm%22
   - Alshehri가 방향 추정에 쓴 Gradient Descent Filter의 원출처. **선택지 B(쿼터니언 처리)를 택할 경우 필요.**

---

## 6. 미결 사항

| # | 항목 |
| --- | --- |
| 1 | ~~Cotter et al. (2014) 확보 후 기준각 확정~~ → **2026-08-19 해결. 기립 기준 채택, 착석 기준도 병행 수집.** 남은 결정은 %ROM 방식과 절대 편차 방식 중 무엇을 일차로 보고할지 |
| 2 | 부호 규약 확정(Kim 방식 = 양수 전만 권고) 후 전 문서 통일 |
| 3 | 단순 차감(A) vs 쿼터니언(B) 확정 — A 권고, X·Z축 병행 기록 |
| 4 | 머리각 IMU의 부착 위치·기준 분절·계산식 확정 (이마 vs C7) |
| 5 | 장비 확정 및 실제 샘플링레이트·정확도 사양 확인 |
| 6 | 기준각 산출구간의 길이와 대표값(평균 vs 중앙값) 확정 |
| 7 | 촉진 위치의 검사자 간 신뢰도 확보 절차(2인 교차 검증 여부) |
| 8 | EMG-IMU 동기화 장비·프로토콜 확정 |
