# BasicPNG ( Forensics 3 ) writeup by `whales`

### Forensics part `( by Long )`



### RE part `( by CDA )`
After the first 1h without any idea what to do in Crypto 1, Long told me he found the file which we have to reverse to get the flag. So from then on it'd be my job with the PE32+

Opened the file in IDA64, I got the overall view. But i still couldn't understand the code's flow and how it worked clearly, so i copied and pasted it into chatgpt requested some help:


![Screenshot 2024-09-15 183653](https://github.com/user-attachments/assets/cf9aafb9-a7e5-445f-92df-f2ce2a2a3d20)


It told me that i needed to put 2 input which is ```v4, v5[0]``` correctly to bypass some conditions then i would get the flag.
Because it's a competition ( i meaned i don't want to waste any time 'cause we still couldn't solve any challenge yet ), i asked chatgpt about what should i put into the exe file, it give me some hints like this


![Screenshot 2024-09-15 182932](https://github.com/user-attachments/assets/9ae66fe6-a98e-4daf-96d7-e48151da8541)


![Screenshot 2024-09-15 183518](https://github.com/user-attachments/assets/f905bf78-4cf1-4cfd-8e9e-493336249ea8)


![Screenshot 2024-09-15 182948](https://github.com/user-attachments/assets/34b61b32-ad45-4af3-9f16-d2f253a79769)

Ok from now that i know what i have to do, i bruteforce the v5 input as the chatgpt refered 6, 12, 18, 24, ... At 6 it created a file but i don't know how to open it so i continue with 12 and 18, the 12 didn't even create a file, but at 18 i open the file with an mp4 viewer, here come the flag 


![image](https://github.com/user-attachments/assets/f0529010-a2f5-4470-ae4b-52065e70a99f)


