# GitHub Copilot 지침 — PhD 논문 (Sitting Biomechanics / Kinesiology)

이 저장소는 **GitHub Copilot(주)** 과 **Claude Code(보조)** 를 함께 사용한다.

규칙 본문은 아래 파일들에 한 벌만 존재한다. 이 문서는 진입점이며, 규칙 내용을 여기에 복사해 두지 않는다. 규칙을 바꿀 때는 아래 원본 파일만 수정한다.

## 규칙 출처 (작업 전 반드시 읽는다)

| 파일 | 적용 시점 |
| --- | --- |
| `.github/agents/phd-thesis-writer.agent.md` | 논문 작성·수정·검토 전반 (규칙 전문) |
| `policy/korean-academic-style.md` | 한국어 초안 작성 및 문체 수정 전 |
| `etc/han/analysis.md` | 문체 근거와 문장 템플릿이 필요할 때 |
| `references/번역_가이드라인.md` | 논문 번역본 작성·수정 전 |
| `CLAUDE.md` | 프로젝트 개요, 파일 구조, references.md 필수 기재 항목 |

## 수정 승인

에이전트를 지정하지 않은 채 Chat을 열어도 이 규칙은 적용된다.

- 현재 사용자 메시지의 첫 단어가 대소문자와 관계없이 `edit`일 때만 파일 생성·수정·이름 변경·이동·삭제를 실행한다.
- `edit`으로 시작하지 않으면 읽기·분석·제안만 하고, `이 작업을 실행하려면 메시지를 edit으로 시작해주세요.`라고 안내한 뒤 대기한다.
- 승인은 현재 메시지에만 적용된다. 이전 메시지의 `edit`을 근거로 삼지 않는다.

## 에이전트 역할 분담

| 에이전트 | 담당 |
| --- | --- |
| **Copilot (주)** | 본문 초안 작성·수정 — `introduce.md`, `methods.md`, 이후 추가될 결과·논의 섹션 |
| **Claude Code (보조)** | 검증·대조 — 인용 정합성, 문체 점검, `references.md` 대조, 스크립트 작성, git 정리 |

- 같은 파일을 두 에이전트가 동시에 편집하지 않는다.
- 에이전트를 전환하기 전에 커밋해 체크포인트를 남긴다.

## 근거 사용

- `search1.md`, `search2.md`, `search3.md`는 외부에서 불러온 AI 리서치 산출물이다. **탐색 단서일 뿐 근거가 아니다.** 내부의 `[cite: n]` 마커는 원문 추적이 불가능하다.
- 이 문서들의 내용은 원문 PDF 또는 확보된 텍스트로 확인한 뒤에만 본문 근거로 사용하고, `references.md`에 등록한다.
- 나머지 근거 규칙(지어내지 않기, `[CITE?]`, `[확인 필요]` 사용)은 `.github/agents/phd-thesis-writer.agent.md`를 따른다.
