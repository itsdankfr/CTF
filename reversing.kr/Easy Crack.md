# Viết writeup web này cũng như để học lại từ đầu tất cả những khái niệm mà trước giờ ăn xổi
Vẫn tuân thủ theo các bước tự đặt ra trong quá trình làm RE, ném vào `Die` và nhận được 1 PE32 không có dấu hiệu bị packed hay obfuscated

![image](https://github.com/user-attachments/assets/5c5d80da-5e62-4f0c-9ffc-ff7a6457a768)

Chạy thử chương trình, đúng như tên bài đây là 1 bài dạng `EasyCrackme`, mục tiêu của chúng ta là crack password của file này

![image](https://github.com/user-attachments/assets/00915822-04dc-4549-a05b-ab7d1ad8308b)

Đưa file vào IDA32, tìm đến vị trí check password thực thi ta có thể thấy password của ta được so sánh với các data có sẵn ở dạng ASCII hoặc strings

![image](https://github.com/user-attachments/assets/881b1e49-acfc-4601-944e-9119816f2fdb)

=> Reverse lại logic trên ta được auth: Ea5yR3versing => Solved
