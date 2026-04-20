# Sổ Tay Vận Hành

Bản tiếng Anh: `OPERATIONS_MANUAL.md`

File này là manual tổng cho `agent-skills-unified`.

Nếu cần bắt đầu nhanh, đọc `HUONG_DAN_SU_DUNG.md`.
Nếu cần hiểu đầy đủ cách bộ này vận hành, được mở rộng, được harden, và được bảo trì, đọc file này.

## 1. Mục Tiêu

Bộ này không phải chỉ là một thư viện skill.

Nó là một hệ vận hành cho AI agent:

- biết nên đọc gì trước
- biết chọn skill nào đúng
- biết khi nào cần ghép nhiều skill
- biết cách verify trước khi chốt
- biết cách nâng cấp bundle mà không làm nó rơi vào tình trạng tạp nham, mơ hồ, hoặc khó trigger

### 1.1 Operating Charter

Bộ này được huấn luyện để vận hành như một team senior:

- frame đúng bài toán
- tách scope và risk
- chọn architecture và workflow phù hợp
- làm trên branch/worktree khi cần
- verify bằng bằng chứng
- handoff rõ ràng cho người hoặc AI khác

Nếu gặp ý tưởng quá lớn hoặc tham vọng, không được giả vờ như đã sẵn sàng production.

Phải tách:

- concept
- prototype
- simulator
- production
- verification và operations

### 1.2 Boundary An Toàn

Bộ này không được dùng để hỗ trợ:

- weapon guidance, targeting, kill-chain
- malware, credential theft, unauthorized access, exfiltration
- giám sát con người không đồng ý
- lời hứa trading "luôn thắng"
- fake verification, fake benchmark, fake readiness

Nếu request chạm vào vùng này, phải pivot sang hướng hợp pháp và an toàn hơn:

- simulation
- telemetry
- verification harness
- safety analysis
- risk dashboard

## 2. Tư Duy Nên Dùng

Hãy nhìn bundle này theo 4 lớp:

1. `workspace-operating-system`
   - lớp điều phối trung tâm
2. `skills/`
   - tri thức và workflow theo domain
3. `agents/`
   - prompt chuyên gia theo vai trò
4. `workflows/`
   - điểm vào theo kiểu command/procedure

Thêm vào đó:

- `rules/`
  - ràng buộc toàn cục
- `scripts/`
  - helper và validator
- `.shared/`
  - tài nguyên dùng chung

## 3. Cấu Trúc Chuẩn

Root repo:

- `README.md`
  - giải thích repo là gì
- `HUONG_DAN_SU_DUNG.md`
  - quick start
- `SO_TAY_VAN_HANH.md`
  - manual tổng
- `BAO_CAO_HARDENING.md`
  - lịch sử và nguyên tắc làm sạch/hardening

Runtime tree:

- `.agent/skills/`
  - thư viện skill canonical duy nhất
- `.agent/agents/`
  - 20 agent prompts
- `.agent/workflows/`
  - 11 workflow entry points
- `.agent/rules/`
  - 1 global rule file
- `.agent/scripts/`
  - helper/validation scripts
- `.agent/.shared/`
  - shared assets

Tình trạng hiện tại:

- `55` skills
- `20` agents
- `11` workflows
- `1` rules file

## 4. Thứ Tự AI Nên Đọc Khi Vào Repo

Đây là trình tự để một AI mới vào repo và vận hành đúng:

1. Đọc `.agent/skills/workspace-operating-system/SKILL.md`
2. Đọc:
   - `.agent/skills/workspace-operating-system/references/task-routing.md`
   - `.agent/skills/workspace-operating-system/references/quality-bar.md`
   - `.agent/skills/workspace-operating-system/references/operating-charter.md`
   - nếu task là idea/pitch tham vọng: `idea-to-program-playbook.md`
   - nếu task cần vận hành như một team: `department-operating-model.md`
3. Nếu task là code, infra, release, hoặc deployment:
   - đọc thêm `branch-and-release-policy.md`
4. Nếu task nhiều domain:
   - đọc thêm `composition-patterns.md`
5. Nếu chưa chắc skill nào:
   - đọc `skill-catalog.md`
6. Sau đó mới đọc `SKILL.md` của skill chính
7. Chỉ đọc `references/` khi thực sự cần
8. Nếu task cần role chuyên biệt:
   - đọc agent phù hợp trong `.agent/agents/`
9. Nếu task theo kiểu command/process có sẵn:
   - đọc workflow phù hợp trong `.agent/workflows/`

Nguyên tắc:

- đi từ tổng quan -> route -> skill chính -> reference sau
- không đọc lần từng folder một cách mù quáng
- không load hết context nếu task không cần
- task code nghiêm túc thì luôn nghĩ theo branch/review/release path

## 5. Entry Point Chuẩn

Mặc định, câu mở đầu tốt nhất là:

```text
Use $workspace-operating-system to decide the right skill stack, sequence the work, and verify the result.
```

Dùng entry này khi:

- task mơ hồ
- task lớn
- task nhiều domain
- task có giá trị cao
- task cần quality bar rõ ràng

## 6. Cách Route Task

### 6.1 Task mở rộng ứng dụng

Dùng:

- `app-builder`
- support: `architecture`, `frontend-design`, `api-patterns`, `database-design`, `deployment-procedures`, `closed-loop-delivery`

### 6.2 Task kiến trúc

Dùng:

- `architecture`

### 6.2b Task hệ thống lớn, mission software, simulation

Dùng:

- `systems-engineering`

Đọc thêm:

- `references/mission-software-playbook.md`
- `references/simulation-first-delivery.md`
- `references/interface-control-checklist.md`
- `references/decision-playbook.md`
- `references/adr-checklist.md`

### 6.3 Task API

Dùng:

- `api-patterns`

Đọc thêm:

- `references/contract-playbook.md`
- `references/api-review-checklist.md`

### 6.4 Task UI/frontend

Dùng:

- `frontend-design`
- support tùy task: `web-design-guidelines`, `tailwind-patterns`, `nextjs-react-expert`, `mobile-design`

### 6.5 Task debug

Dùng:

- `systematic-debugging`
- support: domain skill liên quan
- verify thêm bằng `webapp-testing` hoặc `testing-patterns`

### 6.6 Task cần hoàn tất thật sự

Dùng:

- `closed-loop-delivery`
- support:
  - `verification-before-completion`
  - `receiving-code-review`
  - `webapp-testing`

### 6.7 Task đã có plan

Dùng:

- `executing-plans`
- support:
  - `using-git-worktrees`
  - `parallel-agents`
  - `verification-before-completion`

### 6.8 Task review feedback

Dùng:

- `receiving-code-review`

Khác với:

- `code-review-checklist`
  - dùng khi chính mình đi review code

### 6.9 Task hiệu năng React/Next.js

Dùng:

- `nextjs-react-expert`

Đọc thêm:

- `references/performance-investigation-playbook.md`
- `references/app-router-checklist.md`

## 7. Nguyên Tắc Thiết Kế Skill

Bộ này đang theo một rule rất quan trọng:

- `SKILL.md` phải gọn, rõ trigger, rõ workflow
- tri thức sâu đưa xuống `references/`

Lý do:

- `SKILL.md` quá dài sẽ trigger kém
- AI cần một lớp điều phối gọn để load nhanh
- tri thức senior-grade nên được lưu thành playbook/checklist/matrix ở `references/`

Mẫu lý tưởng của một skill:

- `SKILL.md`
  - khi nào dùng
  - quy trình chính
  - related skills
- `references/`
  - playbook
  - decision matrix
  - review checklist
  - advanced heuristics
- `agents/openai.yaml`
  - metadata để discover/invoke đẹp hơn

## 8. Catalog Skill Chính

Để xem đầy đủ tất cả skill:

- `.agent/skills/workspace-operating-system/references/skill-catalog.md`

Nhóm skill quan trọng nhất:

- Operating:
  - `workspace-operating-system`
  - `closed-loop-delivery`
  - `executing-plans`
  - `parallel-agents`
  - `plan-writing`
  - `verification-before-completion`
  - `using-git-worktrees`
  - `finishing-a-development-branch`
- Product and architecture:
  - `app-builder`
  - `architecture`
  - `systems-engineering`
  - `api-patterns`
  - `database-design`
  - `mcp-builder`
- Frontend:
  - `frontend-design`
  - `web-design-guidelines`
  - `tailwind-patterns`
  - `nextjs-react-expert`
  - `mobile-design`
- Quality:
  - `systematic-debugging`
  - `testing-patterns`
  - `tdd-workflow`
  - `webapp-testing`
  - `receiving-code-review`
  - `code-review-checklist`

## 9. Catalog Agent

Đây là 20 agent hiện có trong `.agent/agents/`:

- `backend-specialist`
  - backend, server, API, auth, database integration
- `code-archaeologist`
  - legacy code, repo analysis, modernization
- `database-architect`
  - schema, migrations, indexing, data modeling
- `debugger`
  - root cause, crash investigation, production issue
- `devops-engineer`
  - deployment, rollback, CI/CD, server operations
- `documentation-writer`
  - docs khi user yêu cầu rõ ràng
- `explorer-agent`
  - deep codebase discovery
- `frontend-specialist`
  - React/Next.js UI architecture
- `game-developer`
  - game logic và engines
- `mobile-developer`
  - React Native, Flutter, mobile patterns
- `orchestrator`
  - điều phối nhiều agent
- `penetration-tester`
  - offensive security
- `performance-optimizer`
  - profiling, speed, bundle
- `product-manager`
  - requirements, acceptance criteria
- `product-owner`
  - backlog, MVP, strategic prioritization
- `project-planner`
  - planning và breakdown
- `qa-automation-engineer`
  - e2e, regression, automation infra
- `security-auditor`
  - OWASP, auth, supply chain, security review
- `seo-specialist`
  - SEO và GEO
- `test-engineer`
  - tests, TDD, coverage

Nguyên tắc dùng agent:

- dùng agent khi role thực sự quan trọng với task
- không thay agent cho skill; agent và skill là 2 lớp khác nhau
- skill lo tri thức/quy trình
- agent lo góc nhìn và vai trò

## 10. Catalog Workflow

11 workflow hiện có trong `.agent/workflows/`:

- `brainstorm.md`
  - structured brainstorming
- `create.md`
  - tạo ứng dụng mới
- `debug.md`
  - điều tra lỗi có hệ thống
- `deploy.md`
  - deployment flow
- `enhance.md`
  - nâng cấp feature hiện có
- `orchestrate.md`
  - điều phối nhiều agent
- `plan.md`
  - lập kế hoạch
- `preview.md`
  - quản lý preview/local server
- `status.md`
  - theo dõi trạng thái
- `test.md`
  - sinh/chạy tests
- `ui-ux-pro-max.md`
  - luồng thao tác UI

Lưu ý:

- workflows là điểm vào theo process
- skills vẫn là lớp tri thức canonical
- nếu workflow cũ/legacy xung đột với `workspace-operating-system`, ưu tiên routing từ skill trung tâm

## 11. Rules

Hiện tại có 1 global rule file:

- `.agent/rules/GEMINI.md`

Vai trò của nó:

- giữ compatibility với một số hệ cũ
- mô tả framework-style behavior rộng

Nhưng cần hiểu rõ:

- runtime canonical hiện tại vẫn nên bắt đầu từ `workspace-operating-system`
- `GEMINI.md` là file inherited legacy, không nên tiếp tục phình to nó
- rule mới nên ngắn, rõ, và tối giản

Khuyến nghị:

- để `rules/` cho ràng buộc thật sự toàn cục
- để logic route/execution ở `skills/workspace-operating-system`
- để domain knowledge ở `skills/*`

## 12. Rule Ưu Tiên

Trong repo này, nên nghĩ theo thứ tự:

1. user request
2. `workspace-operating-system`
3. skill chính của task
4. reference của skill đó
5. agent role nếu có dùng agent
6. workflow nếu task vào theo workflow
7. global rules để giữ compatibility

Nguyên tắc đơn giản:

- rule nào cụ thể hơn và gần task hơn thì ưu tiên để làm việc
- rule nào cũ/legacy mà mâu thuẫn với hệ canonical mới thì phải review cẩn thận

## 13. Prompt Mẫu Cho Human

### Route tổng quát

```text
Use $workspace-operating-system to route this task, choose the minimum effective skill stack, and verify the result.
```

### Build app

```text
Use $app-builder to shape this product request, choose the stack, and plan the next implementation steps.
```

### Architecture

```text
Use $architecture to compare realistic system options and recommend the best architecture with tradeoffs.
```

### API

```text
Use $api-patterns to design the API style, response contract, auth, and versioning for this system.
```

### End-to-end delivery

```text
Use $closed-loop-delivery to finish this task end to end and prove the acceptance criteria.
```

### Review feedback

```text
Use $receiving-code-review to process these review comments, apply valid fixes, and verify them.
```

### Performance

```text
Use $nextjs-react-expert to find the main bottleneck and optimize this React or Next.js flow deliberately.
```

## 14. Các Quy Trình Vàng

### 14.1 Build feature lớn

Trình tự nên dùng:

1. `workspace-operating-system`
2. `app-builder`, `architecture`, hoặc `systems-engineering`
3. `plan-writing`
4. `executing-plans`
5. domain skills
6. `verification-before-completion`
7. `finishing-a-development-branch`

### 14.2 Sửa bug khó

1. `workspace-operating-system`
2. `systematic-debugging`
3. domain skill liên quan
4. `testing-patterns` hoặc `webapp-testing`
5. `verification-before-completion`

### 14.3 Xử lý review feedback

1. `receiving-code-review`
2. domain skill
3. `verification-before-completion`
4. nếu cần hoàn tất thật sự -> `closed-loop-delivery`

### 14.4 Performance pass

1. `nextjs-react-expert`
2. `performance-profiling`
3. `frontend-design` nếu có tác động UX
4. `verification-before-completion`

## 15. Cách Thêm Skill Mới

Khi thêm skill mới:

1. Tạo folder trong `.agent/skills/<skill-name>/`
2. Tạo `SKILL.md`
3. Nếu cần tri thức sâu:
   - tạo `references/`
4. Nếu cần metadata đẹp:
   - tạo `agents/openai.yaml`
5. Nếu cần helper repeatable:
   - tạo `scripts/`
6. Chạy lại:

```text
python .agent/skills/workspace-operating-system/scripts/build_skill_catalog.py
```

Checklist trước khi commit:

- tên folder và `name:` trong frontmatter phải khớp
- `description:` phải nói rõ khi nào dùng
- tất cả reference trong `SKILL.md` phải tồn tại
- không nhắc file/đường dẫn hệ cũ sai context
- không import launcher/app shell lạ vào cây runtime
- với hệ thống lớn, phải nói rõ đâu là concept, đâu là simulator, đâu là prototype, và đâu là production claim

## 16. Cách Nâng Cấp Skill Cũ

Khi một skill cũ quá rộng, mơ hồ, hoặc mang dấu vết inherited source:

1. Rút gọn `SKILL.md`
2. Làm rõ:
   - khi nào dùng
   - quy trình chính
   - related skills
3. Chuyển tri thức sâu xuống `references/`
4. Thêm checklist/playbook senior-grade
5. Thêm `agents/openai.yaml` nếu skill quan trọng
6. Rebuild catalog

Đây là cách bundle này đã được nâng cấp.

## 17. Cách Bảo Trì Agent

Khi sửa `agents/*.md`:

- mô tả rõ role
- giải thích khi nào nên dùng
- không để agent trở thành bản sao của skill
- để skill cung cấp tri thức
- để agent cung cấp góc nhìn, tone, và vùng trách nhiệm

Agent tốt nên:

- có description rõ trigger
- biết nó dùng skill nào
- không nói quá nhiều về framework cũ nếu runtime đã đổi

## 18. Cách Bảo Trì Workflow

Khi sửa `workflows/*.md`:

- xem nó là entry procedure, không phải skill thay thế
- giữ command flow rõ
- nếu logic đã được skill trung tâm quản lý tốt hơn, workflow nên đơn giản hóa
- tránh để workflow override triết lý canonical mới mà không có lý do

## 19. Hardening Và Ownership

Nguyên tắc đang dùng:

- local-first
- không bật sẵn MCP ngoài
- không ship file nhạy cảm
- không import raw launcher/app shell từ bundle ngoài vào `.agent`
- không để workflow khuyến khích direct-to-main khi repo chưa cho phép
- khi gộp bundle ngoài vào:
  - audit
  - lọc
  - viết lại/cherry-pick
  - không merge nguyên cây runtime của nó vào canonical tree

Xem thêm:

- `BAO_CAO_HARDENING.md`

## 20. Release Checklist

Trước khi push:

1. cập nhật file cần thiết
2. rebuild catalog nếu inventory/description đổi
3. kiểm tra reference link không gãy
4. chạy:

```text
git diff --check
```

5. đọc lại:
   - `README.md`
   - `HUONG_DAN_SU_DUNG.md`
   - `SO_TAY_VAN_HANH.md`
   nếu thay đổi tác động đến cách dùng
6. commit rõ nghĩa
7. push branch đang làm việc
8. mở hoặc chuẩn bị PR
9. merge vào `dev`/`test`/staging theo flow của repo nếu có
10. chỉ merge vào `main`/`master` sau khi đã qua gate verify và được phê duyệt

## 21. Dấu Hiệu Hệ Đang Xấu Đi

Cần cảnh giác nếu thấy:

- skill tên một đằng, folder một nẻo
- `SKILL.md` phình to và lặp ý
- nhiều skill trigger trùng nhau
- reference không tồn tại
- inherited wording cũ xuất hiện ở core skill
- workflow/agent/rule nói ngược với canonical flow
- catalog không rebuild sau khi sửa frontmatter

## 22. Quy Tắc Vàng Cuối Cùng

Bộ này hướng tới chuẩn:

- rõ trigger
- giàu tri thức
- ít mơ hồ
- quality bar rõ
- verification trước khi chốt
- phong cách senior dev thực thụ

Nếu phải chọn giữa:

- dài nhưng mơ hồ
- và
- gọn nhưng rõ + có reference sâu

thì chọn vế sau.
