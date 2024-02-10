from tkinter import *


def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
cal = Tk()
cal.title("Calculator")
operator = ""
text_Input= StringVar()

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def bntEqualsInput():
    global operator
    sumup=str(eval(operator)) 
    text_Input.set(sumup)
    operator=""

txtDisplay = Entry(cal, font=('Comic Sans MS',30,'bold','italic'),textvariable = text_Input, bd=30, insertwidth=4, bg="white", justify='right').grid(columnspan=4) 

btn7=Button(cal, padx=36, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="7",  command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal, padx=36, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="8", command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(cal, padx=36, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="9", command=lambda:btnClick(9)).grid(row=1,column=2)
Addition=Button(cal, padx=45, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="+", command=lambda:btnClick('+')).grid(row=1,column=3 )
#=========================================================================================================
btn4=Button(cal, padx=36, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="4", command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(cal, padx=36, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="5", command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(cal, padx=36, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="6", command=lambda:btnClick(6)).grid(row=2,column=2)
Subtration=Button(cal, padx=45, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="-", command=lambda:btnClick("-")).grid(row=2,column=3)
#=========================================================================================================
btn1=Button(cal, padx=36, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="1", command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(cal, padx=36, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="2", command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(cal, padx=36, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="3", command=lambda:btnClick(3)).grid(row=3,column=2)
Multiply=Button(cal, padx=45, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="*", command=lambda:btnClick("*")).grid(row=3,column=3)
#=========================================================================================================
btn0=Button(cal, padx=34, pady=30, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="0", command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear=Button(cal, padx=34, pady=30, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="C", command=btnClearDisplay).grid(row=4,column=1)
btnEquals=Button(cal, padx=30, pady=30, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="= ", command=bntEqualsInput).grid(row=4,column=2)
Division=Button(cal, padx=45, pady=30, bd=10, fg='black',font=('Comic Sans MS',23,'bold'),bg="powder blue", text="/", command=lambda:btnClick("/")).grid(row=4,column=3)

cal.mainloop()
