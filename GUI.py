# Python program to  create a simple GUI  
# calculator using Tkinter 





#FROM GFG




# import everything from tkinter module
#pimport Tkinter as tk
from Tkinter import *
  
# globally declare the expression variable 
expression = "" 
  
  
# Function to update expressiom 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    equation.set(expression) 
  
  
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 

        # total = str(eval(expression))
        exp=str(expression) 
        # print(exp)
        ans=otb(exp[1])+dtb(exp[0])+dtb(exp[2])+"0000"

        f=open('./in.txt','w')
        f.write(str(ans))
        f.close()
        # equation.set("") 
        fi=open('./out1.txt','r')
        # print("bjbjbjbj")
        final=str(fi.read(4))
        # print(final)
        equation.set(str(btd(final))) 
        fi.close()
  

        
       


        
        # initialze the expression variable 
        # by empty string 
        expression = "" 
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
def dtb(n):
    if n=='1':
        return "0001"
    if n=='2':
        return "0010"
    if n=='3':
        return "0011"
    if n=='4':
        return "0100"
    if n=='5':
        return "0101"
    if n=='6':
        return "0110"
    if n=='7':
        return "0111"
    if n=='8':
        return "1000"
    if n=='9':
        return "1001"
    if n=='0':
        return "0000"
def otb(n):
    if n=='+':
        return "00"
    if n=='-':
        return "01"
    if n=='|':
        return "10"
    if n=='~':
        return "11"


def btd(n):

  if n=="0000":
       return 0
  if n=="0001":
       return 1
  if n=="0010":
       return 2
  if n=="0011":
       return 3
  if n=="0100":
       return 4
  if n=="0101":
       return 5
  if n=="0110":
       return 6
  if n=="0111":
       return 7
  if n=="1000":
       return 8
  if n=="1001":
       return 9



          
  



  
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    gui.configure(background="black") 
  
    # set the title of GUI window 
    gui.title("Simple Calculator") 
  
    # set the configuration of GUI window 
    gui.geometry("300x280+0+300") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(gui, textvariable=equation) 
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=4, ipadx=70) 
  
    equation.set('0') 
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
                     command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
                     command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
                     command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
                     command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
                     command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
                     command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
                     command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
                     command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                     command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
                     command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='black', bg='red', 
                  command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='red', 
                   command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' | ', fg='black', bg='red', 
                      command=lambda: press("|"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text='2s complement ', fg='black', bg='red', 
                    command=lambda: press("~"), height=1, width=7) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='black', bg='red', 
                   command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='Clear', fg='black', bg='red', 
                   command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
  
    # start the GUI 
    gui.mainloop() 
