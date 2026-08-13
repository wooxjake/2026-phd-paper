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

