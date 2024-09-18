# BasicPNG ( Forensics 3 ) writeup by `whales`

The challenge provided us a corrupted file, with the byte structure resembling a PE32+ file.

![image](https://github.com/user-attachments/assets/b8648a99-009c-47dc-a431-bd6397941e5e)

Instead of null bytes `00`, the file contained `1B`. 
My first thought was that the byte values had been shifted. 
To reverse this, I tried to shift the bytes back by subtracting the shift value:
```python
def shift_bytes(byte_array, shift_value=0x1B):
    return bytes([(byte - shift_value) % 256 for byte in byte_array])

def main():
    input = r"C:\Users\ADMIN\Downloads\basic.png"
    output = r"C:\Users\ADMIN\Downloads\test.txt"
    with open(input, "rb") as f:
        data = f.read()
    shifted_data = shift_bytes(data)
    with open(output, "wb") as f:
        f.write(shifted_data)
if __name__ == "__main__":
    main()
```
However, this approach didn’t get the expected results.

There was another way to transform 1B into 00, is to XORing each byte of the file with 1B.
I used the following script:
```python
def xor_bytes(byte_array, key=0x1B):
    return bytes([byte ^ key for byte in byte_array])

def main():
    input = r"C:\Users\ADMIN\Downloads\basic.png"
    output = r"C:\Users\ADMIN\Downloads\test2.txt"

    with open(input, "rb") as f:
        data = f.read()

    xor_data = xor_bytes(data)

    with open(output, "wb") as f:
        f.write(xor_data)

if __name__ == "__main__":
    main()
```
After running this script, I got the original file.
Now come to the reverse engineering part:
![image](https://github.com/user-attachments/assets/64813f62-f869-4bc9-b418-0aedb94e0aa5)


Opened the file in IDA64, I got the overall view. But i still couldn't understand the code's flow and how it worked clearly, so i copied and pasted it into chatgpt requested some help:


![Screenshot 2024-09-15 183653](https://github.com/user-attachments/assets/cf9aafb9-a7e5-445f-92df-f2ce2a2a3d20)


It told me that i needed to put 2 input which is ```v4, v5[0]``` correctly to bypass some conditions then i would get the flag.
This `if` must be what chatgpt mentioned, it's an easy one. The v5 we put in must satisfied an `AND (&)` bitwise and `v5 % 3` which means v5 % 3 != 0 because 0 stands for false in binary and in many programming languages.


![image](https://github.com/user-attachments/assets/c3eeb5da-30c4-474c-9922-40ccd8af9f91)


In summary, i bruteforce the v5 input as refered 6, 12, 18, 24, ... At 6 it created a file but i couldn't open it so i continue with 12 and 18, the 12 didn't even create a file, but at 18 i open the file with a mp4 viewer, here come the flag 


![image](https://github.com/user-attachments/assets/f0529010-a2f5-4470-ae4b-52065e70a99f)


