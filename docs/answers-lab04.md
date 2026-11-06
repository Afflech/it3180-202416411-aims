# Lab 04 — Trả lời thảo luận

- Trong Release Flow của học phần, `master` là nơi phát triển tiếp còn
  `release/*` giữ dòng đã nộp. Chỉ đưa bản sửa cần thiết về `master`; merge
  nguyên nhánh release có thể mang theo thay đổi phiên bản hoặc bảo trì riêng.
- GitFlow dùng thêm nhánh `develop` và các nhánh release/hotfix để chuẩn bị
  phát hành. Mô hình của bài thực hành dùng `master` làm nhánh phát triển chính
  và `release/labXX` làm dòng nộp bài.
- `1.0.0` đánh dấu bản ổn định đầu tiên sau các mốc thực hành `0.1.0` đến
  `0.3.0`; `0.4.0` vẫn biểu thị giai đoạn chưa ổn định theo SemVer.
