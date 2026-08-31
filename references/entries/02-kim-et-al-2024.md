# 2. Kim et al. (2024)

- **영문 제목**: Assessing the Preservation of Lumbar Lordotic Curvature in Everyday Sitting Conditions Assessed with an Inertial Measurement System
- **한글 제목**: 관성측정장치를 이용한 일상 좌식 조건에서의 요추 전만각 유지 평가
- **저자/출처**: Kim, J. C., Kim, J.-G., Kim, B. S., Kim, C. K., Choi, M., Lee, J., & Chung, S. G. (2024). _Journal of Clinical Medicine_, 13(9), 2728. (IRB No. 1703-174-842, Seoul National University Hospital) https://doi.org/10.3390/jcm13092728 (전문: https://pmc.ncbi.nlm.nih.gov/articles/PMC11084529/)
- **연도 정정 기록**: 2026-08-19에 원문에서 게재 연도를 확인하였다. 원문 표기는 `J. Clin. Med. 2024, 13, 2728`(투고 2024-03-27, 게재 2024-05-06)이므로 **2024년**이 맞다. 이전에 이 파일과 `outline.md`에 `2025`로 표기되어 있었다.
- **상태**: cited
- **연구목표**: AHRS 기반 관성센서(IMU)를 이용해 구두 지시, 의자 종류, 책상 작업 유형이라는 세 범주의 일상 좌식 조건에서 요추 전만각(LLA)의 크기(LLAavg)와 유지도(LLAdev)가 어떻게 변화하는지 평가.
- **집단 정의 및 피험자 수**: 건강한 성인 N=29 (남 15, 여 14). 정상 요추 전만 범위를 가진 것으로 예상되는 자를 대상으로 하였으며, 센서 부착 부위 피부질환·정신질환 등은 제외기준.
- **비교 조건**: 3개 범주, 총 7개 좌식 조건.
  - 구두 지시: 곧게 앉기(Iupright) vs. 평소 습관대로 앉기(Iusual)
  - 의자 종류: 사무용 의자(Coffice) vs. 등받이 없는 의자(Cstool) (표준의자 대비, 높이 45cm 무팔걸이 기준 의자 사용)
  - 책상 작업: 키보드 타이핑(Tkeyboard), 마우스 조작(Tmouse), 필기(Twriting)
  - 각 조건 3분간 착석 유지.
- **측정 방법 및 절차**: 실험실 단일 세션에서 전 참가자 동일 프로토콜(3개 범주 총 7개 좌식조건) 수행. IMU 부착 전 두 센서를 실험실 코너에서 병렬 캘리브레이션(캘리브레이션 후 두 센서 간 각도차가 0에 근접함을 확인)한 뒤 의료용 테이프로 T12·S2 극돌기 피부에 고정. 각 조건별로 3분간 해당 자세를 유지시키며 데이터를 40Hz로 무선 수집.
- **측정장비 및 변인**: 무선 IMU 2개(MTw Awinda, Xsens Technologies B.V., Netherlands; 40Hz), T12 극돌기와 S2(천골) 극돌기 피부에 부착. 두 센서 간 상대각(시상면 기준 단순 차감법)으로 요추 전만각(LLA) 산출. 변인: LLAavg(평균 전만각), LLAdev(전만각 유지 편차/변동성).

## Citation Like

- **원문 텍스트**: [Assessing the Preservation of Lumbar Lordotic Curvature in Everyday Sitting Conditions Assessed with an Inertial Measurement System.txt](../Assessing%20the%20Preservation%20of%20Lumbar%20Lordotic%20Curvature%20in%20Everyday%20Sitting%20Conditions%20Assessed%20with%20an%20Inertial%20Measurement%20System.txt)

1. [introduce_copilot.md - IMU 측정과 요추각 변인](../../introduce_copilot.md#초안-imu-측정과-요추각-변인)
   > "Using medical tape, two IMU sensors were affixed on the skin over the spinous process of the 12th thoracic vertebra, palpated along the 12th rib, and over the 2nd sacral vertebra at the midpoint between the posterior superior iliac spines."
   >
   > "Data from the sensors were sampled at a rate of 40 Hz and wirelessly transmitted to a data-processing computer."
   >
   > "Lumbar posture was determined by subtracting the angles between the thoracic sensor (T12) and the sacral sensor (S2) along each of these axes."
   >
   > "LLAavg was computed by dividing SumLLA by the test duration, where SumLLA represents a time-weighted integration of LLA obtained using the trapezoidal rule."
   >
   > "LLAdev was defined as the deviation from LLAstart, the initial LLA value at the start of the test."

2. [introduce.md - 관성측정장치와 요추각 변인](../../introduce.md#관성측정장치와-요추각-변인)

  > "Using medical tape, two IMU sensors were affixed on the skin over the spinous process of the 12th thoracic vertebra, palpated along the 12th rib, and over the 2nd sacral vertebra at the midpoint between the posterior superior iliac spines."
  >
  > "Data from the sensors were sampled at a rate of 40 Hz and wirelessly transmitted to a data-processing computer."
  >
  > "Lumbar posture was determined by subtracting the angles between the thoracic sensor (T12) and the sacral sensor (S2) along each of these axes."
  >
  > "LLAavg was computed by dividing SumLLA by the test duration, where SumLLA represents a time-weighted integration of LLA obtained using the trapezoidal rule."
  >
  > "LLAdev was defined as the deviation from LLAstart, the initial LLA value at the start of the test."
