# Lab 02 — Trả lời thảo luận

- Đồng bộ với `master` trước PR để kiểm tra tính tương thích và giải quyết
  xung đột trước khi tích hợp.
- Không rebase các commit đã được người khác dùng; rebase đổi SHA và khiến
  lịch sử chung bị phân nhánh. Với nhánh riêng, dùng `--force-with-lease` khi
  cần đẩy lịch sử đã rebase.
- `feature/*` chứa tính năng sản phẩm; `topic/*` chứa việc hỗ trợ như tài liệu,
  cấu hình CI hoặc chuẩn bị phát hành.
- Merge commit giữ lịch sử từng commit; squash gộp thay đổi thành một commit;
  rebase tạo lịch sử tuyến tính với SHA mới.
