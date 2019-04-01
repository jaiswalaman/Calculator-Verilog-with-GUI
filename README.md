# Calculator-Verilog-with-GUI
CSN 221 CP-1
--------------



We have made four .v files out of which 2 are modules which are Calculator.v and Seven_seg_output.v and 2 are test-benches which are Calc_TestBench.v and calc_tb2.v. We have implemented the GUI using Python. We have used the Tkinter library to create the GUI. 
The modules are explained below-
The Calculator.v is our main design file.   We have string as one input which takes a 14-bit instruction as input. The first 2 bits specify the operation code, the next 4-bits are for the first number and the next 4-bits are for the second number and the last 4-bits is for the output. We have 2 outputs , one as res which will be 4-bits BCD output and the other output as seven_output which will be seven segment output.

The Seven_seg_output.v is the module for converting the input BCD as seven segment output.
The Calc_TestBench.v is the test bench for the Calculator.v module which will give all the possible inputs to the module.
The calc_tb2.v is the test bench which connects the GUI with the input and output files of the Verilog code. We have made 3 files, as interface between the GUI and the Verilog code. One file is for the input which takes the input from the GUI as entered by the user.  The entered input in the GUI will then be stored in the input file. The data from the input file will be called by the test bench in the Xilinx. After getting the data, we will calculate the output using the Verilog module. And the result in the BCD form will then be stored in the output file. The GUI will then collect the data from the output file and display it on the user screen.   
