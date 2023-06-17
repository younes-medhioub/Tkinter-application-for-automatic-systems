# Tkinter-application-for-automatic-systems
we have designed a desktop application using the Python language that tracks multiple responses. 
It is characterized by precision and speed. Finally, it's easy to use and very practical.

1: Application name - 2: Numerator polynomial
3 : denominator polynomial - 4 : nature of study
6: Transfer Function Field - 5: Response Type           
7: Button for plotting curve - 8: Information
![image](https://github.com/younes-medhioub/Tkinter-application-for-automatic-systems/assets/130268149/600cbe51-03ee-4369-8f98-0005359c7779)
The source code is captured by Visual Studio Code.
We have imported several libraries.
Tkinter: for the graphical interface
Numpy: for mathematical functions 
Matplotlib: for plotting
Control: for frequency study (Bode)
Signal : for temporal studies.

***********NB: some libraries require downloading and installation via the command prompt.***********

Example: pip install numpy


 /////***********\\\\\ HOW TO USE  /////***********\\\\\
 The transfer function H(p) = N(p)/D(p) is entered in the corresponding fields. This data is read through the Class ENTRY .

The choice of response type is made via the Combobox class. It lets you choose from a predefined list of list types.

Pressing the "Trace curve" button calls the Trace() function. Depending on type and nature, the Tracez() function calls the corresponding Impulse() or echlon() or Bode() or error() function.

continue with the Bode() example:
we pass the coefficients of the numerator and denominator as parameters to the function.
We then transform a string into a list of integers, as the Control class Bode function requires this syntax.
Then we create the transfer function again 

Then plot and display it

This application is :
Easy to use 
Fast.
Does not require a lot of hardware resources.
Reliable.
It offers the possibility of repairing itself in the event of an error using the error() function.
Example : 
Nature: Time study and Bode type
This is not possible, so it displays this message.
![image](https://github.com/younes-medhioub/Tkinter-application-for-automatic-systems/assets/130268149/10ebfe60-6c01-46d4-a14c-cbe6d3819851)
