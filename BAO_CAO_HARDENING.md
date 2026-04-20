# Báo Cáo Hardening

Bản tiếng Anh: `HARDENING_REPORT.md`

Ngày audit: 2026-04-20

## Mục Tiêu

Làm bundle này an toàn hơn để public, để AI khác có thể dùng ngay, và để giảm tối đa các điểm có thể gây mơ hồ về quyền sở hữu, kết nối bên ngoài, hoặc side-effect trên máy.

## Đã Xử Lý

- Gỡ 4 skill có license hạn chế khỏi bundle public:
  - `.agent/skills/docx`
  - `.agent/skills/pdf`
  - `.agent/skills/pptx`
  - `.agent/skills/xlsx`
- Làm sạch `.agent/mcp_config.json` thành cấu hình rỗng, không bật sẵn dịch vụ MCP bên ngoài.
- Chuẩn hóa `.claude-plugin/marketplace.json`:
  - bỏ thông tin chủ sở hữu cá nhân
  - bỏ path cũ `./skills/...` đã sai với cấu trúc merged
  - đổi metadata sang tên bundle hiện tại
- Harden `.agent/scripts/auto_preview.py`:
  - bỏ `shell=True`
  - resolve lệnh npm/yarn/pnpm/bun trên Windows theo cách rõ ràng hơn
- Mở rộng `.gitignore` để bỏ qua file runtime và log tạo ra trong lúc preview.
- Cập nhật lại routing, quality bar, và hướng dẫn sử dụng theo hướng local-first.
- Audit 2 bundle cộng đồng mới (`superpowers-main.zip`, `antigravity-awesome-skills-main.zip`) trước khi gộp.
- Không import launcher hay app shell từ bundle ngoài vào cây skill chính:
  - `superpowers-main/hooks/run-hook.cmd`
  - `antigravity-awesome-skills-main/START_APP.bat`
  - `antigravity-awesome-skills-main/scripts/activate-skills.bat`
- Chỉ hấp thụ các workflow giá trị cao bằng cách viết lại local-first vào skill tree hiện tại.

## Kết Quả Audit

- Không tìm thấy hidden file lạ ngoài `.git`.
- Không tìm thấy junction hay reparse point còn sót lại.
- Không tìm thấy executable binary đáng ngờ trong repo.
- Các skill còn lại không tự động kết nối ra ngoài; những skill dùng provider bên ngoài vẫn là opt-in và cần được gọi rõ ràng.
- Đã chạy custom scan bằng Windows Defender trên `D:\\skill\\skill\\agent-skills-unified` và không có threat nào được báo cáo.
- Không đưa file `.bat`, `.cmd`, app web, hay script launcher từ 2 bundle mới vào thư viện skill canonical.

## Tình Trạng Sau Hardening

- Thư viện skill hiện tại: được tăng cường bằng nhóm workflow mới cho verification, worktrees, plan execution, review handling, branch closeout, và closed-loop delivery.
- Cấu hình mặc định: local-first, không có MCP server bên ngoài được bật sẵn.
- Metadata/plugin market đã được làm sạch để phù hợp với bundle merged hiện tại.

## Ghi Chú Vận Hành

- Nếu muốn dùng MCP server bên ngoài, hãy tự thêm cấu hình sau khi review thủ công.
- Nếu muốn thêm lại skill xử lý file văn phòng, chỉ nên thêm từ nguồn mà bạn chắc chắn có quyền sử dụng và phân phối.
- Script trong repo vẫn có thể đọc file dự án hoặc chạy subprocess khi bạn chủ động gọi nó, nhưng bundle hiện tại không ship cấu hình nào tự động lấy dữ liệu máy.
