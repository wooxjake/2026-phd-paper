# 러닝 운동역학 실험 매뉴얼 — 지면반력 트레드밀 + QTM

<!--
작성: 2026-10-15, Claude Code. Data collection과 Data processing 절을 문헌 기반으로 작성하였다.
- 문헌의 서지와 인용한 결과는 PubMed 서지 기록과 초록 또는 PMC 전문으로 확인하였다. 각 문헌의 연구 맥락(보행/러닝, 지상/트레드밀)을 함께 적었으며, 맥락이 다른 문헌은 본 실험에 그대로 적용하지 않고 "참고"로만 표시하였다.
- [확인 필요]: 실험실 장비 사양이나 실험 설계에 따라 결정할 값, 또는 문헌 근거를 아직 확보하지 못한 값.
- [실험실 결정]: 문헌이 직접 정해 주지 않아 실험실 운영 규칙으로 정할 값.
- 이 매뉴얼은 학위논문 본문이 아니므로 references.md와 references/entries에 등록하지 않았다. 논문에 인용하게 되면 그때 등록한다.
-->

## 0. 범위와 전제

- 장비: Qualisys 광학식 동작분석 시스템(Qualisys Track Manager: QTM)과 지면반력 트레드밀(instrumented treadmill). 카메라 대수·모델, 트레드밀 모델, 벨트 구성(단일 벨트 또는 좌우 분리 벨트) [확인 필요]
- 산출: 지면반력(ground reaction force: GRF), 하지 관절 각도, 관절모멘트, 관절 파워
- 트레드밀 전체(모터 포함)가 힘 센서 위에 놓인 구조에서는 벨트 마찰을 포함한 내부력이 서로 상쇄되어 수직·수평 지면반력이 정확히 전달된다(Willems & Gosseye, 2013).
- 지면반력 트레드밀에서 측정한 러닝 변인은 지상 러닝과 비슷하나 동일하지 않으며, 트레드밀 표면이 충분히 단단하고 벨트 속도가 일정하게 유지되어야 지상 러닝으로 일반화할 수 있다(Riley et al., 2008).
- 메타분석에서 트레드밀 러닝과 지상 러닝은 대부분의 변인이 비슷하였으나, 착지 시 발-지면 시상면 각도, 접지시간, 착지 시 무릎 굴곡각, 발목 시상면 관절모멘트 등에서 차이가 보고되었다(Van Hooren et al., 2020). 결과를 지상 러닝으로 일반화할 때 이 변인들은 제한점으로 기재한다.

---

# Data collection

## 1. 세션 전 점검 (매 측정일)

| 순서 | 항목 | 절차 | 근거·비고 |
| --- | --- | --- | --- |
| 1 | 카메라 캘리브레이션 | QTM wand 캘리브레이션 수행, 결과 리포트(평균 잔차, 카메라별 point 수) 저장 | 허용 잔차 기준 [확인 필요] |
| 2 | 트레드밀 힘판 영점 | 벨트 정지·무부하 상태에서 zero 설정. 매 trial 시작 직전 무부하 신호 재확인 | — |
| 3 | 좌표계 정렬·압력중심 확인 | 끝에 마커를 붙인 막대로 벨트 위 여러 지점을 눌러 압력중심(center of pressure: COP)과 막대 끝 마커 위치를 비교 | 계측 막대를 이용한 보정은 힘 트레드밀의 COP 오차를 91% 줄였다(Collins, Adamczyk, Ferris, & Kuo, 2009). 허용 오차 [확인 필요] |
| 4 | 동기화 | 카메라와 아날로그(힘판) 신호 동기 확인 | 동기 방식(QTM 아날로그 보드 또는 트레드밀 외부 트리거) [확인 필요] |
| 5 | 무부하 노이즈 기록 | 벨트를 측정 속도로 구동하고 사람 없이 5 s 기록 → 수직 GRF 노이즈 최대 진폭 확인 | 이벤트 역치 설정에 사용(§8) |

## 2. 파일 명명 규칙

형식: `S{피험자번호 2자리}_{YYMMDD}_{시행유형}_{조건}_T{반복 2자리}.qtm`

| 시행 | 예시 |
| --- | --- |
| 정적 시행 | `S01_260518_static_T01.qtm` |
| 무부하 노이즈 | `S00_260518_noise_v30_T01.qtm` |
| 러닝 시행 | `S01_260518_run_v30_T01.qtm` (v30 = 3.0 m/s) |

- 피험자번호를 맨 앞에 둔다. 기존 예시(`sub_260518_trial1_id.qtm`)는 ID가 끝에 있어 파일 목록을 이름순으로 정렬하면 피험자별로 묶이지 않는다.
- 영문, 숫자, 언더스코어만 사용하고 공백과 한글은 쓰지 않는다. 조건 코드(v30, shoeA 등)는 별도 코드표로 관리한다.
- 파일 하나에 trial log 한 행을 대응시킨다. 기록 항목: 파일명, 시각, 벨트 속도, 신발, 적응 시간, 휴식 시간, 마커 탈락·재부착, 특이사항.

## 3. 마커셋

### 3.1 원칙

- 정적 시행에서 해부학적 랜드마크로 분절의 해부학 좌표계를 정의하고, 동적 시행에서는 추적용(technical) 마커로 분절을 추적한다(Cappozzo, Catani, Della Croce, & Leardini, 1995; Cappozzo, Della Croce, Leardini, & Chiari, 2005).
- 한 분절의 위치와 방향(6자유도)을 추적하려면 그 분절에 일직선 위에 놓이지 않은 마커가 3개 이상 필요하다. 이 조건을 만족하지 않는 분절은 관절 각도를 산출할 수 없다.

### 3.2 하지 — 클러스터

- 대퇴와 하퇴: 강체 판(rigid shell)에 추적 마커 4개를 붙인 클러스터를 사용한다.
  - 보행 연구에서 하퇴 원위 외측에 언더랩으로 고정한 4마커 강체 판이 경골 회전을 가장 잘 추정하였으나, 이 조건에서도 내외측·전후 축에서 ±2°, 장축에서 ±4°의 회전 편차가 남았다(Manal, McClay, Stanhope, Richards, & Galinat, 2000).
  - 지면반력 트레드밀 러닝 연구에서도 대퇴와 하퇴에 4마커 강체 판 클러스터를 사용하였다(Fukuchi, Fukuchi, & Duarte, 2017).
- 고정: 탄성 랩 위에 클러스터를 얹고 테이프로 감는다. 고정 방식과 클러스터 크기 [실험실 결정]
- 정적 시행 전용 해부학 마커: 대전자, 대퇴 내·외측상과, 내·외측 복사. 정적 시행 후 제거하되, 해부학 마커와 추적 마커를 겸하는 마커는 남긴다(Fukuchi et al., 2017).
- 골반: 좌우 전상장골극(ASIS)과 후상장골극(PSIS). 러닝 중 팔 흔들기로 ASIS가 가려지면 추적용 마커 추가 여부 [확인 필요]

### 3.3 발 — 2분절(후족부·전족부)

| 분절 | 마커(신발 위 부착) | 용도 |
| --- | --- | --- |
| 후족부 | 종골 상부, 종골 하부, 종골 외측 | 후족부 추적, 착지 이벤트 백업 |
| 전족부 | 제1 중족골두, 제5 중족골두, 제2 중족골두 [확인 필요] | 전족부 추적, 착지 이벤트 백업 |
| 무지 | 무지(hallux) 1개 | 이지 이벤트 백업(§8.3) |

- 관절모멘트와 파워는 발을 단일 강체로 보고 산출한다. 다분절 발 모델에서 분절별 관절모멘트를 구하려면 분절마다 지면반력을 따로 측정해야 하며, 선행연구는 인접한 힘판 2개와 표적 보행을 사용하였다(Bruening, Cooney, & Buczek, 2012). 트레드밀 벨트 하나로는 후족부와 전족부의 지면반력을 나눌 수 없다.
- 따라서 2분절 발은 운동학(하퇴-후족부, 후족부-전족부 각도)에만 사용한다. 같은 연구에서 단일 분절 발 모델은 발목 파워를 과대추정하였으므로(Bruening et al., 2012), 발목 파워를 보고할 때 제한점으로 기재한다. 이 연구는 소아 보행 자료이다.
- 착지 패턴 분류에는 착지 시 시상면 발-지면 각도(footstrike angle)를 사용한다. 이 각도는 힘판 자료로 산출하는 strike index와 유의한 상관을 보였다(Altman & Davis, 2012).

### 3.4 몸통·상지·머리

| 분절 | 현재 계획 | 산출 가능 범위 | 결정 사항 |
| --- | --- | --- | --- |
| 흉곽 | 흉골 절흔(IJ), 검상돌기(PX), C7, T8 | 흉곽 좌표계와 각도(Wu et al., 2005) | — |
| 상완·전완·손 | 분절당 1개 | 마커 위치 궤적(팔 흔들기 범위)만 산출. 분절 방향과 관절 각도는 산출 불가 | 상지 각도나 분절 질량중심이 필요하면 분절당 3개 이상으로 늘린다 [확인 필요] |
| 머리 | [확인 필요] | 마커 1개는 위치만, 헤드밴드 마커 3~4개는 위치와 머리 방향을 산출 | 머리 방향이 필요한지 결정 [확인 필요] |

### 3.5 마커셋 기록 양식

| 분절 | 추적 마커 | 정적 전용 마커 | 부착 위치 사진 파일 |
| --- | --- | --- | --- |
| 골반 | | | |
| 대퇴(L/R) | 클러스터 4 | 대전자, 내·외측상과 | |
| 하퇴(L/R) | 클러스터 4 | 내·외측 복사 | |
| 후족부(L/R) | 종골 3 | — | |
| 전족부(L/R) | 중족골두 3, 무지 1 | — | |
| 흉곽 | IJ, PX, C7, T8 | — | |
| 상지·머리 | | | |

## 4. 피험자 준비

- 측정: 신장, 체중, 다리 길이, 골반 폭과 깊이. 골반 폭·깊이와 다리 길이는 고관절 중심 회귀식의 입력값이다(Harrington, Zavatsky, Lawson, Yuan, & Theologis, 2007).
- 체중은 트레드밀 힘판에 정지 상태로 선 수직 GRF로도 확인한다.
- 신발: 표준 신발과 개인 신발 중 선택 [확인 필요]. 처음 신는 신발은 2~3분, 평소 신발은 7분 뒤 하지 운동학이 안정되었으므로(Huang et al., 2023), 신발 선택에 따라 적응 시간을 다시 검토한다.
- 사전 설문: 트레드밀 러닝 경험, 주간 러닝 거리, 최근 부상 이력 [확인 필요]

## 5. 실험 절차

### 5.1 순서

1. 세션 전 점검(§1)
2. 피험자 준비와 마커 부착(§3, §4)
3. 정적 시행
4. 적응기(§5.3)
5. 조건별 러닝: 조건 내 적응 → 기록 30 s(§5.4)
6. 조건 사이 휴식(§5.5)
7. 마커 제거 전 누락 시행 확인

### 5.2 정적 시행

- 발 위치를 정해진 틀에 맞추고 해부학적 자세로 선다.
- 선행연구는 1 s를 기록하였다(Fukuchi et al., 2017). 본 매뉴얼은 3 s를 기록하고 가운데 1 s를 평균한다 [실험실 결정].
- 기능적 고관절 중심 시행 추가 여부 [확인 필요]

### 5.3 적응기

| 문헌 | 대상·조건 | 결과 |
| --- | --- | --- |
| Lavcanska, Taylor, & Schache (2005) | 트레드밀 경험이 없는 성인, 자기선택속도 11분 | 시상면 관절 운동학, 케이던스, 스트라이드 시간이 6분부터 변하지 않았다 |
| Arnold, Weeks, & Horan (2019) | 트레드밀 경험이 없는 남성, 맨발·신발, 20분 | 두 조건 모두 8분 이후 시간에 따른 차이가 없었다. 최대 순간 수직 부하율은 8분 이후에도 연속 시점 간 신뢰도(ICC > 0.90) 기준을 충족하지 못하였다 |
| Huang et al. (2023) | 처음 신는 신발·평소 신발, 자기선택속도 10분 | 처음 신는 신발 2~3분, 평소 신발 7분 |
| Van Hooren et al. (2020) | 체계적 문헌고찰 | 측정 직전 6분 미만의 적응을 둔 연구가 14편이었다. 트레드밀 초보자에게는 조건마다 8분 이상의 적응을 권고하였다 |

- 기준: 측정 속도 또는 자기선택속도로 **8분** 적응한 뒤 기록을 시작한다(Arnold et al., 2019; Van Hooren et al., 2020).
- 연구에서 6분 미만의 적응이 흔하였으나(Van Hooren et al., 2020), 6분은 시상면 운동학 기준이고(Lavcanska et al., 2005) 지면반력 변인은 포함하지 않았다. 운동역학을 측정하므로 8분을 적용한다.
- 부하율은 8분 이후에도 안정성이 낮았으므로(Arnold et al., 2019) 부하율을 1차 변인으로 정하면 적응 시간 연장 여부를 검토한다 [확인 필요].

### 5.4 조건별 러닝 시간과 기록 구간

- 선행연구는 속도마다 3분 적응한 뒤 30 s를 기록하였고, 분석한 발 접지는 매번 30회 이상이었다(Fukuchi et al., 2017).
- 기준: 조건마다 3분 러닝 후 30 s 기록 [실험실 결정]. 첫 조건은 §5.3의 8분 적응이 이 3분을 대신한다.
- 30 s 기록의 충분성: 케이던스 170 steps/min이면 30 s에 약 85 steps(약 42 strides)이다. 마커 결측이나 이벤트 오류로 스텝을 제외해도 §9의 필요 스텝 수를 확보할 수 있다.
- 조건 순서: 선행연구는 속도를 같은 순서(2.5 → 3.5 → 4.5 m/s)로 고정하였다(Fukuchi et al., 2017). 신발이나 중재처럼 순서 효과가 우려되는 조건은 무작위화 또는 역균형화한다 [확인 필요].

### 5.5 조건 사이 휴식

- 확인한 문헌은 공통 휴식 시간을 제시하지 않았으며, 연구 설계에 따라 달랐다.
  - 속도를 올리는 연속 프로토콜은 속도 사이 휴식 없이 다음 속도의 적응기로 넘어갔다(Fukuchi et al., 2017).
  - Van Hooren et al.(2020)은 트레드밀 초보자에게 조건마다 8분 이상의 적응을 권고하였다. 휴식으로 러닝을 중단하면 다음 조건에서 적응을 다시 거친다.
- 기준 [확인 필요]
  - 속도만 바꾸는 연속 프로토콜: 휴식 없이 다음 속도로 전환, 속도별 3분 적응.
  - 신발·중재를 바꾸는 프로토콜: 앉아서 휴식 후 재적응. 휴식 길이는 근거 문헌을 확보한 뒤 정한다.
- 휴식 시간은 실제 값을 trial log에 기록한다.

### 5.6 안전

- 안전 하네스, 비상정지 버튼 위치, 측정 중단 기준 [확인 필요]

---

# Data processing

## 6. 샘플링레이트

| 신호 | 기준 | 문헌 예 |
| --- | --- | --- |
| 마커 | 200 Hz [확인 필요] | 150 Hz(Fukuchi et al., 2017), 240 Hz(Kristianslund, Krosshaug, & van den Bogert, 2012) |
| GRF | 1000 Hz [확인 필요] | 300 Hz(Fukuchi et al., 2017), 960 Hz(Kristianslund et al., 2012) |

- GRF 샘플링레이트는 마커 샘플링레이트의 정수배로 설정한다. 두 문헌의 설정도 2배와 4배였다. 정수배이면 GRF를 마커 프레임에 맞출 때 보간 없이 추출할 수 있다.
- Kristianslund et al.(2012)은 방향 전환(sidestep cutting) 동작 연구이다.

## 7. 필터와 차단주파수

### 7.1 관절모멘트 산출용 — 마커와 GRF에 같은 차단주파수

- 필터: 4차 저역통과 Butterworth, 정방향·역방향 적용(위상 지연 없음). 2차 필터를 양방향으로 적용해 4차가 된 것인지, 4차 필터를 양방향으로 적용한 것인지 보고서에 명시한다.
- 마커와 GRF는 같은 차단주파수로 필터링한다.
  - 차단주파수가 다르면 충격 구간의 관절모멘트에 인위적인 최대값이 나타난다(Bisseling & Hof, 2006).
  - 방향 전환 동작에서 마커와 GRF를 다른 차단주파수로 처리하면 관절모멘트가 유의하게 달라졌고, 무릎 외전 모멘트 기준 피험자 순위도 바뀌었다(Kristianslund et al., 2012).
  - 후족 착지 러너 94명을 3.5 m/s에서 분석한 결과, 운동학 10 Hz와 GRF 100 Hz 조합에서 고관절 시상면 최대 모멘트가 평균 94% 변하였고 피험자 순위와 신발 효과 판정도 달라졌다. 저자들은 약 20 Hz의 같은 차단주파수를 권고하였다(Mai & Willwacher, 2019).
- 기준: 마커와 GRF 모두 **20 Hz**(Mai & Willwacher, 2019). 선행연구에는 두 신호 모두 10 Hz를 적용한 예도 있다(Fukuchi et al., 2017).
- 예비 자료로 잔차분석(residual analysis)을 실시해 20 Hz가 실험실 자료에 적절한지 확인한다(Winter, 2009). 결정한 값은 모든 피험자와 조건에 같게 적용한다.

### 7.2 GRF 변인 산출용 — 별도 처리

- 20 Hz로 필터링한 GRF는 고주파 성분이 제거되므로 충격 최대값과 부하율 산출에 쓰지 않는다. Mai & Willwacher(2019)도 낮은 차단주파수가 GRF의 생리적 고주파 성분을 지나치게 제거한다고 지적하였다.
- GRF 변인(충격 최대값, 부하율, 접지시간)은 원자료에서 별도로 처리한 GRF로 산출한다. 차단주파수 [확인 필요: 근거 문헌 확보 필요]

### 7.3 보고

- 필터 종류, 차수, 차단주파수, 결정 방법, 관절모멘트의 내적·외적 표기, 표현 좌표계, 정규화 방법을 보고한다(Derrick et al., 2020).

## 8. 이벤트 검출

### 8.1 지면반력 기준

- 착지(initial contact: IC)와 이지(toe-off: TO)는 수직 GRF가 역치를 넘는 시점과 역치 아래로 내려가는 시점으로 정한다.
- 지면반력 트레드밀 러닝 연구는 20 N 역치를 사용하였다(Fukuchi et al., 2017).
- 기준: 20 N. §1의 무부하 노이즈 최대 진폭이 20 N에 가까우면 역치를 올린다 [실험실 결정]. 사용한 역치는 trial log에 기록한다.
- 역치 판정에는 §7.2의 GRF를 사용한다.

### 8.2 벨트 구성별 처리

- 러닝에는 양발이 모두 떨어진 체공기가 있으므로 단일 벨트에서도 접지가 발마다 분리된다. 좌우 구분은 접지 구간에서 종골 마커의 좌우 위치로 판정한다.
- 좌우 분리 벨트: 한 발이 두 벨트를 동시에 밟은 스텝은 제외한다. 4 mm 간격의 분리 벨트 보행에서는 보폭 너비가 3.7 cm 넓어졌다(Altman, Reisman, Higginson, & Davis, 2012). 이 연구는 보행 자료이므로 러닝에서는 보폭 너비를 별도로 확인한다 [확인 필요].

### 8.3 운동학 백업

- GRF 이벤트를 얻지 못한 스텝에는 운동학 알고리즘을 적용한다. 러닝에서는 종골 또는 제1 중족골 마커의 수직 가속도 최대값 중 먼저 나타난 시점을 착지로, 무지 마커의 수직 jerk 최대값을 이지로 정한 방법의 오차가 가장 작았다(Handsaker, Forrester, Folland, Black, & Allen, 2016).
- Zeni, Richards, & Higginson(2008)의 알고리즘은 보행용이므로 러닝에 적용하지 않는다.
- 운동학 이벤트를 사용한 스텝 수를 결과에 보고한다.

## 9. 스트라이드 추출

| 문헌 | 맥락 | 결과 |
| --- | --- | --- |
| Riazati, Caplan, & Hayes (2019) | 트레드밀, 클럽 러너, 고강도 인터벌과 중강도 지속주 | 하지 3개 관절 3개 평면의 최대 각도, 착지 시 각도, 가동범위와 시공간 변인은 연속 20 strides에서 95% 신뢰 수준으로 안정되었다. 필요 스트라이드 수는 속도와 기록 시점의 영향을 받지 않았다 |
| Oliveira & Pirscoveanu (2021) | 지상 러닝, 44명 | 10 steps 이하로는 연구 표본의 35%만 평균 안정성에 도달하였다. 운동역학 변인을 포함한 분석에 피험자 25명 이상, 피험자당 25 steps 이상을 권고하였다 |

- 기준: 피험자·조건별로 **좌우 각 25 steps**를 30 s 기록 구간에서 연속으로 추출한다(Oliveira & Pirscoveanu, 2021). 운동학만 분석하면 연속 20 strides(Riazati et al., 2019)로 충족된다.
- 제외 기준 [실험실 결정]
  - 보간하지 못한 마커 결측이 있는 스텝
  - 분리 벨트에서 두 벨트를 밟은 스텝
  - 접지시간이 해당 시행 평균 ± 3 SD를 벗어난 스텝
- 제외 후 25 steps를 채우지 못하면 시행을 다시 수행하고, 재측정이 불가능하면 확보한 스텝 수를 결과에 보고한다.

## 10. 변인 선정 — 최대값 중심

### 10.1 시공간 변인

| 변인 | 정의 | 단위 |
| --- | --- | --- |
| 접지시간 | IC → TO | ms |
| 체공시간 | TO → 반대발 IC | ms |
| 케이던스 | 분당 스텝 수 | steps/min |
| 스텝 길이 | 벨트 속도 × 스텝 시간 | m |
| 착지 시 발-지면 각도 | IC 시점 발 분절의 시상면 각도(Altman & Davis, 2012) | ° |

### 10.2 지면반력 변인 (§7.2 GRF 사용, 체중 정규화: BW)

| 변인 | 정의 | 비고 |
| --- | --- | --- |
| 충격 최대값(impact peak) | 입각 초기 수직 GRF 첫 최대값 | 후족 착지에서 뚜렷하며 전족 착지에는 나타나지 않을 수 있다 |
| 능동 최대값(active peak) | 입각 중기 수직 GRF 최대값 | — |
| 수직 평균 부하율(VALR) | 구간 내 수직 GRF 기울기의 평균 | 구간 정의 3가지(Ueda et al., 2016): ① IC → 첫 최대값, ② IC → 첫 최대값 시간의 20~80% 구간, ③ IC 후 50 ms |
| 수직 순간 부하율(VILR) | 같은 구간 내 기울기의 최대값 | VALR은 구간 정의에 따라 유의하게 달랐으나 VILR은 차이가 없었다(Ueda et al., 2016). 연구 간 비교에는 VILR을 우선한다 |
| 제동 최대값 | 전후 GRF 음의 최대값 | — |
| 추진 최대값 | 전후 GRF 양의 최대값 | 트레드밀에서 지상보다 낮게 보고되었다(Van Hooren et al., 2020) |

- 충격 최대값이 없는 스텝에는 구간 ①, ②를 정의할 수 없으므로 착지 패턴이 섞인 표본에서는 구간 ③을 쓴다.

### 10.3 관절 운동학 (고관절·무릎·발목, 3개 평면)

- 착지 시 각도, 입각기 최대 각도, 입각기 가동범위. 세 변인 모두 연속 20 strides에서 안정되었다(Riazati et al., 2019).

### 10.4 관절 운동역학 (§7.1 자료 사용)

- 입각기 최대 내적 관절모멘트(N·m/kg), 최대 관절 파워(W/kg). 선행연구는 관절모멘트와 GRF를 체질량으로 정규화하였다(Fukuchi et al., 2017).
- 관절모멘트의 표현 좌표계(관절 좌표계 또는 근위 분절 좌표계)와 내적·외적 표기를 명시한다(Derrick et al., 2020).

### 10.5 변인 수에 대한 주의

- 부상과의 관련성이 보고된 변인은 제한적이다.
  - 수직 부하율은 피로골절 이력군에서 대조군보다 높았으나, 충격 최대값과 능동 최대값은 차이가 없었다(van der Worp, Vrielink, & Bredeweg, 2016).
  - 피로골절 이력이 있는 여성 러너는 순간·평균 수직 부하율이 더 높았다(Milner, Ferber, Pollard, Hamill, & Davis, 2006).
  - 전향적 연구를 종합한 결과 생체역학 변인과 러닝 부상의 관련성은 근거가 적고 일관되지 않았으며, 여성 러너의 고관절 최대 내전각은 슬개대퇴통증·장경인대증후군과의 관련성에 관한 제한적인 근거가 있었다(Ceyssens, Vanelderen, Barton, Malliaras, & Dingenen, 2019).
- 위 표의 최대값을 모두 동일한 비중으로 검정하면 비교 횟수가 늘어난다. 연구가설과 연결된 1차 변인 2~3개를 사전에 정하고, 나머지는 탐색적 변인으로 구분해 보고한다 [확인 필요].

## 11. 처리 파이프라인

### 11.1 QTM 단계

| 단계 | 작업 | 기준 |
| --- | --- | --- |
| Q1 | 수집 | §2 파일명, trial log 작성 |
| Q2 | 자동 라벨링(AIM) | 첫 피험자의 정적·러닝 시행을 수동 라벨링해 AIM 모델 생성, 이후 피험자마다 모델 갱신 |
| Q3 | 라벨 점검 | 마커 뒤바뀜, 미라벨 궤적, 클러스터 마커 간 거리 변화 확인 |
| Q4 | 결측 보간 | 짧은 결측은 다항식(spline) 보간, 200 ms 이상 결측은 같은 클러스터의 다른 마커를 이용하는 relational 보간 |
| Q5 | 힘판 확인 | 힘판 할당, 좌표계 방향, 영점, COP 위치 |
| Q6 | 내보내기 | C3D(마커 + 아날로그 GRF) |

- Q4 근거: 휠체어 추진 시 상지 마커를 재구성한 연구에서 200 ms 이상의 결측은 국소 좌표계 기반 보간의 오차가 가장 작았고, 그보다 짧은 결측은 spline 보간이 우수하였다(Howarth & Callaghan, 2010). 이 연구는 러닝 자료가 아니므로 200 ms 기준은 실험실 운영 기준으로 쓴다 [실험실 결정]. 200 Hz에서 200 ms는 40 frames이다.
- 해부학 마커가 보간 불가능하거나 보간 구간이 입각기 이벤트와 겹치면 해당 스텝을 제외한다(§9).

### 11.2 Python 단계

| 단계 | 작업 | 기준·근거 |
| --- | --- | --- |
| P1 | C3D 읽기 | ezc3d(Michaud & Begon, 2021) |
| P2 | 단위·좌표계 정렬 | mm → m, 힘판 좌표계 → 전역 좌표계 |
| P3 | 필터 | 두 갈래: (a) 관절모멘트용 마커·GRF 20 Hz(§7.1), (b) GRF 변인용(§7.2) |
| P4 | 이벤트 | (b) GRF에 20 N 역치(§8) |
| P5 | 정적 시행 처리 | 분절 해부학 좌표계 정의. 고관절 중심은 Harrington et al.(2007) 회귀식, 무릎 관절 중심은 대퇴 내·외측상과 중점, 발목 관절 중심은 내·외측 복사 중점 |
| P6 | 동적 시행 분절 추적 | 클러스터 마커에 정적 시행의 해부학 좌표계를 최소제곱 강체 정합으로 대응 |
| P7 | 관절 각도 | 관절 좌표계(Grood & Suntay, 1983; Wu et al., 2002) |
| P8 | 역동역학 | 분절 관성 계수 de Leva(1996), 발 → 하퇴 → 대퇴 순서의 Newton-Euler 계산, GRF와 COP를 발 분절에 적용 |
| P9 | 시간 정규화 | 입각기 0~100%, 101 points(Fukuchi et al., 2017은 보행주기를 101 points로 정규화) |
| P10 | 변인 추출 | §10 변인을 스텝마다 산출 → 피험자·조건·좌우별 평균 |
| P11 | 품질 점검 | 피험자별 스텝 곡선 중첩 그림, 제외 스텝 목록, 운동학 이벤트 사용 스텝 수 |
| P12 | 출력 | long-format CSV → Update DB |

- P5 근거: Harrington et al.(2007)은 MRI로 확인한 고관절 중심과 기존 회귀식을 비교하였고, 성인에서 최대 절대오차가 31 mm였다. 새 회귀식의 예측 변인은 전후 방향 골반 깊이, 상하 방향 골반 폭과 다리 길이, 내외측 방향 골반 깊이와 골반 폭이다.
- 상용 소프트웨어를 쓰면 Visual3D(C-Motion)로 P3~P9를 대체할 수 있다. 선행연구는 Visual3D로 필터링과 관절 운동학·운동역학을 산출하였다(Fukuchi et al., 2017).

### 11.3 출력 형식 (P12)

| 열 | 예 |
| --- | --- |
| subject | S01 |
| date | 260518 |
| condition | v30 |
| side | L |
| step | 1~25 |
| variable | vilr |
| value | 숫자 |
| unit | BW/s |
| event_source | grf / kinematic |

---

## 참고문헌

<!-- 서양서 알파벳순. HTML 전문이 있으면 html read로 함께 표기 -->

- Altman, A. R., & Davis, I. S. (2012). A kinematic method for footstrike pattern detection in barefoot and shod runners. *Gait & Posture, 35*(2), 298–300. https://doi.org/10.1016/j.gaitpost.2011.09.104 — html read: https://pmc.ncbi.nlm.nih.gov/articles/PMC3278526/
- Altman, A. R., Reisman, D. S., Higginson, J. S., & Davis, I. S. (2012). Kinematic comparison of split-belt and single-belt treadmill walking and the effects of accommodation. *Gait & Posture, 35*(2), 287–291. https://doi.org/10.1016/j.gaitpost.2011.09.101 — html read: https://pmc.ncbi.nlm.nih.gov/articles/PMC3274623/
- Arnold, B. J. W., Weeks, B. K., & Horan, S. A. (2019). An examination of treadmill running familiarisation in barefoot and shod conditions in healthy men. *Journal of Sports Sciences, 37*(1), 5–12. https://doi.org/10.1080/02640414.2018.1479533
- Bisseling, R. W., & Hof, A. L. (2006). Handling of impact forces in inverse dynamics. *Journal of Biomechanics, 39*(13), 2438–2444. https://doi.org/10.1016/j.jbiomech.2005.07.021
- Bruening, D. A., Cooney, K. M., & Buczek, F. L. (2012). Analysis of a kinetic multi-segment foot model part II: Kinetics and clinical implications. *Gait & Posture, 35*(4), 535–540. https://doi.org/10.1016/j.gaitpost.2011.11.012
- Cappozzo, A., Catani, F., Della Croce, U., & Leardini, A. (1995). Position and orientation in space of bones during movement: Anatomical frame definition and determination. *Clinical Biomechanics, 10*(4), 171–178. https://doi.org/10.1016/0268-0033(95)91394-t
- Cappozzo, A., Della Croce, U., Leardini, A., & Chiari, L. (2005). Human movement analysis using stereophotogrammetry. Part 1: Theoretical background. *Gait & Posture, 21*(2), 186–196. https://doi.org/10.1016/j.gaitpost.2004.01.010
- Ceyssens, L., Vanelderen, R., Barton, C., Malliaras, P., & Dingenen, B. (2019). Biomechanical risk factors associated with running-related injuries: A systematic review. *Sports Medicine, 49*(7), 1095–1115. https://doi.org/10.1007/s40279-019-01110-z
- Collins, S. H., Adamczyk, P. G., Ferris, D. P., & Kuo, A. D. (2009). A simple method for calibrating force plates and force treadmills using an instrumented pole. *Gait & Posture, 29*(1), 59–64. https://doi.org/10.1016/j.gaitpost.2008.06.010 — html read: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665306/
- de Leva, P. (1996). Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. *Journal of Biomechanics, 29*(9), 1223–1230. https://doi.org/10.1016/0021-9290(95)00178-6
- Derrick, T. R., van den Bogert, A. J., Cereatti, A., Dumas, R., Fantozzi, S., & Leardini, A. (2020). ISB recommendations on the reporting of intersegmental forces and moments during human motion analysis. *Journal of Biomechanics, 99*, 109533. https://doi.org/10.1016/j.jbiomech.2019.109533
- Fukuchi, R. K., Fukuchi, C. A., & Duarte, M. (2017). A public dataset of running biomechanics and the effects of running speed on lower extremity kinematics and kinetics. *PeerJ, 5*, e3298. https://doi.org/10.7717/peerj.3298 — html read: https://pmc.ncbi.nlm.nih.gov/articles/PMC5426356/
- Grood, E. S., & Suntay, W. J. (1983). A joint coordinate system for the clinical description of three-dimensional motions: Application to the knee. *Journal of Biomechanical Engineering, 105*(2), 136–144. https://doi.org/10.1115/1.3138397
- Handsaker, J. C., Forrester, S. E., Folland, J. P., Black, M. I., & Allen, S. J. (2016). A kinematic algorithm to identify gait events during running at different speeds and with different footstrike types. *Journal of Biomechanics, 49*(16), 4128–4133. https://doi.org/10.1016/j.jbiomech.2016.10.013
- Harrington, M. E., Zavatsky, A. B., Lawson, S. E. M., Yuan, Z., & Theologis, T. N. (2007). Prediction of the hip joint centre in adults, children, and patients with cerebral palsy based on magnetic resonance imaging. *Journal of Biomechanics, 40*(3), 595–602. https://doi.org/10.1016/j.jbiomech.2006.02.003
- Howarth, S. J., & Callaghan, J. P. (2010). Quantitative assessment of the accuracy for three interpolation techniques in kinematic analysis of human movement. *Computer Methods in Biomechanics and Biomedical Engineering, 13*(6), 847–855. https://doi.org/10.1080/10255841003664701
- Huang, M., Mo, S., Chan, P. P.-K., Chan, Z. Y. S., Zhang-Lea, J. H., & Cheung, R. T. H. (2023). The influence of running shoes on familiarization time for treadmill running biomechanics evaluation. *Sports Biomechanics, 22*(3), 459–472. https://doi.org/10.1080/14763141.2022.2046144
- Kristianslund, E., Krosshaug, T., & van den Bogert, A. J. (2012). Effect of low pass filtering on joint moments from inverse dynamics: Implications for injury prevention. *Journal of Biomechanics, 45*(4), 666–671. https://doi.org/10.1016/j.jbiomech.2011.12.011
- Lavcanska, V., Taylor, N. F., & Schache, A. G. (2005). Familiarization to treadmill running in young unimpaired adults. *Human Movement Science, 24*(4), 544–557. https://doi.org/10.1016/j.humov.2005.08.001
- Mai, P., & Willwacher, S. (2019). Effects of low-pass filter combinations on lower extremity joint moments in distance running. *Journal of Biomechanics, 95*, 109311. https://doi.org/10.1016/j.jbiomech.2019.08.005
- Manal, K., McClay, I., Stanhope, S., Richards, J., & Galinat, B. (2000). Comparison of surface mounted markers and attachment methods in estimating tibial rotations during walking: An in vivo study. *Gait & Posture, 11*(1), 38–45. https://doi.org/10.1016/s0966-6362(99)00042-9
- Michaud, B., & Begon, M. (2021). ezc3d: An easy C3D file I/O cross-platform solution for C++, Python and MATLAB. *Journal of Open Source Software, 6*(58), 2911. https://doi.org/10.21105/joss.02911 — html read: https://joss.theoj.org/papers/10.21105/joss.02911
- Milner, C. E., Ferber, R., Pollard, C. D., Hamill, J., & Davis, I. S. (2006). Biomechanical factors associated with tibial stress fracture in female runners. *Medicine and Science in Sports and Exercise, 38*(2), 323–328. https://doi.org/10.1249/01.mss.0000183477.75808.92
- Oliveira, A. S., & Pirscoveanu, C. I. (2021). Implications of sample size and acquired number of steps to investigate running biomechanics. *Scientific Reports, 11*, 3083. https://doi.org/10.1038/s41598-021-82876-z — html read: https://pmc.ncbi.nlm.nih.gov/articles/PMC7862397/
- Riazati, S., Caplan, N., & Hayes, P. R. (2019). The number of strides required for treadmill running gait analysis is unaffected by either speed or run duration. *Journal of Biomechanics, 97*, 109366. https://doi.org/10.1016/j.jbiomech.2019.109366
- Riley, P. O., Dicharry, J., Franz, J., Della Croce, U., Wilder, R. P., & Kerrigan, D. C. (2008). A kinematics and kinetic comparison of overground and treadmill running. *Medicine and Science in Sports and Exercise, 40*(6), 1093–1100. https://doi.org/10.1249/MSS.0b013e3181677530
- Ueda, T., Hobara, H., Kobayashi, Y., Heldoorn, T. A., Mochimaru, M., & Mizoguchi, H. (2016). Comparison of 3 methods for computing loading rate during running. *International Journal of Sports Medicine, 37*(13), 1087–1090. https://doi.org/10.1055/s-0042-107248
- van der Worp, H., Vrielink, J. W., & Bredeweg, S. W. (2016). Do runners who suffer injuries have higher vertical ground reaction forces than those who remain injury-free? A systematic review and meta-analysis. *British Journal of Sports Medicine, 50*(8), 450–457. https://doi.org/10.1136/bjsports-2015-094924
- Van Hooren, B., Fuller, J. T., Buckley, J. D., Miller, J. R., Sewell, K., Rao, G., Barton, C., Bishop, C., & Willy, R. W. (2020). Is motorized treadmill running biomechanically comparable to overground running? A systematic review and meta-analysis of cross-over studies. *Sports Medicine, 50*(4), 785–813. https://doi.org/10.1007/s40279-019-01237-z — html read: https://pmc.ncbi.nlm.nih.gov/articles/PMC7069922/
- Willems, P. A., & Gosseye, T. P. (2013). Does an instrumented treadmill correctly measure the ground reaction forces? *Biology Open, 2*(12), 1421–1424. https://doi.org/10.1242/bio.20136379 — html read: https://pmc.ncbi.nlm.nih.gov/articles/PMC3863428/
- Winter, D. A. (2009). *Biomechanics and motor control of human movement* (4th ed.). John Wiley & Sons. — 검색: https://www.google.com/search?q=Biomechanics+and+Motor+Control+of+Human+Movement+Winter+4th+edition
- Wu, G., Siegler, S., Allard, P., Kirtley, C., Leardini, A., Rosenbaum, D., Whittle, M., D'Lima, D. D., Cristofolini, L., Witte, H., Schmid, O., & Stokes, I. (2002). ISB recommendation on definitions of joint coordinate system of various joints for the reporting of human joint motion—part I: Ankle, hip, and spine. *Journal of Biomechanics, 35*(4), 543–548. https://doi.org/10.1016/s0021-9290(01)00222-6
- Wu, G., van der Helm, F. C. T., Veeger, H. E. J., Makhsous, M., Van Roy, P., Anglin, C., Nagels, J., Karduna, A. R., McQuade, K., Wang, X., Werner, F. W., & Buchholz, B. (2005). ISB recommendation on definitions of joint coordinate systems of various joints for the reporting of human joint motion—Part II: Shoulder, elbow, wrist and hand. *Journal of Biomechanics, 38*(5), 981–992. https://doi.org/10.1016/j.jbiomech.2004.05.042
- Zeni, J. A., Richards, J. G., & Higginson, J. S. (2008). Two simple methods for determining gait events during treadmill and overground walking using kinematic data. *Gait & Posture, 27*(4), 710–714. https://doi.org/10.1016/j.gaitpost.2007.07.007 — html read: https://pmc.ncbi.nlm.nih.gov/articles/PMC2384115/

---

Update DB
커스텀 코드 (옵션) ; python
코드 제작 (DB); python

Visualization
시각화 (web base); react + typescript + js + html + css
