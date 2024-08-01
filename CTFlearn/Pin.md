# PIN
#### https://ctflearn.com/challenge/379
## Writeup
#### As a first step for any RE challenges, make it executable in linux by `chmod +x rev1` then run it. Got our first overall look
![image](https://github.com/user-attachments/assets/ea323a60-e2ca-4900-ac19-259e9c807636)

## Solution using IDA
![image](https://github.com/user-attachments/assets/33a2715c-674d-4e48-8551-7a15a903a4f5)
#### Open it in IDA, we can see the ASM flow is that it called `cek` to check if `input == the pin ( the flag )`, we got the different PIN which called `PIN benar`
#### Step into `cek`, it seems clearly they're comparing `index rbp+var_4 with eax`
![image](https://github.com/user-attachments/assets/9f31441a-d72b-4a4f-817e-1d7e3d30b921)
#### eax now that have the same value with `cs:valid` after the `mov` they made, double click in the valid to see its value and we got the flag in `HEX`
![image](https://github.com/user-attachments/assets/21ae6b4e-fe84-4bd0-8b47-5f098847e229)

## Solution using GDB
#### Checking out all the functions with `info functions`
![image](https://github.com/user-attachments/assets/3bc903a3-74ba-4dc4-b893-8c1f5b60ffcc)
#### Disassemble main, got our ASM 
![image](https://github.com/user-attachments/assets/ee1e0f39-1c7e-4c7b-a687-a56a0be3db71)
#### The logic is still the same, we have to check the `cek` at `0x000000000040060c` so we have to disas `cek` too
![image](https://github.com/user-attachments/assets/a9fbccc2-21e7-43f8-9d18-959a6499c8ee)
#### Set a breakpoint after the `cmp` to check `eax`, run the file and put whatever with the input 'cause that's no need, got to our breakpoint and display the value of `eax`, got our flag which is `CTFlearn{333333}`
![image](https://github.com/user-attachments/assets/3ba637ee-a637-49ac-8a37-0246d7c5a413)
