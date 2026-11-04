# Tool Mockup Áo — Urbanhomevibe

Tool ghép file thiết kế lên ảnh áo trơn để tạo ảnh mockup sản phẩm hàng loạt,
kèm tính năng **tự tạo màu áo mới từ một ảnh mẫu** bằng mô hình AI tách áo
(rembg/U2-Net) chạy trên chính máy của bạn.

## Cách chạy (Windows)

Cần **Python 3.10+** (cài từ python.org, nhớ tick "Add python.exe to PATH").

Nhấp đúp **`run.bat`**:

- Lần đầu: tự tạo môi trường ảo và cài thư viện (vài phút), và server sẽ tải
  mô hình tách áo (~176MB) — tất cả chỉ làm một lần.
- Các lần sau: mở thẳng tool tại **http://localhost:8765** (trình duyệt tự mở).
- Để nguyên cửa sổ đen của chương trình khi đang dùng; đóng cửa sổ = tắt tool.

Chạy tay nếu muốn: `python app.py` (sau khi đã `pip install -r requirements.txt`).

Kiến trúc: `app.py` là server Python local lo phần nặng — tách áo khỏi nền
bằng AI và nhuộm màu theo đúng vùng áo, có cache mặt nạ theo từng ảnh gốc
(nhuộm nhiều màu từ một ảnh chỉ chạy mô hình một lần). Giao diện web lo phần
khung in, ghép hình in theo nếp vải và xuất ảnh. Mở thẳng `index.html` bằng
trình duyệt vẫn dùng được các tính năng khác, nhưng **nhuộm màu bắt buộc
chạy qua server Python**.

## Quy trình dùng

1. **Áo mẫu:** kéo ảnh áo trơn vào mục 1 — nạp nhiều ảnh cùng lúc, mỗi ảnh là
   một màu. Đặt tên màu (tên này dùng đặt tên file xuất ra) và tick
   "Xuất màu này" cho những màu muốn xuất ở lần chạy đó.
2. **Tạo thêm màu từ một áo mẫu:** bấm nút "Tạo màu" ở áo gốc, chọn màu nhuộm
   + đặt tên màu + chỉnh độ đậm. Server tách đúng vùng áo bằng AI rồi nhuộm —
   nền giữ nguyên, nếp vải và sáng tối của áo được giữ lại, áo màu mới dùng
   chung khung in của áo gốc.
3. **Khung in:** bấm "Đặt khung" ở từng áo, kéo khung tới vị trí in trên áo:
   kéo giữa khung để di chuyển, kéo 4 góc để phóng to/thu nhỏ, kéo núm tròn
   phía trên để xoay. Mỗi màu áo có vị trí khung riêng.
4. **File thiết kế:** kéo hàng loạt file PNG nền trong suốt vào mục 2. Tool tự
   cắt phần viền trong suốt thừa quanh họa tiết. Bấm vào một file để xem thử
   trên áo; có thanh trượt chỉnh phóng to/thu nhỏ và lệch vị trí riêng cho
   từng file.
5. **Xuất ảnh:** nút cam ở góc trên. Ảnh ra chuẩn up shop: **vuông
   1000×1000, WebP**, tên file `ten-thiet-ke__ten-mau.webp`. Một ảnh thì tải
   thẳng, nhiều ảnh thì đóng gói thành một file `mockups-urbanhomevibe.zip`.

## Độ thật của hình in

Ba thanh trượt ở mục 3 điều chỉnh hiệu ứng ghép:

- **Uốn theo nếp vải** — hình in bị uốn theo nếp gấp của áo (displacement).
- **Ăn sáng tối của vải** — tông sáng tối của hình in đi theo ánh sáng trên áo.
- **Chi tiết nếp gấp** — mức độ hằn nếp gấp nhỏ lên trên hình in.

## Ghi chú

- Áo mẫu + vị trí khung in được trình duyệt tự lưu (gắn với địa chỉ
  localhost:8765) — mở lại tool là có sẵn. File thiết kế thì nạp lại mỗi lần.
- Vùng xuất ra là hình vuông ôm theo tâm khung in — xem trước thế nào thì
  ảnh ra thế đó.
- Mọi xử lý chạy local trên máy bạn, không gửi ảnh đi đâu.
