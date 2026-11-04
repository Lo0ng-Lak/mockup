# Tool Mockup Áo — Urbanhomevibe

Tool ghép file thiết kế lên ảnh áo trơn để tạo ảnh mockup sản phẩm hàng loạt.
Chạy hoàn toàn ngay trong trình duyệt, không cần cài đặt, không cần mạng —
file của bạn không rời khỏi máy.

## Cách chạy

Mở file **`index.html`** bằng Chrome hoặc Edge (nhấp đúp là được).

Lưu ý: áo mẫu + vị trí khung in được lưu tự động **trong trình duyệt, gắn với
đúng đường dẫn file này**. Hãy để file ở một chỗ cố định (đừng đổi tên/di
chuyển sau khi đã lưu mẫu), và luôn mở bằng cùng một trình duyệt — mở bằng
trình duyệt khác sẽ là một bộ lưu trữ trống mới.

## Quy trình dùng

1. **Áo mẫu:** kéo ảnh áo trơn vào mục 1 — nạp nhiều ảnh cùng lúc, mỗi ảnh là
   một màu. Đặt tên màu (tên này dùng đặt tên file xuất ra) và tick
   "Xuất màu này" cho những màu muốn xuất ở lần chạy đó.
2. **Tạo thêm màu từ một áo mẫu:** bấm nút "Tạo màu" ở áo gốc, chọn màu nhuộm
   + đặt tên màu + chỉnh độ đậm, tool sinh ra áo màu mới — giữ nguyên nếp vải
   và sáng tối của áo gốc, và dùng chung khung in của áo gốc. Tool tự nhận
   diện vùng áo để nhuộm: áo tối/màu trên nền sáng tương phản thì nền được
   giữ nguyên; áo sáng trên nền xám/trắng (tông áo và nền quá gần nhau, máy
   không tách reliably được) thì tool nhuộm đều cả khung — áo lên màu chuẩn,
   nền thành phông cùng tông màu.
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

Mặc định đã để ở mức trông thật; cứ tăng/giảm theo mắt khi xem thử.

## Ghi chú

- File thiết kế chỉ nạp cho phiên làm việc hiện tại — mở lại tool thì thả lại
  các file vào (áo mẫu và khung in thì vẫn còn).
- Vùng xuất ra là hình vuông ôm theo tâm khung in — xem trước trên màn hình
  thế nào thì ảnh ra thế đó.
