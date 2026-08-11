# Anatomy-Based Assessment of Spinal Posture Using IMU Sensors and Machine Learning
## IMU 센서와 기계 학습을 이용한 척추 자세의 해부학 기반 평가

## 논문 정보
- Academic Editors: Michael E. Hahn, Seth Donahue
- Received: 30 July 2025
- Revised: 15 September 2025
- Accepted: 17 September 2025
- Published: 25 September 2025
- Citation: Koca, R.; Koca, Y.B. Anatomy-Based Assessment of Spinal Posture Using IMU Sensors and Machine Learning. Sensors 2025, 25, 5963. https://doi.org/10.3390/s25195963
- Correspondence: ybkoca@aku.edu.tr
- Author affiliations:
  - Department of Physical Therapy and Rehabilitation, Faculty of Health Sciences, Afyonkarahisar Health Sciences University, 03030 Afyonkarahisar, Türkiye
  - Department of Electrical Engineering, Faculty of Engineering, Afyon Kocatepe University, 03200 Afyonkarahisar, Türkiye

## Highlights

### 주요 결과는 무엇인가?
- IMU 기반 자세 각도를 사용해 문헌의 기준 범위에 대한 프록시 편차 라벨을 도출했고, 기계 학습 모델은 인구통계학적 및 인체측정학적 변수로 이 라벨을 예측했다.
- 일상적 자세 습관, 특히 장시간의 책상 작업과 스마트폰 사용은 경추 전만, 흉추 후만, 요추 전만의 편차에 유의한 영향을 미쳤다.

### 주요 결과의 의미는 무엇인가?
- IMU 기반 척추 자세 모니터링은 예방적 건강 전략에 대한 후속 연구를 촉진할 수 있지만, 현재 결과는 탐색적이며 검정력이 충분하지 않다.
- 센서 기반 자세 모니터링을 일상생활 및 직업 환경에 통합하는 가능성은 있으나, 아직 검증된 진단 도구는 아니다.

## Abstract

배경: 본 연구에서는 IMU(관성 측정 장치) 기반 자세 각도 추정을 사용하여 프록시 위험 레이블을 정의하고 기계 학습 분석을 통해 인구통계학적, 인체 측정적, 생활 방식 변수로부터 이러한 레이블을 예측할 수 있는지 조사했습니다. 방법: 18~25세의 건강한 개인 30명이 포함되었습니다. 인구통계학적, 인체측정학적 데이터와 일상생활 활동에 대한 정보를 수집했습니다. IMU 센서는 척추 수준 C1, C7, T5, T12 및 L5에 배치되었습니다. 참가자들에게 똑바로 선 자세로 서도록 지시한 후 편안한 일상 자세를 취하도록 했습니다. 이러한 위치 사이의 해부학적 자세 변화를 분석했습니다. RF(Random Forest) 및 ANN(인공 신경망)을 포함한 기계 학습 알고리즘을 사용하여 경추 전만증, 흉추 후만증, 요추 전만증 및 척추측만증 위험을 예측했습니다. 결과: 책상 작업 및 전화 사용 중 잘못된 자세는 경추 전만증, 흉추 후만증 및 요추 전만증과 같은 자세 관련 편차의 가능성 증가와 관련이 있었습니다. 반대로, 매일의 신체 활동은 이러한 편차를 줄였습니다. LOSO 및 불균형 처리 기능이 포함된 계층화된 교차 검증을 사용하면 균형 정확도는 대상 전체에서 0.55~0.82 사이였으며 다수 클래스 기준선은 0.53~0.87이었습니다. 경추 전만증 위험의 경우 RF는 0.82의 균형 정확도(95% CI: 0.74–0.97)를 달성한 반면, 다른 범주는 중간이지만 일관된 성능을 보였습니다. AUPRC 값은 모든 모델에서 기준 수준을 초과했습니다. 결론: IMU 기반 자세 각도 추정은 자세 관련 위험 범주를 식별하는 데 사용될 수 있습니다. 이 연구에서 ML 모델은 인구통계학적, 인체측정학적, 라이프스타일 변수와의 예측 관계를 보여주었습니다. 이러한 발견

<!-- Page 2 -->

건강한 젊은 성인으로 구성된 소규모 집단에서 IMU 유래 프록시 라벨을 기반으로 탐색적 증거를 제공합니다. 이는 임상 결과보다는 자세 이탈에 대한 탐색적 지표를 나타내며 예방 전략에 대한 향후 연구에 동기를 부여할 수 있습니다. 중요한 점은 결과가 선험적 권력 목표에 비해 여전히 약하다는 점이며 질적으로 해석되어야 한다는 것입니다.

**Keywords:** anatomic posture analysis; IMU sensors; machine learning; cervical lordosis;

흉부 후만증; 요추 전만증; 척추 측만증

## 1. Introduction

해부학적 자세는 중력에 대항하는 개인의 신체 위치를 정의하는 개념입니다. 해부학적 구조와 직접적으로 관련된 자세는 서거나 앉거나 움직이는 등의 활동 중에 정적으로, 동적으로 검사할 수 있습니다[1]. 정적 자세는 정지해 있을 때 관절의 안정성을 제공하는 반면, 동적 자세는 지속적인 적응이 필요한 움직임 상태입니다. 척추는 신체의 기본 골격으로 바른 자세를 제공하고 건강한 자세를 유지하는데 중요한 역할을 합니다. 건강한 자세를 유지하려면 척추, 척추의 기본 구조 단위, 추간판의 충격 흡수 기능, 다양한 근육 그룹의 자세 지지 메커니즘 사이의 관계가 필요합니다. 자세 안정성을 제공하는 근육, 특히 척추 기립근과 복횡근은 척추의 올바른 정렬과 하중 운반 능력을 증가시킵니다[1,2]. 올바른 자세는 근골격계가 올바르게 정렬되고 해부학적 구조에 가해지는 스트레스가 감소되어 생체역학적 효율성이 높아지는 상태입니다. 척추는 올바른 자세로 뒤에서 보면 수직면에 일직선으로 보입니다. 측면만곡이 10도 이상일 경우 척추측만증으로 정의한다[3]. 그러나 특정 해부학적 곡선은 측면에서 볼 때 정상적인 것으로 간주됩니다. 이 곡선은 특정 각도에 있어야 합니다. 경추 부위의 곡률(경추 전만증)은 35~45도 사이이고, 흉부 부위의 곡률(흉부 후만증)은 20~40도 사이이며, 요추 부위의 곡률(요추 전만증)은 40~60도 사이입니다[4-6]. 오늘날의 생활습관은 장시간 앉아 있는 자세, 잘못된 침대 자세, 무거운 물건을 드는 등의 요인으로 인해 척추의 자연스러운 곡선을 무너뜨려 척추 자세 장애를 유발할 수 있습니다[7,8]. 특히, 학생들의 공부나 청취 시 잘못된 앉은 자세, 장시간의 전화 및 컴퓨터 사용은 노년기에 다양한 건강 문제를 일으킬 수 있다[7,9]. 시간이 지남에 따라 이러한 장애는 척추와 근육계에 영향을 미쳐 만성 통증, 신경 압박 및 운동 제한을 유발하여 삶의 질을 저하시킬 수 있습니다[8]. 장기간 잘못된 앉은 자세는 요추 전만증을 증가시키고 허리 통증이나 경추 및 흉추 부위의 통증을 유발할 수 있습니다 [10]. 그러므로 척추자세장애의 조기진단과 치료는 건강문제의 진행을 예방하고 생명을 보존하기 위해 필수적이다. 이러한 방향에서 척추 자세 분석은 많은 자세 문제에 특정한 치료 접근법을 결정하고 입증하는 데 필수적입니다[11]. 척추 자세 분석은 척추 위치를 평가하여 가능한 기형 및 장애를 진단합니다[12]. 불만 사항에 대한 신체 검사는 환자의 안내를 통해 자세 문제를 발견하는 데 도움이 되며 치료 계획을 결정하는 데 필수적입니다. 임상 실습에서 척추 자세는 일반적으로 방사선 영상(예: Cobb 각도), 연조직 평가를 위한 MRI/초음파 검사, 측각기, 사진 측량, 광전자 모션 캡처 시스템과 같은 실험실 기반 도구를 사용하여 평가됩니다.

<!-- Page 3 -->

각각은 반복적인 실제 모니터링에 대한 실질적인 제약이 있습니다[13,14]. 전통적으로 척추 자세는 진료소, 일상적인 환자 검사, 물리치료 세션 또는 실험실 기반 평가를 통해 검사됩니다. 그러나 이러한 전통적인 왜곡은 일상적인 자세 측정 및 시기적절한 피드백과 관련하여 충분하지 않습니다. 방사선학적 평가는 척추 자세를 분석하는 기본 방법이다[15]. 그러나 반복 사용에 따른 비용과 방사선 노출로 인해 선호되지 않는 경우가 많습니다[16]. MRI 및 초음파 촬영과 같은 기술을 사용하여 근육 및 연조직 구조를 자세히 검사하면 자세 장애의 원인을 보다 명확하게 이해할 수 있습니다. 이러한 방법은 연조직의 통합과 근육의 적절한 기능을 결정하는 데 특히 중요합니다[17]. 측각기, 사진 측량 시스템, 광전자 시스템과 같은 다른 실험실 기반 방법은 다양한 제한으로 인해 일상적인 의료 행위에 통합되지 않았습니다 [10,18,19]. 최근 전자 장치의 발전으로 인해 IMU를 사용하여 해부학적 자세 분석을 3D로 기록하는 데 대한 관심이 높아졌습니다. 소프트웨어로 개발된 알고리즘은 IMU 센서의 데이터를 처리하여 사람의 해부학적 자세 분석을 수행할 수 있습니다. 이를 통해 환자의 자세 오류, 자세 이상, 동작 결함을 감지하고 사용자에게 피드백을 제공하여 조기 선별 및 모니터링이 가능하다[20,21]. IMU 센서는 자세 분석을 위한 필수적인 대안이 되었으며, 휴대성, 저렴한 비용, 무방사선 구조 등 기존의 광학 모션 캡처 시스템에 비해 많은 이점을 제공합니다[22,23]. 작은 크기와 사용 용이성으로 인해 IMU는 임상 및 비임상 환경 모두에서 장기 모니터링 및 데이터 수집에 이상적이며 재활 진행 상황과 인간 수행 능력을 쉽게 추적할 수 있습니다[24,25]. 기존 모션 캡처 시스템에 비해 보완적인 옵션을 제공하는 IMU는 X선이나 컴퓨터 단층촬영(CT)과 같은 방사선 관련 방법에 대한 더 안전한 대안이며, 특히 장애나 마비가 있는 경우 반복적으로 사용할 수 있습니다[25,26]. 이러한 센서의 비침습적 특성은 정확하고 간결한 자세 분석을 가능하게 하여 사용자 편의성을 높이고 장기적인 사용 데이터를 제공합니다[25]. 또한 오늘날의 조건과 실험실 환경 외부에서의 유용성은 노인의 야외 분석부터 공장 환경의 인간-기계 움직임에 이르기까지 다양한 응용 분야를 제공합니다 [22,24,27]. 그러나 IMU를 정확하게 사용하려면 환경 전반에 걸쳐 측정 안정성을 보장하기 위해 지속적인 교정과 주의 깊은 센서 정렬과 함께 자기 교란 및 온도 관련 드리프트를 완화해야 합니다[23,26,28,29]. IMU 센서는 휴대성과 저렴한 비용의 장점으로 산업 보건 및 안전 분야에서 직업성 근골격계 질환을 예방하기 위한 실용적인 솔루션을 제공합니다[30].

## RESEARCH GAP, CONTRIBUTION, OBJECTIVES, AND HYPOTHESIS

그 가치에도 불구하고 위의 방법은 대부분 정적이거나 실험실에 국한되어 있으며 일상 활동 중 자세를 쉽게 포착하지 못합니다. 반복적이고 방사선 없는 측정을 가능하게 하는 휴대용, 병원 독립적 모니터링에 대한 필요성이 여전히 남아 있습니다. 우리는 IMU에서 파생된 자세 각도가 문헌 기반 참조 범위를 사용하여 프록시 편차 레이블로 변환되는 건강한 젊은 성인의 타당성 프레임워크를 조사하고 간단하고 쉽게 수집된 변수(인구통계, 인체 측정 및 일일 행동)가 이러한 레이블을 예측할 수 있는지 여부를 조사합니다. 이 연구의 목적은 다음과 같습니다: (i) 경추 전만증, 흉부 후만증 및 요추 전만증에 대한 IMU 기반 프록시 편차 레이블을 도출합니다. (ii) 일상 행동 및 인체 측정과의 연관성을 정량화합니다. (iii) 작은 표본 크기와 클래스 불균형을 해결하면서 이러한 레이블을 예측하는 교차 검증된 기계 학습 모델을 평가합니다. 쉽게 수집된 인구 통계, 인체 측정 및 일일 행동 변수는 IMU에서 파생된 프록시 편차 레이블과 측정 가능한 연관성을 보여주고 이 코호트에서 확률보다 더 나은 교차 검증 분류를 가능하게 합니다.

<!-- Page 4 -->

## 2. Materials and Methods

### 2.1. Study Design and Setting

이 연구는 대학 실험실 환경에서 수행되었습니다. 이는 단일 세션에서 수행된 단면 관찰 연구였습니다. 연구에 대한 윤리적 승인은 Afyonkarahisar Health Sciences University의 과학 연구 윤리 위원회로부터 받았습니다(승인 날짜: 2023년 9월 1일, 승인 번호: 2023/405). 모든 참가자로부터 서면 동의서를 얻었습니다. 18~25세의 총 30명의 건강한 참가자(여성 15명, 남성 15명)가 포함되었습니다. 개인의 인구통계학적 특성, 인체 측정치, 일상 생활 활동은 구조화된 설문지를 통해 수집되었습니다. 사전 전력 분석은 G*Power 3.1을 사용하여 수행되었습니다. Cohen의 h ≒ 0.51, α = 0.05, 검정력 = 0.80을 기반으로 약 30명의 표본 크기가 큰 효과만 탐지하기에 충분한 것으로 추정되었습니다. 각 위험 범주에 대해 기술 기준이 없는 것과 관련된 필수 정확도가 계산되었습니다(표 1). 이는 연구가 큰 효과에 대해서는 적절하게 검정력이 있었지만 작은 효과에 대해서는 검정력이 부족했음을 나타냅니다. 그러나 이 연구에서 얻은 교차 검증 결과(경추 전만증의 경우 최대 0.90)는 표 1에 나열된 선험적 임계값에 도달하지 못했습니다. 따라서 ML 결과는 검증되지 않은 탐색적 결과로 제시되고 질적으로 해석되어야 합니다.

### Table 1 - 전력 분석 대상: 스킬 정확도 없음(p 0) 및 80% 전력에 필요한 정확도(p 1)
- 이미지 재현: [원문 추출 불명확]

결과당. 목표 기술 없음 정확도(p0) 80% 전력에 필요한 정확도(p1) 경추 전만증 0.80 0.96 흉부 후만증 0.53 0.77 요추 전만증 0.87 0.99 척추측만증 0.57 0.80 IMU 센서를 사용하여 해부학적 자세 분석을 수행했습니다. 센서는 참가자 척추의 경추 1(C1), 경추 7(C7), 흉추 5(T5), 흉추 12(T12) 및 요추 5(L5) 수준에 배치되었습니다. 참가자들에게 먼저 똑바로 서서 편안한 자세로 일상 활동을 수행하도록 요청했습니다. 두 상황 사이의 각도 변화를 관찰하여 자세 분석을 수행하였다. 각 참가자는 먼저 약 10초 동안 표준 해부학적 자세로 똑바로 서 있었습니다. 그 후, 서 있거나 앉아 있는 동안 일반적인 일상 자세를 반영하는 편안한 자세로 전환하도록 지시 받았습니다. 자연스러운 동작을 보장하기 위해 이 전환 중에 외부 수정이나 제약이 적용되지 않았습니다. 5개 센서 모두의 각도 데이터는 두 위치 모두에서 지속적으로 기록되었으며 각 기록 단계는 약 20초 동안 지속되었습니다. 준비 및 보정을 포함하여 전체 절차는 참가자당 약 5분이 소요되었습니다. 굴곡, 신전, 좌우 측면 굴곡 및 회전 운동을 검사했습니다. 데이터는 Bluetooth를 통해 무선으로 중앙 장치로 전송되었습니다. 히트맵은 쌍별 연관성의 시각화에만 사용되었습니다. 편차/위험 라벨은 히트맵에서 파생되지 않았습니다. 이는 문헌 기반 참조 범위(경추 전만증 35~45°, 흉부 후만증 20~40°, 요추 전만증 40~60°, 척추 측만증 선별 역치 ±10° 측면 편차)를 사용하여 IMU 기반 각도로부터 선험적으로 정의되었습니다[3-6]. 연구의 흐름도는 그림 1에 나와 있습니다.

<!-- Page 5 -->

### Figure 1 - 자세 분석 및 기계 학습의 주요 단계를 요약한 흐름도입니다.
- 이미지 재현: [원문 추출 불명확]

### 2.2. Participant Criteria and Parameters

참가자는 정해진 기준에 따라 선정되었으며 자발적으로 동의를 얻은 후 인구통계학적, 인체측정학적 데이터를 수집했습니다. 인구통계학적 특성(연령, 키, 체중, BMI), 일일 책상에 앉아 있는 시간, 일일 전화/컴퓨터 사용, 주간 신체 활동 및 일일 서 있는 시간을 구조화된 설문지를 사용하여 기록했습니다. 평균 전화 및 컴퓨터 사용 시간은 주로 참가자의 일반적인 주중 일상을 기반으로 한 자체 보고 추정치를 통해 수집되었습니다. 회상 편향을 최소화하기 위해 참가자들은 스마트폰에서 화면 시간 통계나 사용 추적 애플리케이션을 확인하도록 권장되었습니다. 회상 편향을 줄이기 위해 참가자들에게는 지난 7일 동안의 사용량을 고려하고 일일 평균 사용량을 보고하도록 지시했습니다. 가능한 경우 참가자들은 보다 정확한 평균 전화 사용 시간을 제공하기 위해 화면 시간 통계 또는 스마트폰의 사용량 추적 애플리케이션을 확인하도록 권장되었습니다. 경추 길이, 흉추 길이, 요추 길이, 다리 길이, 발 길이, 보폭, 보폭 등의 인체 측정이 이루어졌습니다. 이러한 측정에 대한 설명은 다음과 같습니다.

- 경추 길이: 경추의 최상부와 최하부 사이의 길이
척추 C1~C7은 선 자세에서 측정되었습니다.

- 흉추 길이 : 흉추 최상부와 최하부 사이의 길이
척추뼈 T1~T12는 선 자세에서 측정되었습니다.

- 요추 길이 : 요추 최상부와 최하부 사이의 길이
척추뼈 L1~L5는 선 자세에서 측정되었습니다.

- 다리 길이: 전상장골극과 내측장골 사이의 거리
Malleolus는 서있는 동안 측정되었습니다.

- 발 길이: 똑바로 선 자세에서 발에 동일한 체중을 실었을 때 발 길이는
앞쪽의 가장 긴 발가락 끝과 뒤쪽의 발뒤꿈치를 그려 측정합니다.

- 보폭: 참가자가 걷는 동안 정지되었으며, 두 사람 사이의 거리는
걸음수를 측정했습니다. 모든 인체측정 측정은 신장 측정용 표준 측정기, 길이 측정용 비신축성 측정 테이프, 분할 측정용 인체측정 캘리퍼를 포함한 표준 인체측정 툴킷을 사용하여 수행되었습니다. 참가자는 다음 기준을 충족하는 경우 연구에 포함되었습니다. 18~25세, 신경학적 또는 근골격계 질환의 병력이 없으며 지난 2년 동안 낙상 관련 부상을 경험하지 않았으며 자발적으로 참여하기로 동의했습니다. 제외 기준에는 진단된 자세 장애, 척추 수술 이력 또는 외상 관련 신체적 제한 또는 모든 상태가 포함되었습니다.

<!-- Page 6 -->

적절한 센서 배치를 방해할 수 있는 것(예: 피부 문제, 열린 상처 또는 척추 부위에 이식된 장치).

### 2.3. Statistical Analysis

데이터 분석에는 SPSS for Windows Version 27 통계 프로그램이 사용되었습니다. 측정을 통해 얻은 변수는 평균±표준편차로 나타내었다. Shapiro-Wilk 테스트를 사용하여 정규성을 평가하고 Levene 테스트를 사용하여 분산의 동질성을 평가했습니다. 분산이 동일하지 않은 경우 Welch의 t-검정이 사용되었습니다. 남성과 여성으로 구분된 그룹 간의 비교에서는 파라메트릭 조건을 만족하는 경우 그룹에 대한 t-test를 적용하고, 충족되지 않는 경우에는 Mann-Whitney U test를 사용하였다. 해부학적 및 행동적 차이가 척추 곡률 및 웨어러블 센서 인체공학에 영향을 미칠 수 있기 때문에 성별 기반 비교가 미리 지정되었습니다. 유의성은 양측 α = 0.05로 평가되었습니다. 효과 크기는 모수 검정의 경우 Cohen의 d로, 비모수 검정의 경우 순위-이중 상관 관계로 계산되었습니다. 작은 표본을 사용한 해석을 돕기 위해 95% 신뢰 구간이 p 값과 함께 보고되었습니다. 카이제곱 검정은 범주형 데이터를 비교하는 데 사용되었습니다.

### 2.4. Sensors and Data Collection

본 연구에서는 척추의 움직임과 자세 분석에 사용하기 위해 9축 IMU 센서가 선호되었습니다. MPU-9250 9축 IMU 센서가 시스템 설계에 사용되었습니다. 저전력 Bluetooth BLE 5.0 데이터 수집 시스템과 통합되었습니다. 이러한 통합을 통해 얻은 데이터를 실시간으로 컴퓨터 환경으로 전송하고 기록했습니다. 센서는 가속도계, 자이로스코프, 자력계의 세 가지 주요 구성 요소로 구성됩니다. 이러한 구성요소는 x, y 및 z축의 변화를 측정할 수 있습니다. 가속도계는 ±2g ~ ±16g의 감도 범위로 선형 움직임을 감지할 수 있는 반면, 자이로스코프는 ±250о/s ~ ±2000о/s 범위의 각속도를 측정할 수 있습니다. 또한 자력계는 지구 자기장을 기준으로 고정된 위치를 추적할 수 있습니다. 원시 데이터 처리 단계에서 Savitzky-Golay 필터를 사용하여 가속도, 자이로스코프 및 자기장 측정이 의미 있게 이루어졌습니다. 이러한 방식으로 보다 정확하고 일관된 결과를 얻었습니다. 저렴한 비용과 휴대성으로 인해 IMU 센서는 값비싸고 침습적인 기존 이미징 방법(예: X선 및 MRI)에 대한 보다 보완적이고 실용적인 대안을 제공합니다. 블루투스를 통한 즉각적인 데이터 전송으로 사용자는 잘못된 자세를 빠르게 교정할 수 있습니다. 센서는 척추를 따라 5개의 척추뼈(C1, C7, T5, T12, L5)에 배치되었습니다. 이 배치를 통해 두개골과 경추부터 골반까지 척추 움직임을 포괄적으로 모니터링할 수 있습니다. 예를 들어, C1 영역에 배치된 센서는 머리 꼭대기와 경추 상부의 상세한 동역학을 기록했습니다. C7 센서는 경추와 흉추 사이의 전환 영역에서 움직임을 기록했습니다. T5 센서는 몸통의 회전 및 측면 굴곡 움직임을 기록했습니다. T12 센서는 흉요추 전이 영역의 움직임을 기록했습니다. L5 센서는 골반과 하체의 움직임을 기록했습니다. 피부 인공물과 정렬 오류를 줄이기 위해 의료용 테이프와 탄성 고정 장치를 사용하여 센서를 신체에 고정했습니다. 센서는 배치 전에 해부학적 정렬을 통해 보정되었으며 고정된 뼈 랜드마크는 참가자 전체에 걸쳐 일관된 위치를 보장합니다. 오정렬 및 배치 오류를 최소화하기 위해 동일한 훈련을 받은 연구자가 극돌기(C1, C7, T5, T12 및 L5)를 기준으로 센서를 배치했습니다. 각 센서는 배치 중에 시상면, 관상면 및 횡단면에 수동으로 정렬되었습니다. 이동 중 센서가 기울어지거나 변위되는 것을 방지하기 위해 탄성 스트랩과 의료용 테이프를 사용했습니다. 기록하기 전에 방향 편향을 줄이기 위해 센서를 직립 자세로 제로화했습니다. Madgwick의 필터링을 사용하여 드리프트 및 소음을 ​​최소화했습니다.

<!-- Page 7 -->

각 시도 전에 교정 확인을 반복합니다. 따라서 정렬 불량이 방지되고 센서가 올바르게 작동하는 것이 보장되었습니다. 지정된 지점에 센서를 배치하는 방법은 그림 2에 나와 있습니다. 그림 2에 표시된 대로 센서 배치는 모든 분석에서 일관되게 사용된 특정 척추 세그먼트를 정의합니다. 경추 전만증의 경우 C1~C7, 흉부 후만증의 경우 C7~T12, 요추 전만증의 경우 T12~L5, 척추측만증의 경우 C1~L5에 대한 측면(Y축) 편차가 있습니다. 이러한 정의는 척추 생체역학에서 확립된 방사선 촬영 표준과 일치하도록 선택되었습니다.

### Figure 2 - 센서의 위치와 해당 척추 분절 정의. IMU는 다음 위치에 배치되었습니다.
- 이미지 재현: [원문 추출 불명확]

C1, C7, T5, T12 및 L5 척추 수준. 이러한 배치는 시상면의 C1~C7(경추 전만증), C7~T12(흉부 후만증), T12~L5(요추 전만증), 관상면의 C1~L5 측면 편위(척추측만증) 등의 자세 관련 세그먼트를 정의했습니다. 모든 IMU 센서(MPU-9250)는 100Hz에서 샘플링되었습니다. 동시 초기화 및 타임스탬프 정렬을 통해 센서가 동기화되었습니다. 원시 방향 데이터는 로컬 센서 프레임에서 처리되었으며 직립 기준 자세로 정의된 해부학적 전역 프레임으로 변환되었습니다. 제로 기준 각도를 초기화하기 위해 중립 기립 시험이 사용되었습니다. 방향은 가속도계, 자이로스코프 및 자력계 신호를 이전의 정적 자이로스코프 바이어스 보정 및 자력계 보정과 결합한 Madgwick 필터(β = 0.1)를 사용하여 추정되었습니다. 오일러 각도 변환 전에 중력 정렬 및 방향 드리프트 보상이 적용되었습니다. 인접한 센서 사이의 상대 쿼터니언은 시상(굴곡/신장), 관상(측면 굽힘) 및 축(회전) 측정값을 제공했습니다. 시계열 데이터는 Savitzky-Golay 필터(창 길이 11개 샘플, 다항식 차수 3)를 사용하여 평활화되었습니다. 추가 원시-처리 신호 예제는 보충 그림 S1에 제공됩니다. 본 연구에서는 척추에 장착된 IMU 센서로부터 얻은 데이터를 이용하여 척추의 다양한 부위의 각도 변화를 계산하였다. 센서에서 얻은 데이터는 오일러 각도와 쿼터니언을 사용하여 처리됩니다. 이 데이터를 사용하면 시간에 따른 각도 변화를 추적할 수 있습니다. 경추, 흉추, 요추 부위의 움직임 패턴을 분석했습니다. 척추 경사각, 분절 정렬 및 위치 변화의 차이를 조사하기 위해 시계열 전반에 걸쳐 움직임 데이터를 분석했습니다.

### 2.5. Machine Learning (ML) Methods

이 연구에서는 ML 방법을 적용하여 인구통계학적, 인체측정학적, 일일 행동 변수를 사용하여 IMU에서 파생된 프록시 편차 레이블을 모델링했습니다. 모델링 전 기능

<!-- Page 8 -->

벡터는 데이터 유출을 방지하기 위해 각 교차 검증 접기 내에서 z-점수로 표준화되었습니다. 예측 변수에는 연령, 성별, 키, 체중, BMI, 주간 신체 활동, 일일 책상/스마트폰 사용이 포함되었으며 IMU 기반 자세 각도를 사용하여 결과 라벨을 생성했습니다. 기능 선택은 주로 인구 통계, 인체 측정 및 행동 예측 변수의 문헌 기반 포함을 기반으로 했습니다. 표본 크기가 작기 때문에 자동화된 차원 축소(예: PCA, RFE)가 적용되지 않았습니다. 대신 예측 변수는 사전에 미리 지정되었으며 모두 모델에 유지되었습니다. 이는 해석 가능성을 보장하고 과적합을 방지했습니다. 작은 표본 크기(n = 30)와 심각한 클래스 불균형을 해결하기 위해 모델 평가는 LOSO(leave-one-subject-out) 및 계층화된 k-겹 교차 검증을 포함하도록 재설계되었습니다. 오버샘플링 기술(소수 샘플 크기에 따라 SMOTE 또는 ROS) 및 class_weight 조정이 적용되었습니다. 각 검증 방식에 대해 Wilson의 방법을 사용하여 95% 신뢰 구간을 계산했습니다. 각 알고리즘에 대한 전처리 파이프라인과 조정된 하이퍼파라미터는 표 2에 요약되어 있습니다.

### Table 2 - 각 ML 알고리즘에 대한 파이프라인 및 조정된 하이퍼파라미터를 전처리합니다.
- 이미지 재현: [원문 추출 불명확]

알고리즘 전처리 하이퍼파라미터 SVM StandardScaler → (소수가 ≥3인 경우 SMOTE, 그렇지 않은 경우 ROS) kernel = {rbf, 선형}; C = {0.1, 1, 10, 100}; γ = {척도, 0.1, 0.01, 0.001}; class_weight = 균형 잡힌 로지스틱 회귀 StandardScaler → (SMOTE/ROS) 솔버 = liblinear; 페널티 = {l1, l2}; C = {0.01, 0.1, 1, 10, 100}; class_weight = 균형 잡힌; max_iter = 2000 KNN StandardScaler → (SMOTE/ROS) n_neighbors = {1, 3, 5, 7, 9}; 가중치 = {균일, 거리}; 미터법 = 민코프스키; p = {1, 2} 의사결정트리(SMOTE/ROS) 기준 = {gini,entropy}; max_깊이 = {없음, 2–5}; min_samples_split = {2–5}; min_samples_leaf = {1–3}; max_features = {없음, sqrt, log2}; ccp_alpha = {0.0, 0.001, 0.01}; class_weight = 균형 잡힌 랜덤 포레스트(SMOTE/ROS) n_estimators = 100; 최대 깊이 = 없음; 무작위 상태 = 42; class_weight = 균형 잡힌 ANN StandardScaler → (SMOTE/ROS) Hidden_layer_sizes = {(8), (16), (32), (16,8), (32,16)}; 활성화 = {relu,tanh}; 알파 = {0.0001, 0.001, 0.01}; 학습률 = 적응형; learning_rate_init = {0.001, 0.01}; 해결사 = 아담; max_iter = 1000; early_stopping = 사실; n_iter_no_change = 20; random_state = 42 ML은 데이터로부터 학습하고 예측하는 데 초점을 맞춘 인공 지능의 하위 분야입니다. 본 연구에서는 다양한 ML 알고리즘을 사용하여 최상의 결과를 얻는 것을 목표로 했습니다. 정확도, 정밀도, 재현율, F1 점수 등의 성능 지표를 사용하여 방법을 평가했습니다. 해부학적 자세 분석 및 추정 과정에서는 다양한 데이터 구조와 특징이 모델링에 미치는 영향을 평가하기 위해 본 연구에서 6개의 서로 다른 ML 알고리즘을 사용했습니다. 각 알고리즘의 성능은 정확도, 정밀도, 재현율, F1 점수 등의 지표를 사용하여 분석되었습니다. 이러한 측정항목의 공식은 다음과 같습니다.

- 정확도: 전체 사례 중 모델이 올바르게 분류한 사례의 비율입니다.
정확도 = TP + TN TP + TN + FP + FN

- 정밀도: 긍정적으로 분류된 예가 긍정적인 사례의 수를 나타냅니다.
정밀도 = TP TP + FP

- 재현율: 올바르게 예측된 참양성 사례의 수를 나타냅니다.
<!-- Page 9 -->

회상 = TP TP + FN

- F1 점수: 정밀도와 재현율의 조화 평균입니다.
F1 = 2 × Precision × Recall Precision + Recall ML에서 사용되는 TP, TN, FP, FN은 분류 모델의 성능을 평가하는 데 사용되는 용어입니다. 이러한 측정항목은 모델의 예측이 올바른지 또는 잘못된지를 나타냅니다. 표 3에서는 이러한 용어에 대한 설명을 제공합니다.

### Table 3 - 용어 설명.
- 이미지 재현: [원문 추출 불명확]

약어 설명 의미 TP 참양성 모델이 예측하는 상황은 긍정적이고 긍정적입니다. TN 참 부정 모델이 예측하는 상황은 부정적이며 부정적입니다. FP 거짓 긍정 모델이 예측하는 상황은 긍정적이지만 부정적입니다(제1종 오류). FN 거짓 부정 모델이 부정적으로 예측하지만 긍정적인 상황(유형 II 오류)입니다.

## 3. Results

남성 15명, 여성 15명의 인구통계학적 특성, 일상생활활동, 인체측정치를 성별로 비교하였다. 여성은 더 긴 신체 활동을 보고했고(p < 0.05), 더 긴 서 있는 시간에 대한 유의미한 경향을 보인 반면(p = 0.053), 남성은 경추 길이와 다리 길이가 더 컸습니다(p < 0.05, 표 4). 각 비교에 대해 p 값은 작은 표본(n = 30)의 해석을 돕기 위해 효과 크기(거의 정규 변수에 대해서는 Cohen의 d, 그렇지 않으면 순위-이중 상관 관계)와 함께 표시됩니다. 여러 변수(예: 키, 다리 길이)가 상대적으로 큰 절대 차이를 보였지만 그룹 내 변동성이 높으면 통계적 검정력이 감소했으며 일부 대비는 유의미한 수준에 도달하지 못했습니다. 따라서 표 4의 성별 대비는 이 작은 표본의 결정적인 차이보다는 효과 크기를 사용하여 설명적으로 해석되어야 합니다. 반대로, 신체 활동과 서 있는 시간은 변동성이 낮은 그룹 간 일관된 추세를 보였으며, 중간 정도의 평균 차이에도 불구하고 통계적으로 유의미한 결과를 얻었습니다. 이러한 결과는 표본 크기를 고려하여 주의 깊게 설명적으로 해석되어야 합니다. 이 연구에서는 참가자의 C1, C7, T5, T12 및 L5 척추에 배치된 IMU 센서에서 얻은 동적 자세 데이터를 사용했습니다. 직립 자세에서 정상 자세로 전환되는 각도 변화는 5개 주요 지점에 배치된 9축 IMU 센서를 사용하여 분석되었습니다. 원시 데이터는 각 센서를 사용하여 수집되었습니다. 참가자들에게 먼저 똑바로 선 자세로 서도록 요청한 다음, 편안한 일상 활동을 수행할 수 있는 자세로 이동하도록 요청했습니다. 자세 분석은 직립 자세와 편안한 자세 사이의 각도 변화를 관찰하여 수행되었습니다. 척추에 부착된 센서로부터 얻은 3축 각도 변화 값을 사용하였다. 구체적으로, 경추 전만증(C1~C7), 흉추 후만증(C7~T12), 요추 전만증(T12~L5)에 대한 X축 변화와 척추 측만증에 대한 Y축 변화를 계산했습니다. 본 연구에서 자세 관련 편차 범주는 문헌의 참조 범위에 대한 IMU 추정 각도로부터 파생되었습니다. 경추 전만각 편차는 C1-C7 X축 각도가 45°보다 크면 증가하고 35°보다 작으면 감소한 것으로 표시되었습니다. 흉부 후만증 편차는 C7-T12 각도가 > 40°인 경우 증가하고 <20°인 경우 감소한 것으로 표시되었습니다. 요추 전만각 편차는 T12-L5 각도 > 60°인 경우 증가하고 <40°인 경우 감소한 것으로 표시되었습니다. 척추측만증 선별검사 편차는 측면 Y축 편차가 ± 10°를 초과할 때 표시되었습니다.

<!-- Page 10 -->

### Table 4 - 인구통계학적 특성, 일상습관, 인체측정치 조사
- 이미지 재현: [원문 추출 불명확]

성별로. 인구통계학적 특성 일상생활활동 인체측정 남성(평균±SD) 여성(평균±SD) 검정 p값 효과크기 연령(세) 21.00 ± 1.46 20.40 ± 1.45 t-test 0.27 0.41 키(cm) 175.40 ± 5.95 160.40 ± 4.34 t-test 0.001 * 2.88 체중(kg) 70.93 ± 13.64 59.67 ± 12.57 t-검정 0.026 * 0.86 BMI 22.98 ± 3.79 23.24 ± 5.16 Mann-Whitney U 0.803 −0.06 근무 시간(시간/일) 2.67 ± 1.88 1.80 ± 1.07 Mann-Whitney U 0.309 0.57 전화/컴퓨터 사용 시간(시간/일) 5.00 ± 2.88 3.63 ± 1.45 Mann-Whitney U 0.26 0.6 신체 활동(시간/일) 1.59 ± 0.69 3.53 ± 2.22 Mann-Whitney U 0.014 * −1.18 서 있는 시간 (h/day) 3.53 ± 1.64 5.10 ± 2.49 t-test 0.053 −0.74 경추 길이 (cm) 9.97 ± 1.32 7.90 ± 1.04 t-test 0.001 * 1.74 흉추 길이 (cm) 28.93 ± 4.50 25.30 ± 2.68 t-검정 0.013 * 0.98 요추 길이 (cm) 13.13 ± 2.70 11.13 ± 1.52 t-검정 0.02 * 0.91 다리 길이 (cm) 91.47 ± 4.85 84.73 ± 3.65 Mann-Whitney U 0.001 * 1.57 발 길이(cm) 28.07 ± 2.02 25.27 ± 1.44 t-검정 0.001 * 1.6 보폭(cm) 48.40 ± 13.91 42.67 ± 18.38 t-검정 0.344 0.35 보폭(cm) 6.47 ± 4.00 3.87 ± 2.19 t-검정 0.038 * 0.81 * p < 0.05는 통계적으로 유의한 것으로 간주되었습니다. p ≥ 0.05는 유의하지 않은 것으로 간주되었습니다(ns). 방법 섹션에 설명된 전처리 및 보정에 따라 3축 각도 변화가 계산되고 요약되었습니다. Table 5는 경추전만증, 흉추후만증, 요추전만증, 척추측만증의 성별에 따른 편차를 평가한 것이다. 여성과 남성 사이에는 통계적으로 유의미한 차이가 발견되지 않았습니다(p > 0.05).

### Table 5 - 성별에 따라 경추 전만증, 흉추 후만증, 요추 전만증, 척추측만증 위험이 있습니다.
- 이미지 재현: [원문 추출 불명확]

남성(평균 ± SD) 여성(평균 ± SD) p 값 경추 전만증 예 아니오 0.068 흉부 후만증 예 아니오 0.064 요추 전만증 예 아니오 0.28 척추 측만증 예 아니오 0.30 Table 4에서 보는 바와 같이 일부 인체계측 변수(키, 다리 길이 등)에서는 절대차이가 크고 개인간 편차가 높아 통계적 유의성은 달성되지 않았다. 반면, 신체활동 기간 등 일부 변수에서는 그룹 간 경향이 더 두드러졌으나 차이는 미미하여 유의미한 결과를 얻었습니다. 이는 표본 크기 및 데이터 분포와 같은 통계 변수 때문입니다. 일상생활 활동, 경추 전만증, 흉추 후만증, 요추 전만증, 척추 측만증 및 통증 간의 관계를 그림 3a의 상관 행렬에서 조사했습니다. 소규모 집단에 대해 여러 쌍별 상관관계를 조사했기 때문에 결과를 주의 깊게 해석했습니다. 여러 테스트를 제어하기 위해 FDR(False Discovery Rate) 수정이 적용되었으며 조정 후에도 중요한 연관성만 남아 있습니다.

<!-- Page 11 -->

토론에서 고려되었습니다. 경추 전만증, 흉추 후만증, 요추 전만증, 척추 측만증 편차 범주는 예상 값을 초과하는 각도 변화로 정의되었습니다. 분석에는 일상 생활 습관이 다양한 자세 부문에 미치는 영향을 평가하기 위한 상관관계 및 회귀 분석이 포함되었습니다. 파란색으로 갈수록 음의 상관관계가 증가하고, 빨간색으로 갈수록 양의 상관관계가 증가합니다. 그림 3b에서는 성별, 연령, 키, 체중, BMI 등의 인구통계학적 특성과 척추 길이(경추, 흉추, 요추 길이), 다리 길이, 발 길이, 보폭, 보폭, 경추 전만증, 흉추 후만증, 요추 전만증, 척추 측만증 등의 인체 측정치 간의 관계를 상관 행렬에서 조사했습니다. 파란색으로 갈수록 음의 상관관계가 증가하고, 빨간색으로 갈수록 양의 상관관계가 증가합니다.

(가) (비)

### Figure 3 - (a) 일상생활활동과 경추전만증, 흉추후만 간의 상관행렬
- 이미지 재현: [원문 추출 불명확]

sis, 요추 전만증, 척추 측만증 및 통증. (b) 인구통계학적 특성, 인체 측정, 경추 전만증, 흉추 후만증, 요추 전만증 및 척추 측만증 사이의 상관 행렬. IMU 기반 편차 레이블의 기계 학습 분류 경추 전만증 위험, 흉부 후만증 위험, 요추 전만증 위험 및 척추 측만증 위험 열을 종속 변수로 결정하고 나머지는 독립 변수로 선택했습니다. 데이터 전처리 단계에서는 결측값을 찾아 평균법으로 채우고, 범주형 컬럼을 수치값으로 변환하였다. 모든 전처리 단계(대치, 스케일링 및 오버샘플링)는 각 교차 검증 접기 내에서 엄격하게 수행되었습니다. 대치 및 스케일링은 훈련 데이터에만 맞춘 다음 홀드아웃 접기에 적용한 반면, 오버샘플링(SMOTE/ROS)은 데이터 누출을 방지하기 위해 훈련 세트에서만 수행되었습니다. 그런 다음 데이터를 독립(X) 변수와 종속(y) 변수로 결정했습니다. 본 연구의 결과 변수는 공식적인 임상 진단이 아닌 IMU에서 파생된 각도 추정을 기반으로 한 위험 분류로 운용되었습니다. 컷오프 값은 척추 생체역학 문헌에 보고된 확립된 기준 범위(예: 경추 전만증 35~45°, 흉추 후만증 20~40°, Y축 편차 >±10°로 정의된 척추측만증 위험)에서 채택되었습니다. 이러한 범위는 이전 해부학 및 자세 연구에서 일관되게 인용되어 IMU 기반 운동학 평가와의 호환성을 보장합니다. 이 연구에는 Cobb 각도 측정과 같은 방사선학적 표준에 대한 직접적인 검증이 포함되지 않았지만 선택된 임계값은 학술 자료에서 널리 인정되는 값을 반영합니다. 모델 평가는 LOSO 및 계층화된 k-fold를 사용하여 수행되었습니다.

<!-- Page 12 -->

단일 학습-테스트 분할 대신 교차 검증. 심각한 클래스 불균형을 해결하기 위해 SMOTE 또는 ROS(Random Oversampling)가 class_weight 조정과 함께 적용되었습니다. 각 검증 체계에 대해 95% 신뢰 구간이 계산되었습니다. 해부학적 자세 분석을 위해 6개의 서로 다른 ML 알고리즘을 적용하고 비교했습니다. LR(로지스틱 회귀), SVM(지원 벡터 머신), KNN(K-Nearest Neighbor), DT(결정 트리), RF(Random Forest) 및 ANN(인공 신경망) 알고리즘이 평가되었습니다(그림 4). 클래스 불균형을 해결하고 재현성을 보장하기 위해 모든 모델은 주제별 LOSO 및/또는 계층화된 k-fold 체계 내에서 훈련되었습니다. 접기별 오버샘플링(SMOTE 또는 ROS) 및 해당하는 경우 class_weight = "균형"이 사용되었습니다. 성능은 정확성, 정밀도, 재현율, F1 점수(가중치) 및 95% Wilson 신뢰 구간으로 보고되었습니다. 폴드 레벨 혼동 행렬이 계산되었습니다. 척추 측만증의 경우 균형 잡힌 정확도와 AUPRC는 단 하나의 긍정적 사례로 인해 불안정합니다. 이러한 결과는 설명적으로만 제시됩니다. 계층화된 5겹 체계에 따른 집계 혼동 행렬은 그림 5에 나와 있습니다. 접기 수준 행렬은 공간 제약으로 인해 포함되지 않았지만 집계 결과는 접기 전체의 성능을 요약합니다. 척추측만증 혼동 행렬은 매우 낮은 양성 수(n = 1)를 반영하므로 확증적인 증거보다는 설명적인 증거를 제공합니다. 하이퍼파라미터는 균형 잡힌 정확도를 목표로 사용하여 트레이닝 폴드에 ​​대해서만 계층화된 k-겹 교차 검증을 통해 조정되었습니다. 모델별 설정은 표 2에 나와 있습니다.

### Figure 4 - ML 알고리즘 성능 결과.
- 이미지 재현: [원문 추출 불명확]

<!-- Page 13 -->

### Figure 5 - 다음에서 얻은 자세 분류를 위한 ML 알고리즘의 집계 혼동 행렬
- 이미지 재현: [원문 추출 불명확]

계층화된 5겹 CV. 경추 전만각 편차의 경우 RF, DT 및 ANN은 측정 항목 전체에서 상대적으로 높고 균형 잡힌 성능을 달성했으며 RF는 가장 균형 잡힌 정확도에 도달했습니다. 흉부 후만증에서는 RF와 ANN이 다시 경쟁력 있는 성능을 보인 반면, KNN은 중간 정도이지만 일관된 결과를 제공했습니다. 요추 전만증의 경우 RF와 ANN이 더 강력한 모델로 남아 있었지만 다른 알고리즘에서는 개선의 여지가 있었습니다. 척추 측만증 선별 편차에서는 주로 클래스 불균형과 측면 및 회전 편차의 복잡성으로 인해 성능 수준이 모델 전반에 걸쳐 더 낮고 가변적이었습니다. 이 경우 SVM이 가장 안정적인 결과를 제공했습니다. 그러나 척추 측만증 분류는 단지 설명적인 것으로 간주되어야 합니다. 왜냐하면 코호트에는 단 하나의 양성 사례만이 존재했기 때문입니다(표 5).

<!-- Page 14 -->

오버샘플링에도 불구하고 여러 접기에서 1개 이하의 양성 결과와 불안정한 추정치로 이어집니다. 균형 정확도는 모델 및 위험 범주에 따라 0.55에서 0.82 사이였으며 AUPRC 값은 지속적으로 기준 수준을 초과했습니다. 대다수 클래스 기준선의 범위는 0.53(흉부 후만증)에서 0.87(요추 전만증)까지였습니다. 양성 사례 수는 경추 전만증 = 6, 흉부 후만증 = 16, 요추 전만증 = 4, 척추측만증 = 1이었고, 일부 주름에는 척추측만증에 대한 양성 사례가 1개 이하로 포함되었습니다. 이러한 결과는 작고 불균형한 샘플에서 ML 접근 방식의 잠재력과 불안정성을 모두 강조합니다. 정확도, 정밀도, 재현율 및 F1 점수가 그림 4에 표시되어 있지만 상당한 클래스 불균형으로 인해 해석은 주로 균형 잡힌 정확도와 AUPRC에 의존해야 합니다. 비교를 돕기 위해 다수 클래스 기준선이 결과 섹션에 보고됩니다.

## 4. Discussion

이 섹션에서는 주요 결과를 해석하고 이를 이전 연구와 연관시키며 연구 한계 및 잠재적인 임상 적용에 대한 개요를 설명합니다. 비만과 BMI가 후만증, 전만증, 척추 측만증에 미치는 영향은 놀랍습니다. 키, 몸무게, BMI는 척추 건강 연구에서 자주 검사되지만 척추 기형에 대한 직접적인 영향은 제한적인 것으로 보입니다. 일반적으로 신장, 체중, BMI, 척추 변형(후만증, 전만증, 척추측만증) 사이에는 약한 상관관계가 있지만, 이 관계의 중요성은 연구마다 다릅니다. Rabieezadeh 등의 연구에서. [31], 12~15세 남자 청소년의 인체측정 측정과 전만 및 후만증 만곡 사이에는 통계적으로 유의미한 관계가 발견되지 않았습니다. 이러한 이유로 키, 체중, BMI는 이 연령대 남성의 경추 전만증과 후만증 각도를 평가하는 데 적합한 기준이 아니라고 말했습니다. Lazicet al. [32] 경추 전만증은 나이에 따라 변하고 성별에 따라 다르다고 밝혔습니다. 그들은 여성이 경추 전만증과 척추체 높이가 더 높은 반면 남성은 척추 사이 공간이 더 넓다고 말했습니다. Taoet al. [33] 경추 전만증은 인체 측정치보다는 추간판과 다양한 척추 해부학적 요인에 의해 영향을 받는다는 점을 강조합니다. Yiwaet al. [34] BMI가 높을수록 척추에 추가적인 압력이 가해지기 때문에 후만증이 증가하는 데 기여한다고 밝혔습니다. 그러나 이 관계는 그들의 연구에서 통계적으로 유의미하지 않았습니다. Bayartaiet al. [35] 비만 아동 및 청소년은 건강한 체중을 가진 아동 및 청소년에 비해 흉부 후만각이 훨씬 더 크며 비만은 척추 자세 및 이동성에 부정적인 영향을 미친다고 밝혔습니다. Valdovinoet al. [36]은 과도한 체중이 시상면 정렬과 척추 성장에 부정적인 영향을 미칠 수 있음을 보여주었습니다. Parmithaet al. [37] 특발성 척추측만증이 있는 청소년의 BMI와 척추 회전 기형 사이의 관계가 밝혀졌습니다. Warrenet al. [38]은 건강한 BMI조차도 척추 측만증 발병 위험에 영향을 미치며 성별 및 식단과 같은 요인이 이러한 상관 관계에 기여한다고 밝혔습니다. Naufal과 Azizi[39]는 BMI가 4~6세 어린이의 척추 측만증에 유의미한 영향을 미친다고 보고했습니다. 이 연구에서는 키, 체중, BMI와 경추 전만증 위험, 흉추 후만증 위험, 요추 전만증 위험 및 척추 측만증 위험 사이에 유의미한 관계가 없음을 발견했습니다. 이러한 발견은 본질적으로 탐색적이라는 점을 강조해야 합니다. 코호트는 18~25세의 건강한 젊은 성인들로만 구성되었으며 결과를 다른 연령 그룹이나 임상 인구 집단에 일반화할 수 없습니다. 따라서 우리는 이러한 결과를 결정적인 진단 증거가 아닌 타당성 수준의 신호로 구성합니다. 참가자들은 성장기를 마쳤기 때문에 관계가 없다고 생각되었습니다. 뼈의 발달이 완전하지 않은 젊은 연령층을 본 연구에 포함시켰다면 다른 결과가 나왔을 것이라고 생각한다. 이것이 본 연구의 단점 중 하나이다. 현재 연구는 건강한 개인을 대상으로 수행되었지만 "위험"이라는 용어는 현재 진단이 아니라 임상적으로 허용되는 기준 각도와의 편차를 나타냅니다. 이러한 편차는 비록 무증상이기는 하지만 향후 척추 기형의 소인을 나타낼 수 있으며, 특히 잘못된 자세 습관이나 장기간의 기계적 스트레스와 결합될 경우 더욱 그렇습니다. 일차적인 목표는 다음과 같았습니다.

<!-- Page 15 -->

아직 임상 기형으로 나타나지는 않지만 해부학적 정렬 불량을 나타내는 초기 단계의 형태학적 경향을 식별합니다. 따라서 본 연구의 위험 표시는 진단적 결론이라기보다는 예방적 분류 도구로 사용됩니다. 척추 병리 진단을 받은 개인을 포함한 향후 연구는 제안된 위험 임계값을 추가로 검증하는 데 도움이 될 것입니다. 경추, 흉추, 요추 부분은 생체역학적으로 서로 영향을 미칩니다. 경추 전만증의 변화는 흉추 후만증과 관련이 있으며 요추 전만증과 간접적으로 관련됩니다. 이 상황은 척추 분절 사이의 보상 메커니즘을 보여줍니다 [40,41]. 또한, 요추 전만증의 길이, 각도, 높이, 깊이는 흉추 구조에 가해지는 스트레스를 줄이는 데 필수적이며, 최적의 척추 정렬은 수술적 개입과 척추 만곡 사이의 관계를 고려하여 달성됩니다[42-46]. 이러한 발견은 척추 분절 사이의 생체역학적 균형이 삶의 질에 영향을 미치는 통증 및 기능 장애를 예방하는 데 근본적으로 중요하다는 것을 시사합니다. 우리 연구에서는 경추, 흉추, 요추 부위의 길이를 측정했습니다. 경추 부위의 길이가 증가함에 따라 경추 전만증 및 흉추 후만증의 위험이 증가하는 것으로 확인되었습니다. 흉부 부위의 길이가 길어질수록 흉부 후만증의 위험도 매우 높은 비율로 증가합니다. 요추 길이가 증가함에 따라 경추 전만증과 흉추 후만증의 위험이 증가했습니다. 서로 다른 척추 부위 사이의 생체역학적 관계는 척추 기형을 이해하고 치료하는 데 필수적입니다. 요추 전만증의 길이, 각도 및 깊이는 흉추 후만증과 전반적인 척추 정렬에 영향을 미치는 중요한 요소입니다 [42,43]. 특히 비만과 같은 상태에서 요추 전만증의 변화는 척추의 정적 및 동적 안정성을 결정하고 흉추의 스트레스를 감소시킵니다[44,45]. 또 다른 연구에서는 경추 전만증과 흉추 후만증 사이에 음의 관계가 있는 것으로 나타났으며, 경추 전만증의 감소가 흉추 후만증을 증가시키는 것으로 나타났습니다[40]. 또한, 수술적 중재로 흉부 후만증을 교정하면 척추 분절의 상호 연결성을 강조하는 요추 전만도 교정됩니다[41,46]. 본 연구에서는 문헌과 일치하여 경추 전만증, 흉추 후만증, 요추 전만증 및 척추측만증 위험이 다른 위험과 상관관계가 있는 것으로 나타났습니다. 연구 결과는 척추의 한 부위의 변화가 다른 부위에 연쇄적인 영향을 미칠 수 있으며 적절한 정렬을 보장하는 것이 최적의 척추 건강을 위해 필수적이라는 것을 보여줍니다. 최근 연구에 따르면 장시간 앉아 있는 자세와 과도한 스마트폰 사용은 특히 직장인과 젊은 층에서 자세 장애를 유발하는 것으로 나타났습니다. Singhvi와 Bharnuke의 [47] 연구에 따르면 책상 작업을 완료하는 개인이 장시간 앉아 있으면 장요근이 단축되어 요추 과다전만증이 발생하는 것으로 나타났습니다. 이러한 근육 단축은 전만증 증가로 인해 허리 통증을 증가시키는 것으로 알려져 있습니다. Barutet al. [48] ​​책상에 앉아 있는 시간이 늘어나면 허리 통증이 발생하고 이러한 사람들은 흉추 후만증 각도가 더 높다는 사실이 밝혀졌습니다. 정보 기술 근로자가 농업 근로자보다 더 높은 후만증 및 전만도 값을 보인다는 연구 결과도 이러한 결과를 뒷받침합니다[6]. Kim et al. [49]은 장기간 사무실 의자에 앉아 있으면 요추 전만곡률에 부정적인 영향을 미칠 수 있다고 제안했습니다. Shivangi 등의 연구에서. [50], 과도한 스마트폰 사용은 머리를 앞으로 향한 자세를 유발하며, 이는 목 장애와 유의한 관계가 있는 것으로 나타났다. Yanget al. [51] 부적절한 테이블 높이와 좋지 않은 앉는 습관은 특발성 척추측만증의 위험을 증가시키며, 특히 청소년에게서 더욱 그렇습니다. 그럼에도 불구하고 그들은 특정 시간에 앉는 자세를 바꾸고 올바른 자세를 유지하면 척추측만증 발병 가능성이 줄어든다고 보고했습니다. Betsch 등의 연구에서. [52] 및 Brühl et al. [53], 전화나 컴퓨터 사용은 같은 자세를 계속해서 사용하기 때문에 후만증과 전만증을 일으킨다고 한다. 본 연구에서는 다른 연구와 병행하여 사무직 및 전화 사용 시간이 길어질수록 경추전만증, 흉추후만증 위험이 증가하는 것으로 나타났으며,

<!-- Page 16 -->

요추 전만증 위험 및 척추 측만증 위험이 증가했습니다. 또한, 매일의 신체 활동은 경추 전만증과 요추 전만증, 특히 흉추 후만증의 위험을 감소시키는 것으로 나타났습니다. IMU 센서는 척추 움직임을 모니터링하는 데 사용됩니다. Valchinov et al. 연구에서 언급된 [54]는 Cobb 각도를 통해 개별 척추를 모니터링하고 후만증, 전만증 및 척추 측만증과 같은 상태를 감지하는 데 필수적입니다. 이는 조기 진단과 치료 계획 측면에서 매우 중요합니다. Voinea와 Mogan [55]은 IMU 센서를 사용하여 측면 척추 움직임을 평가하여 비침습적 척추측만증 모니터링을 제공합니다. 이러한 혁신적인 접근법은 특히 젊은 환자의 척추 건강을 보호하는 데 필수적입니다. ML 기술은 매우 낮은 오류로 척추 곡률을 예측할 수 있습니다. Mak 등의 [ 56] 연구에 따르면 신경망은 0.261cm의 오차로 척추 기형을 감지할 수 있습니다. 유사하게, Cho 등의 [57] 연구는 SVM 기술이 척추측만증과 관련된 보행 변화를 90.5% 정확도로 감지할 수 있음을 보여주었습니다. Balajiet al. [58]은 X선 영상을 사용하여 자동으로 요추 척추전방전위증을 감지하고 등급을 매기는 데 사용되는 ML에서 96.8% 민감도와 97.2% 재현율로 98.5%의 평균 민감도(mAP)를 보여주었습니다. 이는 ML이 요추 척추전방전위증의 조기 발견을 위한 신뢰할 수 있고 효과적인 솔루션임을 나타냅니다. IMU 센서를 이용하여 척추 자세를 분석하였고, ML 알고리즘을 이용하여 분류를 수행하였다. ML 분석에 따르면 RF와 ANN은 경추 및 요추 전만증 위험 예측 전반에 걸쳐 지속적으로 강력하고 균형 잡힌 성능을 달성한 반면, DT는 경추 결과에서도 경쟁적으로 수행되었습니다. 흉부 후만증의 경우 RF와 ANN이 다시 강력한 성능을 보인 반면 KNN은 중간이지만 안정적인 결과를 제공했습니다. 대조적으로, 척추 측만증 위험 예측은 더 다양한 결과를 가져왔습니다. SVM은 가장 안정적인 성능을 달성했지만 클래스 불균형과 척추 측만증의 회전 특성으로 인해 정밀도와 재현율 값이 변동했습니다. 이러한 발견은 시상면 편차(전만증, 후만증)가 웨어러블 IMU 센서에 의해 보다 안정적으로 캡처될 수 있는 반면 관상 및 회전 편차(척추측만증)는 기술적으로 여전히 어려운 것임을 시사합니다. 결과 전체의 전반적인 분류 정확도는 모델 및 위험 범주에 따라 0.60~0.90 사이였습니다. 이는 작고 불균형한 데이터 세트에서 ML 접근 방식의 잠재력과 한계를 모두 강조합니다. 중요한 것은, 이 연구의 "위험" 라벨은 임상적 진단이 아닌 규범적 자세로부터의 준임상적 편차를 나타내며, 이는 진단적 종점보다는 예방 지표로서의 잠재적 유용성을 시사합니다. 그러나 척추 측만증 예측의 모델 성능에서는 상당한 변동이 관찰되었습니다. 이러한 불일치는 척추 측만증과 같은 관상면 예측에서 특히 두드러졌습니다. 일반적으로 진폭이 더 크고 IMU 센서로 더 쉽게 포착되는 시상 움직임과 달리 관상 및 회전 편차는 미묘하고 다차원적인 경향이 있습니다. 이로 인해 특히 Y축을 따라 발생하는 사소한 센서 정렬 불량, 연조직 움직임 및 측정 소음에 대한 민감도가 높아집니다. 따라서 관상 매개변수의 모델 전반에 걸쳐 관찰된 성능 변화는 적어도 부분적으로는 웨어러블 센서를 사용하여 측면 및 회전 척추 움직임을 캡처하는 데 있어 복잡성과 기술적 한계로 인한 것일 수 있습니다. SVM은 척추 측만증 예측에 가장 좋은 결과를 제공했습니다. 반면 정밀도와 재현율 값에는 불일치가 있었습니다. 이는 척추 측만증 예측을 위해 추가 데이터 세트 또는 대체 모델링 접근법을 평가해야 함을 나타냅니다. 우리의 연구는 IMU에서 파생된 자세 각도를 사용하여 프록시 위험 라벨을 정의하고 ML 분류자가 인구통계, 인체 측정 및 일일 습관 변수와의 연관성을 탐색하는 타당성 분석을 제공합니다. 이러한 발견은 탐색적이며 임상적 진단으로 해석되어서는 안 됩니다. 이러한 맥락에서 우리는 우리의 연구가 문헌에 기여할 것을 제안합니다.

<!-- Page 17 -->

### 4.1. Limitations

이 연구에는 몇 가지 한계가 있습니다. 첫째, 위험 범주는 방사선 촬영 Cobb 각도와 같은 임상 진단이 아닌 문헌의 임계값을 기반으로 하는 IMU 파생 프록시 라벨을 나타냅니다. 임계값은 척추 생체역학 연구에서 일반적으로 보고되는 참조 범위에서 채택되었으며 IMU 기반 각도 추정과 호환되지만 최적의 임상 측정(예: 방사선 사진, 광학 시스템)에 대해 직접 검증되지 않았습니다. 따라서 현재의 결과는 진단 결과가 아닌 자세 편차의 예비 지표로 간주되어야 합니다. 또한 참가자들에게 스크린타임 애플리케이션을 통해 일일 전화 및 컴퓨터 사용량을 확인하도록 권장했지만 모든 개인이 객관적인 로그를 제공할 수 있는 것은 아닙니다. 결과적으로 데이터 세트의 일부는 여전히 자체 보고 추정치에 의존하여 회상 편향이 발생할 수 있습니다. 향후 연구에서는 일상 활동에 대한 완전히 객관적인 측정값을 얻기 위해 스마트폰 사용 추적 또는 웨어러블 모니터링 장치의 필수 통합을 고려해야 합니다. 둘째, 인구통계학적 및 인체측정학적 특징이 ML 단계에서 보조 예측 변수로 포함되었지만 분류 작업의 기초는 다른 IMU 기반 접근 방식과 일치하여 IMU 파생 결과 범주에 있습니다[20,27]. 이 하이브리드 디자인은 센서 기반 생체역학적 평가가 환자 특성과 함께 해석되는 임상 실습을 반영합니다. 이 연구에서는 평가자 간 또는 테스트-재테스트 ICC를 사용하여 센서-해부체 정렬 오류를 정량화하지 않았습니다. 변동성을 최소화하기 위해 만져볼 수 있는 랜드마크와 중립 기립 교정을 사용하여 동일한 연구자가 모든 배치를 수행했습니다. 향후 연구에는 공식적인 신뢰성 테스트가 포함되어야 합니다. 마지막으로, 작은 표본 크기(n = 30)와 심각한 학급 불균형(특히 척추 측만증 위험)으로 인해 결과의 일반화가 제한됩니다. 따라서 보고된 모델 성능은 탐색적 타당성 결과로 해석되어야 하며, 제안된 IMU 기반 위험 정의의 정확성과 임상적 유용성을 확인하려면 직접적인 임상 참조가 있는 더 크고 균형 잡힌 코호트에서의 검증이 필요할 것입니다. 특히, 척추 측만증 분류는 힘이 약해(1/30 양성) 오버샘플링으로 교정할 수 없는 접이식 불안정성을 초래했습니다. 그러므로 척추 측만증 결과는 본질적으로 탐구적인 것으로 간주되어야 하며 질적으로 논의되어야 합니다.

### 4.2. Clinical Applications

실제로 IMU 기반 자세 모니터링은 직장, 학교 및 가정 환경에서 종단적, 병원 밖 추적을 가능하게 함으로써 표준 평가에 대한 보조 보조 역할을 할 수 있습니다. 가능한 미래의 적용에는 인체공학적 검사, 일상적인 자세 습관 모니터링 또는 행동 변화를 장려하기 위한 피드백 제공에 대한 탐색적 사용이 포함될 수 있습니다. 이러한 사용은 여전히 ​​가설에 불과하며 진단 구현을 고려하기 전에 임상 표준에 대한 전향적 검증과 명확한 임상 임계값 설정이 필요합니다. 따라서 현재 워크플로는 향후 예방 전략을 알려줄 수 있는 탐구적이고 비진단 도구로 간주되어야 합니다.

## 5. Conclusions

결과는 IMU 기반 각도 정의 프록시 위험 라벨을 도출하고 인구통계학적, 인체측정학적 및 일일 습관 변수와의 연관성을 탐색하는 타당성을 뒷받침합니다. 그러나 이 연구는 임상적 효과를 확립하지 못합니다. 효과는 더 크고 다양한 코호트에서 전통적인 임상 표준(예: 방사선 촬영 Cobb 각도 또는 검증된 광학 시스템)에 대한 직접적인 검증을 통해서만 입증될 수 있습니다. 향후 연구에는 직접적인 임상 검증, 주제별 교차 검증 및 신뢰 구간을 갖춘 균형 잡힌 대규모 샘플, IMU 시계열 신호를 활용하는 모델 평가가 포함되어야 합니다. 그러한 증거가 나올 때까지,

<!-- Page 18 -->

제안된 워크플로는 독립형 진단이 아닌 보완적인 연구 도구로 간주되어야 합니다. 보충 자료: 다음 지원 정보는 https: //www.mdpi.com/article/10.3390/s25195963/s1에서 다운로드할 수 있습니다. 그림 S1: 대표적인 원시-처리 IMU 시계열 세그먼트 및 전처리 단계. 저자 기여: 개념: R.K. 디자인: R.K., Y.B.K. 감독 : Y.B.K. 재료: R.K., Y.B.K. 데이터 수집 및/또는 처리: R.K., Y.B.K. 분석 및/또는 해석: R.K., Y.B.K. 문헌 검토: R.K., Y.B.K. 작문: R.K., Y.B.K. 비판적 검토: Y.B.K. 모든 저자는 출판된 원고 버전을 읽고 이에 동의했습니다. 자금 지원: 이 연구는 Afyonkarahisar Health Sciences University 과학 연구 프로젝트 조정 단위 프로젝트 번호 23.GENEL.028의 지원을 받았습니다. 데이터 가용성 설명: 이 연구와 관련된 데이터는 윤리적 제한으로 인해 공개적으로 사용할 수 없습니다. 그러나 합리적인 요청이 있고 기관 윤리 위원회가 승인한 조건에 따라 저자가 제공할 수 있습니다. 또한 분석 코드는 https://github.com/ybahadirkoca/Posture_Analytic_ML(2025년 9월 16일 액세스)에서 공개적으로 제공됩니다. 원시 데이터는 합리적인 요청이 있을 경우 기관 윤리 위원회가 승인한 조건에 따라 저자가 제공할 수 있습니다. 이해 상충: 저자는 이해 상충을 선언하지 않습니다.

## References

1. Ye¸ sil, B. Posture and Its Influence on Anatomical Structures: A Comprehensive Review.Med. Sci. Discov. 2024, 11, 330–337. [CrossRef]

2. Zemková, E.; Zapletalová, L. The Role of Neuromuscular Control of Postural and Core Stability in Functional Movement and Athlete Performance. Front. Physiol. 2022, 13, 796097. [CrossRef]

3. Amran, N.N.; Basaruddin, K.S.; Ijaz, M.F.; Yazid, H.; Basah, S.N.; Muhayudin, N.A.; Sulaiman, A.R. Spine Deformity Assessment for Scoliosis Diagnostics Utilizing Image Processing Techniques: A Systematic Review. Appl. Sci. 2023, 13, 11555. [CrossRef]

4. Zappalá, M.; Lightbourne, S.; Heneghan, N.R. The Relationship between Thoracic Kyphosis and Age, and Normative Values across Age Groups: A Systematic Review of Healthy Adults. J. Orthop. Surg. Res. 2021, 16, 447. [CrossRef]

5. Weerakoon, T.C.S.; Dissanayake, P .H.; Weerasekera, M.M.; Jayakody, S.; Abeywickrama, B.N.; Yasawardene, S.G. Chronic Neck Pain and Its Association with the Angle of the Cervical Curve. Sri Lanka Anat. J. 2022, 6, 48–59. [CrossRef]

6. Bernhardt, M.; Bridwell, K.H. Segmental Analysis of the Sagittal Plane Alignment of the Normal Thoracic and Lumbar Spines and Thoracolumbar Junction. Spine 1989, 14, 717–721. [CrossRef]

7. Sharma, A.; Kalia, R. Assessment of the Posture of Adults at Their Workplace.Nurs. Midwifery Res. J. 2022, 18, 173–180. [CrossRef]

8. Carini, F.; Mazzola, M.; Fici, C.; Palmeri, S.; Messina, M.; Damiani, P .; Tomasello, G. Posture and Posturology, Anatomical and Physiological Profiles: Overview and Current State of Art. Acta Biomed. 2017, 88, 11–16.

9. Liao, D.-Y. Design of a Secure, Biofeedback, Head-and-Neck Posture Correction System. In Proceedings of the 2016 IEEE First International Conference on Connected Health: Applications, Systems and Engineering Technologies (CHASE), Washington, DC, USA, 27–29 June 2016; pp. 119–124.

10. Markova, V .; Markov, M.; Petrova, Z.; Filkova, S. Assessing the Impact of Prolonged Sitting and Poor Posture on Lower Back Pain: A Photogrammetric and Machine Learning Approach. Computers 2024, 13, 231. [CrossRef]

11. Asadullah, G.M.; Ali, H.; Hashikura, K.; Kamal, M.A.S.; Yamada, K. Development of an Automatic Air-Driven 3D-Printed Spinal Posture Corrector. Actuators 2022, 11, 184. [CrossRef]

12. Du, S.H.; Zhang, Y.H.; Yang, Q.H.; Wang, Y.C.; Fang, Y.; Wang, X.Q. Spinal Posture Assessment and Low Back Pain.EFORT Open Rev. 2023, 8, 708–718. [CrossRef]

13. Barragán-Montero, A.; Javaid, U.; Valdés, G.; Nguyen, D.; Desbordes, P .; Macq, B.; Willems, S.; Vandewinckele, L.; Holmström, M.; Löfman, F.; et al. Artificial Intelligence and Machine Learning for Medical Imaging: A Technology Review. Phys. Med. 2021, 83, 242–256. [CrossRef]

14. Vignais, N.; Miezal, M.; Bleser, G.; Mura, K.; Gorecky, D.; Marin, F. Innovative System for Real-Time Ergonomic Feedback in Industrial Manufacturing. Appl. Ergon. 2013, 44, 566–574. [CrossRef]

15. Schwab, F.J.; Smith, V .A.; Biserni, M.; Gamez, L.; Farcy, J.-P .C.; Pagala, M. Adult Scoliosis: A Quantitative Radiographic and Clinical Analysis. Spine 2002, 27, 387–392. [CrossRef] [PubMed]

<!-- Page 19 -->

16. Zhang, Y.; Chen, Y.; Huang, H.; Sandler, J.; Dai, M.; Ma, S.; Udelsman, R. Diagnostic Radiography Exposure Increases the Risk for Thyroid Microcarcinoma: A Population-Based Case—Control Study. Eur. J. Cancer Prev. 2015, 24, 439–446. [CrossRef]

17. Alsoliman, B.; Alrugebh, M.; Alzahrani, A.; Alshreef, N.A.; Algwiser, R.A. Advances in Musculoskeletal Radiology: Diagnostic Techniques and Clinical Applications. J. Adv. Sch. Res. Allied Educ. 2024, 21, 42–45. [CrossRef]

18. Vagnini, A.; Furone, R.; Zanotti, G.; Adamo, P .; Temporiti, F.; Gatti, R. Agreement between Inertial Measurement Unit and Optoelectronic System to Measure Postural Sway. Technol. Health Care 2022, 30, 757–762. [CrossRef]

19. Ranavolo, A.; Don, R.; Draicchio, F.; Bartolo, M.; Serrao, M.; Padua, L.; Cipolla, G.; Pierelli, F.; Iavicoli, S.; Sandrini, G. Modelling the Spine as a Deformable Body: Feasibility of Reconstruction Using an Optoelectronic System. Appl. Ergon. 2013, 44, 192–199. [CrossRef]

20. Michaud, F.; Lugrís, U.; Cuadrado, J. Determination of the 3D Human Spine Posture from Wearable Inertial Sensors and a Multibody Model of the Spine. Sensors 2022, 22, 4796. [CrossRef] [PubMed]

21. Petropoulos, A.; Sikeridis, D.; Antonakopoulos, T. Wearable Smart Health Advisors: An IMU-Enabled Posture Monitor.IEEE Consum. Electron. Mag. 2020, 9, 20–27. [CrossRef]

22. Yin, M.; Li, J.; Wang, T. A Low-Cost Inertial Measurement Unit Motion Capture System for Operation Posture Collection and Recognition. Sensors 2024, 24, 686. [CrossRef]

23. Smith, J.; Parikh, D.; Tate, V .; Siddicky, S.F.; Hsiao, H.Y. Validity of Valor Inertial Measurement Unit for Upper and Lower Extremity Joint Angles. Sensors 2024, 24, 5833. [CrossRef]

24. Matikainen-Tervola, E.; Cronin, N.; Aartolahti, E.; Sihvonen, S.; Sansgiri, S.; Finni, T.; Mattila, O.-P .; Rantakokko, M. Validity of IMU Sensors for Assessing Features of Walking in Laboratory and Outdoor Environments among Older Adults. Gait Posture 2024, 114, 277–283. [CrossRef]

25. Favata, A.; Gallart-Agut, R.; P àmies-Vilà, R.; Torras, C.; Font-Llagunes, J.M. IMU-Based Systems for Upper-Limb Kinematic Analysis in Clinical Applications: A Systematic Review. IEEE Sens. J. 2024, 24, 28576–28594. [CrossRef]

26. Bailes, A.H.; Johnson, M.; Roos, R.; Clark, W.; Cook, H.; McKernan, G.; Sowa, G.A.; Cham, R.; Bell, K.M. Assessing the Reliability and Validity of Inertial Measurement Units to Measure Three-Dimensional Spine and Hip Kinematics During Clinical Movement Tasks. Sensors 2024, 24, 6580. [CrossRef] [PubMed]

27. Paloschi, D.; Bravi, M.; Schena, E.; Miccinilli, S.; Morrone, M.; Sterzi, S.; Saccomandi, P .; Massaroni, C. Validation and Assessment of a Posture Measurement System with Magneto-Inertial Measurement Units. Sensors 2021, 21, 6610. [CrossRef] [PubMed]

28. Chen, T.; Xu, D.; Zhou, Z.; Zhou, H.; Shao, S.; Gu, Y. Prediction of Vertical Ground Reaction Forces Under Different Running Speeds: Integration of Wearable IMU with CNN-XLSTM. Sensors 2025, 25, 1249. [CrossRef]

29. Pitts, M.N.; Ebers, M.R.; Agresta, C.E.; Steele, K.M. Evaluating Sparse Inertial Measurement Unit Configurations for Inferring Treadmill Running Motion. Sensors 2025, 25, 2105. [CrossRef] [PubMed]

30. Freedkin, A.S.; Ryu, J.-C.; Hwang, J. Upper Body Joint Angle Calculation and Analysis Using Multiple Inertial Measurement Units. In Proceedings of the ASME International Mechanical Engineering Congress and Exposition; American Society of Mechanical Engineers, New Orleans, LA, USA, 29 October–2 November 2023; Volume 5.

31. Rabieezadeh, A.; Hovanloo, F.; Khaleghi, M.; Akbari, H. Turkish Journal of Sport and Exercise The Relationship of Height, Weight and Body Mass Index with Curvature of Spine Kyphosis and Lordosis in 12–15-Year Old Male Adolescents of Tehran.Turk. J. Sport Exerc. 2016, 18, 42–46.

32. Lazi´ c, E.; Gliši´ c, B.; Stamenkovi´ c, Z.; Nedeljkovi´ c, N. Changes in Cervical Lordosis and Cervicovertebral Morphology in Different Ages with the Possibility of Estimating Skeletal Maturity. Srp. Arh. Celok. Lek. 2015, 143, 662–668. [CrossRef]

33. Tao, Y.; Niemeyer, F.; Galbusera, F.; Jonas, R.; Samartzis, D.; Vogele, D.; Kienle, A.; Wilke, H.J. Sagittal Wedging of Intervertebral Discs and Vertebral Bodies in the Cervical Spine and Their Associations with Age, Sex and Cervical Lordosis: A Large-Scale Morphological Study. Clin. Anat. 2021, 34, 1111–1120. [CrossRef]

34. Yiwa, Y.G.A.; Andayani, N.L.N.; Negara, A.A.G.A.P .; Utama, A.A.G.E.S. Relationship between Body Mass Index (BMI) & Physical Activity with Cyphhosis in Physiotherapy Students at the Faculty of Medicine, Udayana University. Int. J. Health Med. Sci. 2023, 6, 47–55. [CrossRef]

35. Bayartai, M.E.; Schaer, C.E.; Luomajoki, H.; Tringali, G.; De Micheli, R.; Sartorio, A. Differences in Spinal Posture and Mobility between Children/Adolescents with Obesity and Age-Matched Normal-Weight Individuals. Sci. Rep. 2022, 12, 15570. [CrossRef]

36. Valdovino, A.G.; Bastrom, T.P .; Reighard, F.G.; Cross, M.; Bartley, C.E.; Shah, S.A.; Yaszay, B.; Newton, P .O.; Upasani, V . V Obesity Is Associated With Increased Thoracic Kyphosis in Adolescent Idiopathic Scoliosis Patients and Nonscoliotic Adolescents. Spine Deform. 2019, 7, 865–869. [CrossRef]

37. Parmitha, I.A.J.A.; Kinandana, G.P .; Andayani, N.L.N.; Fridayani, N.K.Y. Correlation between Body Mass Index with Scoliosis: A Narrative Review. Phys. Ther. J. Indones. 2023, 4, 255–259. [CrossRef]

38. Warren, J.M.; Hey, L.A.; Mazzoleni, A.P . Biomechanical Analysis of the Impact of Increasing Levels of Body Mass Index on the Ability of a Bracing Orthosis to Alter the Asymmetric Compressive Growth Plate Loading in a Scoliotic Spine. Biomed. Eng. Adv. 2022, 4, 100044. [CrossRef]

<!-- Page 20 -->

39. Naufal, A.F.; Azizi, L.R. The Effect of Body Mass Index on Scoliosis in Children Age 4-6 Years in The Kartasura Region.J. Ilm. Fisioter. Muhammadiyah 2024, 3, 1–14. [CrossRef]

40. Hellsing, E.; Reigo, T.; McWilliam, J.; Spangfort, E. Cervical and Lumbar Lordosis and Thoracic Kyphosis in 8, 11 and 15-Year-Old Children. Eur. J. Orthod. 1987, 9, 129–138. [CrossRef] [PubMed]

41. Newton, P .O.; Yaszay, B.; Upasani, V .V .; Pawelek, J.B.; Bastrom, T.P .; Lenke, L.G.; Lowe, T.; Crawford, A.; Betz, R.; Lonner, B.; et al. Preservation of Thoracic Kyphosis Is Critical to Maintain Lumbar Lordosis in the Surgical Treatment of Adolescent Idiopathic Scoliosis. Spine 2010, 35, 1365–1370. [CrossRef] [PubMed]

42. Sinaki, M.; Itoi, E.; Rogers, J.W.; Bergstralh, E.J.; Wahner, H.W. Correlation of Back Extensor Strength with Thoracic Kyphosis And Lumbar Lordosis In Estrogen-Deficient Women. Am. J. Phys. Med. Rehabil. 1996, 75, 370–374. [CrossRef] [PubMed]

43. Horie, J.; Murata, S.; Inoue, Y.; Nakamura, S.; Maeda, Y.; Matsumoto, Y.; Sannomiya, T.; Horikawa, E. A Study of the Influence of the Pulmonary Function on the Angles of Thoracic Kyphosis and Lumbar Lordosis in Community-Dwelling Elderly Women. J. Phys. Ther. Sci. 2009, 21, 169–172. [CrossRef]

44. Rahimi, A.; Ghadirian, F.; RezaSoltani, A.; Khalkhali Zavieh, M. Relationship between the Medial Longitudinal Arch and the Thoracic and Lumbar Curvatures with the Static and Dynamic Stability in Obese Females. Sci. J. Rehabil. Med. 2012, 1, 15–22.

45. Bruno, A.G.; Anderson, D.E.; D’Agostino, J.; Bouxsein, M.L. The Effect of Thoracic Kyphosis and Sagittal Plane Alignment on Vertebral Compressive Loading. J. Bone Miner. Res. 2012, 27, 2144–2151. [CrossRef] [PubMed]

46. Ye, J.; Rider, S.M.; Lafage, R.; Gupta, S.; Farooqi, A.S.; Protopsaltis, T.S.; Passias, P .G.; Smith, J.S.; Lafage, V .; Kim, H.J.; et al. Spinopelvic Sagittal Compensation in Adult Cervical Deformity. J. Neurosurg. Spine 2023, 39, 1–10. [CrossRef]

47. Singhvi, P .M.; Bharnuke, J.K. A Cross-Sectional Study on Association of Iliopsoas Muscle Length with Lumbar Lordosis Among Desk Job Workers. Indian J. Occup. Environ. Med. 2024, 28, 235–238. [CrossRef]

48. Koçak, F.A.; Barut, Ö.; Kurt, E.E.; ¸ Sa¸ s, S.; Tuncay, F.; Erdem, H.R. Sırt veya Bel A˘ grısı Olan ve Olmayan Tıbbi Sekreterlerin Omurga Sagittal E˘ grilikleri, Fonksiyonel Durum ve Ya¸ sam Kalitesi Düzeylerinin Kar¸ sıla¸ stırılması.Harran Üniversitesi Tıp Fakültesi Dergisi 2020, 17, 91–97. [CrossRef]

49. Kim, J.C.; Kim, J.G.; Kim, B.S.; Kim, C.K.; Choi, M.; Lee, J.; Chung, S.G. Assessing the Preservation of Lumbar Lordotic Curvature in Everyday Sitting Conditions Assessed with an Inertial Measurement System. J. Clin. Med. 2024, 13, 2728. [CrossRef]

50. Shivangi; Bhatia, S.; Koley, S. Digital Habits and Postural Impact: A Study on Prevalence of Forward Head Posture Among Collegiate Smartphone Users. Int. J. Health Sci. Res. 2024, 14, 265–271. [CrossRef]

51. Yang, J.; Huang, S.; Cheng, M.; Tan, W.; Yang, J. Postural Habits and Lifestyle Factors Associated with Adolescent Idiopathic Scoliosis (AIS) in China: Results from a Big Case—Control Study. J. Orthop. Surg. Res. 2022, 17, 472. [CrossRef]

52. Betsch, M.; Kalbhen, K.; Michalik, R.; Schenker, H.; Gatz, M.; Quack, V .; Siebers, H.; Wild, M.; Migliorini, F. The Influence of Smartphone Use on Spinal Posture—A Laboratory Study. Gait Posture 2021, 85, 298–303. [CrossRef]

53. Brühl, M.; Hmida, J.; Tomschi, F.; Cucchi, D.; Wirtz, D.C.; Strauss, A.C.; Hilberg, T. Smartphone Use—Influence on Posture and Gait during Standing and Walking. Healthcare 2023, 11, 2543. [CrossRef]

54. Valchinov, E.; Rotas, K.; Antoniou, A.; Syrimpeis, V .; Pallikarakis, N. Wearable System for Early Diagnosis and Follow up of Spine Curvature Disorders. In CMBEBIH 2019, Proceedings of the International Conference on Medical and Biological Engineering, Banja Luka, Bosnia and Herzegovina, 16–18 May 2019; Springer: Cham, Switzerland; pp. 205–209.

55. Voinea, G.D.; Mogan, G. Development of a Wearable Scoliosis Monitoring System Using Inertial Sensors. Appl. Mech. Mater. 2015, 811, 353–358. [CrossRef]

56. Mak, T.H.A.; Liang, R.; Chim, T.W.; Yip, J. A Neural Network Approach for Inertial Measurement Unit-Based Estimation of Three-Dimensional Spinal Curvature. Sensors 2023, 23, 6122. [CrossRef] [PubMed]

57. Cho, J.; Cho, Y.-S.; Moon, S.-B.; Kim, M.-J.; Lee, H.D.; Lee, S.Y.; Ji, Y.-H.; Park, Y.-S.; Han, C.-S.; Jang, S.-H. Scoliosis Screening through a Machine Learning Based Gait Analysis Test. Int. J. Precis. Eng. Manuf. 2018, 19, 1861–1872. [CrossRef]

58. Balaji, N.; Sunitha, R.; Pavithra, H.C.; Bhuvan, A.; Suhas, J. Automated X-Ray Image Analysis for Lumbar Spondylolisthesis Detection and Severity Grading. J. Innov. Image Process. 2024, 6, 133–153. [CrossRef]
