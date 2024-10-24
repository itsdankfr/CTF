Đề cho ta 1 file txt và 1 PE32

![image](https://github.com/user-attachments/assets/4b4dd19b-bfdf-43ec-87f3-39a09de74d56)

![image](https://github.com/user-attachments/assets/beaf0940-6315-44a2-915a-c718659f3ab9)

Trong bài này ta cần phải tìm hiểu cách mà chương trình tạo ra serial từ chính name mà người dùng nhập vào, đó cũng là bản chất của keygen (Key generator). 
Một bài keygen có logic đơn giản chúng ta sẽ được cung cấp serial hoặc username, mục tiêu của chúng ta là đi tìm giá trị còn lại để validate chương trình.
Và như đã thấy trong file txt, `Find the Name when the Serial is 5B134977135E7D13` 
Tất cả logic của bài này nằm trong hàm main:
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  signed int v3; // ebp
  int i; // esi
  char v6; // [esp+Ch] [ebp-130h]
  char v7[2]; // [esp+Dh] [ebp-12Fh] BYREF
  char v8[100]; // [esp+10h] [ebp-12Ch] BYREF
  char Buffer[197]; // [esp+74h] [ebp-C8h] BYREF
  __int16 v10; // [esp+139h] [ebp-3h]
  char v11; // [esp+13Bh] [ebp-1h]

  memset(v8, 0, sizeof(v8));
  memset(Buffer, 0, sizeof(Buffer));
  v10 = 0;
  v11 = 0;
  v6 = 16;
  qmemcpy(v7, " 0", sizeof(v7));
  sub_4011B9((int)aInputName);
  scanf("%s", v8);
  v3 = 0;
  for ( i = 0; v3 < (int)strlen(v8); ++i )
  {
    if ( i >= 3 )
      i = 0;
    sprintf(Buffer, "%s%02X", Buffer, v8[v3++] ^ v7[i - 1]);
  }
  memset(v8, 0, sizeof(v8));
  sub_4011B9((int)aInputSerial);
  scanf("%s", v8);
  if ( !strcmp(v8, Buffer) )
    sub_4011B9((int)aCorrect);
  else
    sub_4011B9((int)aWrong);
  return 0;
}
```
Sau một lần debug thì mình cũng hiểu cách chương trình xử lí input, đầu tiên yêu cầu nhập username tương ứng với v8 sau khi run qua một hàm mã hoá và giá trị được lưu vào biến Buffer, sau đó call hàm scanf Serial để check nếu == thì return Correct
```
  for ( i = 0; v3 < (int)strlen(v8); ++i )
  {
    if ( i >= 3 )
      i = 0;
    sprintf(Buffer, "%s%02X", Buffer, v8[v3++] ^ v7[i - 1]);
  }
```
Thiếu gì thì mình tìm nấy, hiện mình biết giá trị Buffer cần tìm, v3 được khởi tạo = 0 nên chỉ cần có data của v7. Debug đến vị trí v7 được sử dụng ta dễ dàng lấy được data trong code asm. Đoạn này hơi ảo khi ta biên dịch sang pseudo code có lẽ là vì 0x10h khi convert sang là kí tự không nhìn thấy được nên IDA đã tự xoá đi mất? Anyway đọc ASM vẫn tốt hơn (kinh nghiệm sau khi lấy data chỉ có 0x20h và 0x30h đi xor k ra gì)

![image](https://github.com/user-attachments/assets/b6913fdf-33b3-4040-b2be-de5471ab3753)

![image](https://github.com/user-attachments/assets/4518fbab-19f2-4975-97f4-1e9da7844f83)

Giờ đã có đủ thông tin, viết 1 script python reverse lại logic hàm mã hoá và ta có được auth tưởng ứng: `#K3yg3nm3`
```
serial = "5B134977135E7D13"
b = bytes.fromhex(serial)
v7 = [0x10,0x20,0x30]
for i in range(8):
    print(chr(int(b[i])^v7[i%3]),end ="") #K3yg3nm3
```
