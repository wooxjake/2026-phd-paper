# 3-2. EMG 정규화 — 좌식 시작 구간 대비 정규화 (MVC·RVC 배제)

출처: `memo3.md` 1장, `memo2.md` 「표준화와 정규화」 절. 작성일 2026-08-19.

---

## 1. 용어 정리

| 약어 | 원어 | 뜻 |
| --- | --- | --- |
| **MVC / MVIC** | maximal voluntary (isometric) contraction | 최대수의(등척성)수축 |
| **RVC** | reference voluntary contraction | 기준수의수축 — 최대가 아닌 **표준화된 하위최대 과제** |

정규화는 피험자 간·전극 부착 간 신호 크기 차이를 제거하는 절차다. 표면 EMG 원신호 진폭(mV)은 피하지방 두께, 전극 위치, 피부 임피던스에 좌우되므로 정규화 없이는 개인 간 비교가 성립하지 않는다.

---

## 2. 선행연구의 정규화 방식 대조

| 문헌 | 진폭(RMS) 정규화 | 주파수(MDF/MPF) 정규화 |
| --- | --- | --- |
| **Baker et al. (2018)** | **하위최대 RVC** 대비 % | 정규화 안 함(원값 Hz) |
| Wong et al. (2018) | %MVC | — |
| Waongenngarm et al. (2015a) | %MVC | — |
| Waongenngarm et al. (2015b) | 진폭 미사용 | 정규화 안 함(원값 시계열) |
| Jung et al. (2021) | 진폭 미사용 | **초기값(첫 5분) 대비** |
| **Areeudomwong et al. (2012)** | 진폭 미사용 | **안정시(rest) 초기 MF 대비** → NMF 기울기 |
| Jia & Nussbaum (2018) | %MVC (과제 전 안정시 + MVC 보정 절차) | **초기값 대비** |
| Saiklang et al. (2022) | 진폭 미사용 | 정규화 안 함 |
| O'Sullivan et al. (2012) | %MVIC | — |
| **Lopez et al. (2024)** | **MVIC 포기** → 전 시행 EMG 최댓값 평균 대비 | — |
| **Makhsous et al. (2009)** | **Normal 착석 자세 대비** | — |
| Zawadka et al. (2023) | 정규화 대신 **비율 지표**(FRR/ERR) | — |

**세 가지 관찰**

1. **MVC 정규화는 과반이 아니다.** 12편 중 4편만 %MVC/%MVIC를 사용했다.
2. **좌식 연구 3편이 각기 다른 이유로 MVC를 회피했다.** Baker는 하위최대 RVC, Lopez는 통증군 때문에 시행 최댓값, Makhsous는 기준 착석 자세.
3. **주파수 지표에 MVC 정규화를 쓴 문헌은 하나도 없다.** 전부 초기값 또는 안정시 대비로 정규화하거나 정규화하지 않았다.

---

## 3. 본 연구에서 MVC를 쓰기 어려운 이유

### (1) 해상도 문제

Jia & Nussbaum (2018)은 40분 무지지 좌식에서 근활성이 **대부분 MVC의 10% 미만**이었다고 보고했다. 값이 한 자릿수 %에 몰리면 조건 간·시간 경과 간 차이가 측정 노이즈에 묻힌다.

### (2) MVC 시행 자체가 피로를 유발한다

본 연구는 30분 좌식 중 피로·자세 변화를 본다. 세션 직전에 여러 근육에 대해 최대 등척성 수축을 3회씩 수행하면 **기저 상태가 이미 오염된다.** Jia는 이월효과를 막기 위해 세션 간 최소 4일의 간격을 두었다.

### (3) 집단 비교에서 편향이 발생한다 — 본 연구에 가장 치명적

본 연구는 **규칙적 운동군과 비운동군**을 비교한다. 운동군은 더 큰 MVC를 낼 가능성이 높다.

> 동일한 절대 근활성 → 운동군에서 **더 작은 %MVC**로 환산

즉 실제 좌식 중 근활성에 차이가 없어도 정규화 과정에서 **인위적인 집단 차이**가 만들어진다. 반대로 실제 차이가 있어도 상쇄되어 사라질 수 있다. **MVC 정규화는 근력이 다른 두 집단을 비교하는 설계와 구조적으로 충돌한다.**

### (4) 노력 의존성

MVC는 참여자의 동기와 통증 회피에 좌우된다. Lopez et al. (2024)은 표본의 절반이 목통증군이라는 이유로 **MVIC 시행이 부적절하다고 판단하고 포기**했다.

---

## 4. 「선 자세를 RVC 기준으로」 방침 검토 — 근거 문헌 없음

`outline.md` III-4의 현재 계획은 **"진폭 트랙: RMS, 표준 직립자세 기준 RVC(%RVC)"**다. 수집 문헌 전수 검색 결과는 다음과 같다.

### (a) EMG 정규화 기준으로 선 자세를 쓴 문헌: **0편**

표면 EMG 진폭을 **기립 자세의 근활성으로 정규화한 문헌은 확인되지 않았다.** 방법론적 이유가 있다.

> 조용한 기립에서 요추기립근 활성은 좌식과 마찬가지로 매우 낮다. **기준값 자체가 노이즈 수준**이므로 분모가 작아지고, 정규화된 값의 분산이 폭발한다.

**따라서 「표준 직립자세 기준 RVC」 방침은 근거 문헌이 없으며 권장하지 않는다.** 표준 직립자세는 **IMU 요추각의 기준각 산출용으로만** 사용하고, EMG 정규화는 별도의 부하가 있는 RVC 과제로 수행한다.

### (b) 선 자세를 **각도** 기준으로 쓴 문헌: 3편 — 이쪽은 근거가 있다

| 문헌 | 기립 기준 정의 |
| --- | --- |
| Wong et al. (2018) | 이주(귓불)를 견봉쇄골관절에 정렬, 양발 어깨너비 |
| Alshehri et al. (2025) | 전 기립 구간 요추각의 **중앙값을 0°** |
| Claus et al. (2016) | 기립을 별도 조건으로 측정해 비교 |

**Cotter, Nairn, & Drake (2014)가 이 문제를 직접 검증했고, 결론은 기립 기준이다.** 좌위 척추 운동학의 상대 굴곡각을 정규화할 때 **요추 분절은 기립 기준자세**가 권고된다(예외는 중부흉추 T5-T8뿐으로 본 연구 범위 밖). → 상세는 `method/4. IMU - LLA/4-1_IMU_측정_프로토콜.md` 3절 참조.

> **따라서 "표준 직립자세"는 폐기하지 않는다.** 다만 그 용도는 **IMU 요추각의 기준자세**이지 **EMG 진폭의 정규화 기준**이 아니다. 두 용도를 분리해야 한다.

---

## 5. 본 연구 프로토콜(안)

### 5.1 최종 결정 — MVC·RVC를 모두 배제하고 좌식 시작 구간 대비로 통일

**2026-08-26 확정.** RVC 과제(Baker의 복와위 무릎거상)는 채택하지 않는다. **진폭·주파수 모두 좌식 시작 구간(세션 초반)의 값 대비 정규화로 통일한다.**

| 지표 | 정규화 기준 | 근거 |
| --- | --- | --- |
| **진폭(RMS)** | 좌식 시작 구간 값 대비 % | 직접 문헌 선례는 없음(5.2절 참조) — 본 연구의 통계 설계가 절대비교 대신 개인 내 상대변화만 요구하므로 채택 |
| **주파수(MDF)** | 좌식 시작 구간 값 대비 % | Jung(2021)·Jia(2018) 선례 |

두 지표가 같은 기준창을 쓰므로 `3-3` 3.4절(JASA) 해석에도 일관되게 적용된다.

### 5.2 진폭에 이 방식을 쓰는 근거와 한계

**⚠ 정직하게 밝혀둔다 — 진폭을 좌식 시작 구간 대비로 정규화한 문헌 선례는 수집 문헌 안에 없다.** 2절 표의 12편 중 진폭 정규화는 전부 %MVC 계열(Wong, Waongenngarm a, Jia, O'Sullivan)이거나 RVC(Baker), 착석기준(Makhsous), 시행 최댓값(Lopez)이었다. "좌식 시작 구간 대비"는 주파수 쪽 선례(Jung·Jia)를 진폭에 유추 적용한 것이며, 이 점을 논문에도 명시해야 한다.

**그럼에도 채택하는 이유**

1. **본 연구의 주분석은 절대비교가 필요 없다.** `6-1_통계분석_설계.md`의 LMM은 시간×집단 상호작용(변화 양상의 차이)을 본다. 참여자별 무작위 절편이 개인 간 기저 차이를 흡수하므로, "이 사람이 얼마나 힘을 냈나"가 아니라 "이 사람 자신의 시작점 대비 얼마나 변했나"만 있으면 분석이 성립한다.
2. **MVC·RVC 둘 다 이미 기각되었다.** MVC는 집단 간 근력 차이로 인한 구조적 편향(3절), RVC는 근거 문헌은 있었으나(Baker) 본 연구에서 채택하지 않기로 결정했다.
3. **본 연구의 실제 목적(굴곡-이완 현상 추적)에는 상대변화만 필요하다.** 자세가 무너지는 시점에 근활성이 급격히 낮아지는지를 IMU와 동기화해 보는 것이 목적이므로(`3-1` 5절 동기화 항목 참조), 참여자 간 절대크기 비교가 애초에 필요하지 않다.

**남는 위험** — 좌식 시작 구간도 활성이 낮으면 분모가 불안정해질 수 있다(기립·안정시만큼 심각하지는 않지만). `3-3` 3.3절의 최소 활성 기준을 기준창 자체에도 적용해 사전 검증해야 한다.

### 5.3 주파수 — 좌식 시작 구간으로 확정

| 방식 | 문헌 | 정의 |
| --- | --- | --- |
| 기각 | Areeudomwong et al. (2012) | 안정시(rest) 초기 MF 대비 |
| **채택** | **Jung (2021), Jia (2018)** | **좌식 시작 구간(세션 초반)의 값**을 초기값으로 사용 |

기준각 산출과 시간축이 맞아 일관성이 좋다는 것이 채택 이유다. 정확한 구간 길이(첫 5분 등)는 예비측정으로 확정한다 `[확인 필요]`.

### 5.4 MVC 측정 — 정규화 목적에서 완전히 제외, 공변량 용도만 검토

정규화 방법에서는 MVC를 완전히 제외한다. 다만 집단 특성 기술(운동군의 체간 근력이 실제로 더 큰지)을 위해 세션 종료 후 측정해 공변량으로 쓰는 방안은 별개로 남아있다 — **측정 여부 자체는 7절 미결 사항 참조.**

```
[기립] 표준 직립자세 (IMU 기준각) — EMG 정규화 용도 아님
   ↓
[착석] 좌식 시작 구간 → 진폭·주파수 초기값 산출 (정규화 기준)
   ↓
[30분 좌식 세션]
   ↓
[MVC] 세션 후 측정 여부 미결 ← 정규화 아님, 집단 특성 기술용 공변량 검토 중
```

---

## 6. 참고문헌

- Areeudomwong, P., Puntumetakul, R., Kaber, D. B., Wanpen, S., Leelayuwat, N., & Chatchawan, U. (2012). Effects of handicraft sitting postures on lower trunk muscle fatigue. *Ergonomics*, 55(6), 693-703. https://www.researchgate.net/publication/223135407_Effects_of_handicraft_sitting_postures_on_lower_trunk_muscle_fatigue
- Baker, R., Coenen, P., Howie, E., Williamson, A., & Straker, L. (2018). *IJERPH*, 15(8), 1678. https://doi.org/10.3390/ijerph15081678 · https://www.mdpi.com/1660-4601/15/8/1678
- Claus, A. P., Hides, J. A., Moseley, G. L., & Hodges, P. W. (2016). *Applied Ergonomics*, 53(Pt A), 161-168. https://doi.org/10.1016/j.apergo.2015.09.006
- Cotter, B. D., Nairn, B. C., & Drake, J. D. M. (2014). Should a standing or seated reference posture be used when normalizing seated spine kinematics? *Journal of Biomechanics*, 47(10), 2371-2377. https://doi.org/10.1016/j.jbiomech.2014.04.023
- Jia, B., & Nussbaum, M. A. (2018). *Ergonomics*, 61(12), 1671-1684. https://doi.org/10.1080/00140139.2018.1497815
- Jung, K.-S., et al. (2021). *Medicina*, 57(1), 3. https://doi.org/10.3390/medicina57010003
- Lopez, E. J., et al. (2024). *International Journal of Exercise Science*, 17(1), 1280-1293. https://pmc.ncbi.nlm.nih.gov/articles/PMC11728583/
- Makhsous, M., et al. (2009). *BMC Musculoskeletal Disorders*, 10, 17. https://doi.org/10.1186/1471-2474-10-17
- O'Sullivan, K., et al. (2012). *Manual Therapy*, 17(6), 566-571. https://doi.org/10.1016/j.math.2012.05.016
- Saiklang, P., Puntumetakul, R., & Chatprem, T. (2022). *IJERPH*, 19(3), 1904. https://doi.org/10.3390/ijerph19031904
- Waongenngarm, P., et al. (2015a). *Journal of Physical Therapy Science*, 27(7), 2183-2187. https://doi.org/10.1589/jpts.27.2183
- Waongenngarm, P., et al. (2015b). *Safety and Health at Work*, 7(1), 49-54. https://doi.org/10.1016/j.shaw.2015.08.001
- Wong, A. Y. L., et al. (2018). *Gait & Posture*. https://doi.org/10.1016/j.gaitpost.2018.10.028
- Zawadka, M., et al. (2023). *Ergonomics*, 66(1), 101-112. https://doi.org/10.1080/00140139.2022.2061051

### 확보 필요 문헌 (정규화 방법론)

1. **Dankaerts, W., O'Sullivan, P. B., Burnett, A. F., Straker, L. M., & Danneels, L. A. (2004). Reliability of EMG measurements for trunk muscles during maximal and sub-maximal voluntary isometric contractions in healthy controls and CLBP patients. *Journal of Electromyography and Kinesiology*, 14(3), 333-342.**
   - PubMed 검색: https://pubmed.ncbi.nlm.nih.gov/?term=Reliability+of+EMG+measurements+for+trunk+muscles+during+maximal+and+sub-maximal+voluntary+isometric+contractions
   - 구글 검색: https://www.google.com/search?q=%22Reliability+of+EMG+measurements+for+trunk+muscles+during+maximal+and+sub-maximal+voluntary+isometric+contractions%22
   - **체간근에서 하위최대 정규화가 최대 정규화보다 신뢰로운지를 직접 검증한 문헌. RVC 채택의 핵심 근거이므로 최우선 확보.**

2. **Burden, A. (2010). How should we normalize electromyograms obtained from healthy participants? What we have learned from over 25 years of research. *Journal of Electromyography and Kinesiology*, 20(6), 1023-1035.**
   - 구글 검색: https://www.google.com/search?q=%22How+should+we+normalize+electromyograms+obtained+from+healthy+participants%22+Burden
   - 정규화 방법 선택의 표준 리뷰.

3. **Mathiassen, S. E., Winkel, J., & Hägg, G. M. (1995). Normalization of surface EMG amplitude from the upper trapezius muscle in ergonomic studies - A review. *Journal of Electromyography and Kinesiology*, 5(4), 197-226.**
   - 구글 검색: https://www.google.com/search?q=%22Normalization+of+surface+EMG+amplitude+from+the+upper+trapezius+muscle+in+ergonomic+studies%22
   - RVC 개념의 원출처로 널리 인용된다.

---

## 7. 미결 사항

**확정된 항목** — 진폭·주파수 모두 좌식 시작 구간 대비 정규화(5.1-5.3절). MVC·RVC는 정규화 방법에서 완전히 배제. `outline.md`의 관련 문구도 갱신 완료.

| # | 항목 |
| --- | --- |
| 1 | 좌식 시작 구간의 정확한 길이(첫 5분 등) 예비측정으로 확정 |
| 2 | 좌식 시작 구간 자체가 최소 활성 기준을 통과하는지 사전 검증하는 절차 확정 (`3-3` 3.3절과 연동) |
| 3 | MVC를 세션 후에 측정할지, 아예 생략할지 결정 |
