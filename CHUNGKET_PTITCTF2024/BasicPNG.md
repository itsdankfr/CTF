# BasicPNG ( Forensics 3 ) writeup by `whales`

### Forensics part `( by Long )`



### RE part `( by CDA )`
After the first 1h without any idea what to do in Crypto 1, Long told me he found the file which we have to reverse to get the flag. So from then on it'd be my job with the PE32+

Opened the file in IDA64, I got the overall view. But i still couldn't understand the code's flow and how it worked clearly, so i copied and pasted it into chatgpt requested some help:


![Screenshot 2024-09-15 183653](https://github.com/user-attachments/assets/cf9aafb9-a7e5-445f-92df-f2ce2a2a3d20)


It told me that i needed to put 2 input which is ```v4, v5[0]``` correctly to bypass some conditions then i would get the flag.
This `if` must be what chatgpt mentioned, it's an easy one. The v5 we put in must satisfied an `AND (&)` bitwise and `v5 % 3` which means v5 % 3 != 0 because 0 stands for false in binary and in many programming languages.


![image](https://github.com/user-attachments/assets/c3eeb5da-30c4-474c-9922-40ccd8af9f91)


In summary, i bruteforce the v5 input as refered 6, 12, 18, 24, ... At 6 it created a file but i couldn't open it so i continue with 12 and 18, the 12 didn't even create a file, but at 18 i open the file with a mp4 viewer, here come the flag 


![image](https://github.com/user-attachments/assets/f0529010-a2f5-4470-ae4b-52065e70a99f)


