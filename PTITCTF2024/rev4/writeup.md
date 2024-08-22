# Writeup Rev4 by `AnhCD`
It's an exe PE32+ so open IDA64 and throw it into this, look at the 5 main function below the function view `(idk why but my mentor said if it was a GOLANG or PYTHON or RUSH sth, he would check the nearest function in the main first when it comes to about 1800 funcs like this)` , so i followed exactly what he said and got my first overall look

![image](https://github.com/user-attachments/assets/4564497e-1778-4383-8cb1-d468255e7077)

Looking through the main_main source code, we can see it called 2 function 
```  main_a0e34459298adf12(qword_DB8008); main_ae0184eaf94897fe() ```
The first function have an condition which check the value of v2 with 36, if there wasn't the same value it would call exit

![image](https://github.com/user-attachments/assets/26768c97-e59b-4cc9-ac8b-a63f4db4233b)

I want to see what is qword_D8008 that was loaded into the first function so i double click on it and it has the data of 0x12 in hex so it must be 18
Now that i can understand how the code flows, i got a thought of the flag length must be 36 and then it was sliced into 2 parts, the first one and second one have the same length which is 18.
Let's dive deeper into what the function does, set a breakpoint at the encrypt function, i can easily understand how it encrypt the data

![image](https://github.com/user-attachments/assets/bf1aabbd-4f8d-4da6-ba19-391d96d72a8a)

