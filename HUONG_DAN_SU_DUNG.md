# Hướng Dẫn Sử Dụng

Bản tiếng Anh: `USAGE_GUIDE.md`

File này là điểm vào nhanh để dùng bộ `agent-skills-unified` mà không cần đọc toàn bộ repo.

## Mục Tiêu

Bộ này được làm để cả người và AI khác có thể vào repo, hiểu nên đọc gì trước, chọn đúng skill, làm đúng thứ tự, và tự kiểm tra chất lượng trước khi kết thúc.

## Cách Dùng Nhanh Nhất

Nếu không chắc nên dùng skill nào, hãy bắt đầu bằng:

```text
Use $workspace-operating-system to decide the right skill stack for this task.
```

Đây là skill trung tâm. Nó giúp:

- phân loại task
- chọn skill chính và skill phụ
- quyết định thứ tự làm việc
- nhắc AI phải verify trước khi chốt
- ép task code đi theo branch-first, review-first, release-aware flow
- giữ ranh giới an toàn và hợp pháp cho những bài toán nhạy cảm

## Khi Nào Dùng Skill Trung Tâm

Hãy bắt đầu bằng `$workspace-operating-system` khi:

- task còn mơ hồ
- task lớn hoặc nhiều bước
- task đụng nhiều domain cùng lúc
- bạn muốn AI tự chọn quy trình làm việc tốt nhất
- bạn muốn AI giải thích vì sao nó chọn skill đó

## Nếu Ý Tưởng Rất Lớn Hoặc Rất Xa

Vẫn dùng được, nhưng hãy để AI xử lý theo cách senior:

- tách concept, prototype, simulator, và production
- viết requirement, risk register, và verification plan trước
- build theo từng slice có thể kiểm chứng

Bộ này có thể giúp rất mạnh cho:

- mission software
- telemetry
- digital twin
- simulation
- control-plane và observability

Nếu ý tưởng thuộc nhóm hệ thống lớn, hãy gọi thẳng:

```text
Use $systems-engineering to turn this system idea into a mission brief, subsystem map, simulation-first plan, and first verifiable software slice.
```

Nhưng không được dùng để hỗ trợ:

- vũ khí, tên lửa, guidance targeting
- malware, đọc dữ liệu trái phép, exfiltration
- giám sát con người không đồng ý
- lời hứa "chơi chứng khoán luôn thắng"

## Khi Nào Gọi Thẳng Skill Chuyên Biệt

Gọi trực tiếp skill khi bạn đã biết rõ việc cần làm.

Ví dụ:

- UI, landing page, component:
```text
Use $frontend-design to redesign this page and keep the UX clear.
```

- test trình duyệt, kiểm tra flow web:
```text
Use $webapp-testing to inspect the app and verify the main user flow.
```

- tạo MCP server:
```text
Use $mcp-builder to design and implement an MCP server for this API.
```

- thiết kế API:
```text
Use $api-patterns to design this endpoint and response format.
```

- schema database:
```text
Use $database-design to propose the schema and indexing strategy.
```

- debug:
```text
Use $systematic-debugging to find the root cause of this issue.
```

- có sẵn plan và muốn AI thi công theo đúng trình tự:
```text
Use $executing-plans to follow this plan step by step and verify each stage.
```

- muốn AI làm đến nơi đến chốn, có acceptance criteria rõ:
```text
Use $closed-loop-delivery to finish this task end to end and prove the result.
```

- đang xử lý review comments:
```text
Use $receiving-code-review to triage these comments, fix valid issues, and verify them.
```

- review code:
```text
Use $code-review-checklist to review these changes for bugs and risks.
```

## Quy Tắc Thực Chiến

1. Không chắc thì bắt đầu bằng `$workspace-operating-system`.
2. Chắc domain rồi thì gọi thẳng skill chính.
3. Task lớn thì để AI ghép nhiều skill theo thứ tự.
4. Task code thì luôn yêu cầu verify hoặc test sau khi sửa.
5. Task review thì ưu tiên bug, regression, missing test trước phần style.
6. Nếu task đã có plan, dùng `$executing-plans` thay vì để AI vừa nghĩ vừa chế lại kế hoạch.
7. Nếu task cần hoàn tất thật sự, dùng thêm `$verification-before-completion` hoặc gọi thẳng `$closed-loop-delivery`.
8. Task code không nhỏ thì nên làm trên branch hoặc worktree riêng.
9. Trước khi merge hay deploy, AI phải nói rõ nó đang ở branch nào, đã verify gì, và đề xuất next step nào.
10. Task nguy cơ cao thì AI phải nói rõ đâu là prototype, đâu là simulation, đâu là production claim.

## Quy Trình Khuyên Dùng

### 1. Task mới hoặc nhiều domain

```text
Use $workspace-operating-system to choose the right skills and execution order for building this feature.
```

### 2. Task UI

```text
Use $frontend-design to define the visual direction, hierarchy, and implementation approach for this interface.
```

### 3. Task bug

```text
Use $workspace-operating-system to route this bug, then use the right debugging and verification skills.
```

### 4. Task review feedback

```text
Use $receiving-code-review to process these review comments, apply valid fixes, and verify them.
```

### 5. Task review

```text
Use $workspace-operating-system to choose the right review stack, then review this code with a risk-first mindset.
```

### 6. Task thi công theo plan

```text
Use $executing-plans to implement this approved plan without drifting from scope.
```

### 7. Task cần chốt đến nơi đến chốn

```text
Use $closed-loop-delivery to finish this task end to end and only stop when the acceptance criteria are proven.
```

### 8. Task tài liệu, brief, hoặc nội dung cần trình bày rõ

Gọi theo hướng viết và điều phối nội dung:

- `$doc-coauthoring`
- `$internal-comms`
- thêm `$brand-guidelines` nếu cần chuẩn hóa giọng thương hiệu

## Cấu Trúc Cần Biết

- `.agent/skills/`
  - thư viện skill chính và là cây skill chuẩn duy nhất
- `.agent/agents/`
  - chuyên gia theo vai trò
- `.agent/workflows/`
  - workflow điều phối
- `.agent/skills/workspace-operating-system/`
  - skill trung tâm
- `.agent/skills/workspace-operating-system/references/task-routing.md`
  - map nhanh từ loại task sang skill phù hợp
- `.agent/skills/workspace-operating-system/references/composition-patterns.md`
  - cách ghép nhiều skill với nhau
- `.agent/skills/workspace-operating-system/references/quality-bar.md`
  - chuẩn tối thiểu trước khi kết thúc task
- `.agent/skills/workspace-operating-system/references/operating-charter.md`
  - operating model kiểu team senior, boundary cho bài toán tham vọng và nhạy cảm
- `.agent/skills/workspace-operating-system/references/branch-and-release-policy.md`
  - branch-first, PR-first, và flow merge/promotion
- `.agent/skills/workspace-operating-system/references/idea-to-program-playbook.md`
  - biến ý tưởng lớn thành brief, milestone, và verification slices
- `.agent/skills/workspace-operating-system/references/department-operating-model.md`
  - mô hình vận hành theo các lane như product, architecture, build, QA, security, ops
- `.agent/skills/workspace-operating-system/references/skill-catalog.md`
  - danh sách đầy đủ các skill hiện có

## Prompt Mẫu Có Thể Copy Ngay

### Prompt tổng quát

```text
Use $workspace-operating-system to understand this request, pick the minimum effective skill stack, do the work, and verify the result before finishing.
```

### Prompt build feature

```text
Use $workspace-operating-system to build this feature end-to-end, including planning, implementation, and verification.
```

### Prompt ý tưởng lớn

```text
Use $workspace-operating-system to turn this ambitious idea into a real engineering program with requirements, architecture, prototype scope, verification strategy, and staged delivery.
```

### Prompt hệ thống lớn

```text
Use $systems-engineering to shape this mission-style system into interfaces, telemetry, simulation boundaries, operator workflows, and a first verifiable delivery slice.
```

### Prompt sửa bug

```text
Use $workspace-operating-system to route this issue, identify the root cause, patch it, and verify the fix.
```

### Prompt làm UI

```text
Use $frontend-design to improve this UI with a stronger visual direction and better UX clarity.
```

### Prompt kiểm tra web

```text
Use $webapp-testing to inspect the app, discover selectors, and verify the key user journeys.
```

## Cách Nâng Cấp Sau Này

Nếu bạn thêm hoặc sửa skill:

1. cập nhật `SKILL.md` của skill đó
2. nếu skill lớn thì thêm `agents/openai.yaml`
3. chạy lại script build catalog:

```text
python .agent/skills/workspace-operating-system/scripts/build_skill_catalog.py
```

## Ghi Chú Quan Trọng

- Bộ này đã dùng được ngay.
- Bây giờ chỉ còn một cây skill chuẩn là `.agent/skills/`.
- Repo này đã được gộp thật sự, không còn hai thư viện skill song song nữa.
- Mặc định repo này là local-first: không bật sẵn MCP server bên ngoài.
- Task code nghiêm túc nên đi theo branch/worktree -> verify -> PR/integration -> main.
- 4 skill file văn phòng có license hạn chế đã được gỡ bỏ khỏi bản public của bundle.
- Các workflow mới được viết lại theo hệ Codex hiện tại, không import launcher hay app shell từ bundle lạ vào cây skill chính.

## Câu Mở Đầu Tốt Nhất

Nếu chỉ chọn đúng một câu để bắt đầu, hãy dùng:

```text
Use $workspace-operating-system to decide what to do first, which skills to load, and how to verify the result.
```
