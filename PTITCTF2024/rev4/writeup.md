# Writeup Rev4 by `AnhCD`
This's a challenge about find out where the real function is in 2000 random ones, and then find out how those main functions flows, take the data then reverse it

It's an exe PE32+ so open IDA64 and throw it into this, look at the 5 main function below the function view `(idk why but my mentor said if it was a GOLANG or PYTHON or RUSH sth, he would check the nearest function in the main first when it comes to about 1800 funcs like this)` , so i followed exactly what he said and got my first overall look

![image](https://github.com/user-attachments/assets/4564497e-1778-4383-8cb1-d468255e7077)

Looking through the main_main source code, we can see it called 2 function 
```  main_a0e34459298adf12(qword_DB8008); main_ae0184eaf94897fe() ```
The first function have an condition which check the value of v2 with 36, if there wasn't the same value it would call exit

![image](https://github.com/user-attachments/assets/26768c97-e59b-4cc9-ac8b-a63f4db4233b)

I want to see what is qword_D8008 that was loaded into the first function so i double click on it and it has the data of 0x12 in hex so it must be 18
Now that i can understand how the code flows, i got a thought of the flag length must be 36 and then it was sliced into 2 parts, the first one and second one have the same length which is 18.
Let's dive deeper into what the function does, set a breakpoint at the encrypt function, i can easily understand how it encrypt the data

First of all, set a breakpoint at the length check to see what would it do with my input, as we can see when we settle here the data is still the same which wasn't encrypted ( i put `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` in the input)

![image](https://github.com/user-attachments/assets/af641544-ac2d-40d2-8d11-2a1caa3ed76a)

![image](https://github.com/user-attachments/assets/60180cce-a988-4d36-836d-275612353950)

v2 and v5 in the 2 functions have the same value, so this is a global variable ( our input ), now that i realized they take or `( input ascii + 32 + i ) ^ 42`, check all characters from the data below which is `a1` below

`a1[] =
{
  0x32,        0x37,  
        0x29,    
      0x35,      
    0x25,        
  0x3B,        0x2E,  
        0xE0,    
      0xCD,      
    0x1B,        
  0xD4,        0x1D,  
        0xD8,    
      0xD6,      
    0xCF,        
  0x22,        0xE1,  
        0xD2
};`

Thus i wrote a python script which reversed all of those steps and got the first flag part `PTITCTF{redacted`

![image](https://github.com/user-attachments/assets/6e175242-bad0-46f4-82e0-13375afef3f3)

The second part got the same logic, the different that made me so struggle is that we must put the breakpoint to take the data in the ASM code!
