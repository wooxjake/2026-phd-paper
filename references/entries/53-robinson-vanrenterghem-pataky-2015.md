# 53. Robinson, Vanrenterghem, & Pataky (2015)

- **영문 제목**: Statistical Parametric Mapping (SPM) for alpha-based statistical analyses of multi-muscle EMG time-series
- **한글 제목**: 다근육 EMG 시계열의 알파 기반 통계 분석을 위한 Statistical Parametric Mapping
- **저자/출처**: Robinson, M. A., Vanrenterghem, J., & Pataky, T. C. (2015). _Journal of Electromyography and Kinesiology_, 25(1), 14-19. https://doi.org/10.1016/j.jelekin.2014.10.018
- **URL**: https://doi.org/10.1016/j.jelekin.2014.10.018 / PDF 원문 `references/Statistical Parametric Mapping (SPM) for alpha-based statistical analyses of multi-muscle EMG time-series.pdf`
- **상태**: candidate
- **연구목표**: 다근육 EMG 시계열을 스칼라 요약값이 아니라 SPM 벡터장으로 분석해야 하는 이유를 보이고, 스칼라 분석과 SPM 분석의 차이를 공개 데이터로 비교한다.
- **집단 정의 및 피험자 수**: Bovi et al. (2011)의 공개 데이터셋을 재분석하였다. 건강한 대상자 40명 중 young 20명(6-17세)과 adult 20명(22-72세)을 비교하였다.
- **비교 조건**: young vs adult 비교, 35-45% stance phase의 스칼라 분석 vs 전체 EMG time-series에 대한 SPM vector-field 분석을 비교하였다.
- **측정 방법 및 절차**: 공개 데이터셋의 3D multi-joint kinematics, kinetics, EMG를 사용하였다. 걷기(walking) trial에서 Anterior Tibialis, Soleus, Gastrocnemius Medialis, Peroneus Longus의 mean EMG time-series를 선택하였다. 데이터는 Gaussian kernel(FWHM 2.0%, SD 4.7%)으로 필터링하였고, 스칼라 분석은 각 근육과 시점에 대해 두 표본 t-검정을 수행하였다. SPM 분석은 Python 2.7/Canopy 1.1에서 SPM Hotelling’s T2 statistic으로 수행하였다.
- **측정장비 및 변인**: 새 실험 장비는 사용하지 않았다. Bovi et al. (2011) 공개 EMG 및 3차원 운동학/운동역학 데이터셋, Anterior Tibialis, Soleus, Gastrocnemius Medialis, Peroneus Longus EMG time-series, 35-45% stance phase의 scalar 값, SPM vector-field, Hotelling’s T2를 사용하였다.
- **결과**: 35-45% stance phase의 스칼라 분석은 Young과 Adult 사이의 차이를 보여 주지 못했지만, SPM vector-field 분석은 해당 구간에서 통계적으로 유의한 차이를 확인하였다. 스칼라 분석은 다근육 및 시간 의존성을 반영하지 못해 Type II error를 보였고, SPM은 Type I과 Type II error를 동시에 통제하는 분석 틀로 제시되었다.
- **현재 연구에서의 활용 범위**: 다근육 EMG 시계열을 분석할 때 스칼라 축약 대신 SPM을 적용해야 하는 방법론적 근거로 사용한다.

## Citation Like

- **원문 텍스트**: [Statistical Parametric Mapping (SPM) for alpha-based statistical analyses of multi-muscle EMG time-series.txt](<../Statistical%20Parametric%20Mapping%20(SPM)%20for%20alpha-based%20statistical%20analyses%20of%20multi-muscle%20EMG%20time-series.txt>)

1. [본문 인용 위치 미정]

   > "Multi-muscle EMG time-series are highly correlated and time dependent yet traditional statistical analysis of scalars from an EMG time-series fails to account for such dependencies."

   > "SPM vector-field analysis did however identify statistical differences within this time period."

2. [본문 인용 위치 미정]

   > "SPM vector-field analysis on the other hand accounts for both dependencies whilst tightly controlling for Type I and Type II error making it highly applicable to EMG data analysis."
