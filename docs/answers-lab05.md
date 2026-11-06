# Lab 05 — Trả lời thảo luận

- Sửa ở `master` trước giúp dòng phát triển chính nhận bản vá ngay và giảm
  nguy cơ quên. Sửa ở nhánh release trước tái hiện đúng mã đã phát hành và
  kiểm thử bản vá trên dòng bị ảnh hưởng, nhưng phải lan truyền sang các dòng
  khác. Bài này dùng cách thứ hai.
- Nếu quên đưa bản sửa vào `release/lab05`, vòng lặp kiểm tra hành vi ở Phần F
  sẽ in `0` cho `v1.1.0` thay vì `1`. So sánh bằng `git cherry -v` cũng giúp
  phát hiện commit tương đương chưa có trên dòng cần kiểm tra.
- Commit sửa lỗi tách khỏi commit nâng phiên bản để cherry-pick chỉ mang mã
  sửa và test, không ghi đè `1.1.0` bằng `1.0.1`.
