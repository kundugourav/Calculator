from tkinter import *
import math

expression=""

def zero_expression():
    global expression
    if expression=="0":
        expression=""
def double_star():
    global expression
    if "**" in expression:
        pos = []
        count = 0
        i = 0
        j = 1
        duplicate = []
        while i < len(expression) - 1:
            if expression[i] == '*' and expression[j] == '*':
                count += 1
                duplicate.append("^")
                pos.append(j)
            else:
                duplicate.append(expression[i])
            i += 1
            j += 1
        duplicate.append(expression[len(expression) - 1])
        del i, j
        i = 0
        while i < count:
            z = pos.pop(0)
            duplicate[z] = ""
            i += 1
        del z
        demo = ""
        for i in range(len(duplicate)):
            demo += duplicate[i]
        del duplicate
        equation.set(demo)
        return demo
    else:
        equation.set(expression)
def empty_expression():
    global expression
    if expression == "" or expression=="0.0":
        expression = "0"

#==================== binding buttons keyboard ====================
def key_1(event):
    global expression
    zero_expression()
    if expression[-2:]=="**":
        demo=double_star()
        equation.set(demo+str(1))
        expression = expression + str(1)
    else:
        expression=expression+str(1)
        double_star()
def key_2(event):
    global expression
    zero_expression()
    if expression[-2:] == "**":
        demo = double_star()
        equation.set(demo + str(2))
        expression = expression + str(2)
    else:
        expression = expression + str(2)
        double_star()
def key_3(event):
    global expression
    zero_expression()
    if expression[-2:] == "**":
        demo = double_star()
        equation.set(demo + str(3))
        expression = expression + str(3)
    else:
        expression = expression + str(3)
        double_star()
def key_4(event):
    global expression
    zero_expression()
    if expression[-2:] == "**":
        demo = double_star()
        equation.set(demo + str(4))
        expression = expression + str(4)
    else:
        expression = expression + str(4)
        double_star()
def key_5(event):
    global expression
    zero_expression()
    if expression[-2:] == "**":
        demo = double_star()
        equation.set(demo + str(5))
        expression = expression + str(5)
    else:
        expression = expression + str(5)
        double_star()
def key_6(event):
    global expression
    zero_expression()
    if expression[-2:] == "**":
        demo = double_star()
        equation.set(demo + str(6))
        expression = expression + str(6)
    else:
        expression = expression + str(6)
        double_star()
def key_7(event):
    global expression
    zero_expression()
    if expression[-2:] == "**":
        demo = double_star()
        equation.set(demo + str(7))
        expression = expression + str(7)
    else:
        expression = expression + str(7)
        double_star()
def key_8(event):
    global expression
    zero_expression()
    if expression[-2:] == "**":
        demo = double_star()
        equation.set(demo + str(8))
        expression = expression + str(8)
    else:
        expression = expression + str(8)
        double_star()
def key_9(event):
    global expression
    zero_expression()
    if expression[-2:] == "**":
        demo = double_star()
        equation.set(demo + str(9))
        expression = expression + str(9)
    else:
        expression = expression + str(9)
        double_star()
def key_0(event):
    global expression
    zero_expression()
    if expression[-2:] == "**":
        demo = double_star()
        equation.set(demo + str(0))
        expression = expression + str(0)
    else:
        expression = expression + str(0)
        double_star()
def key_plus(event):
    global expression
    empty_expression()
    if expression[-1:]=='.':
        expression=expression[0:len(expression)-1]+"+"
        equation.set(expression)
    if expression[-2:]=='**':
        equation.set(double_star())
    elif expression[-1:]=='/' or expression[-1:]=='*' or expression[-1:]=='-' or expression[-1:]=='+':
        double_star()
    else:
        expression = expression + "+"
        double_star()
def key_minus(event):
    global expression
    empty_expression()
    if expression[-1:]=='.':
        expression=expression[0:len(expression)-1]+"-"
        equation.set(expression)
    if expression[-2:]=='**':
        equation.set(double_star())
    elif expression[-1:]=='/' or expression[-1:]=='*' or expression[-1:]=='-' or expression[-1:]=='+':
        double_star()
    else:
        expression = expression + "-"
        double_star()
def key_multiple(event):
    global expression
    empty_expression()
    if expression[-1:]=='.':
        expression=expression[0:len(expression)-1]+"*"
        equation.set(expression)
    if expression[-2:]=='**':
        equation.set(double_star())
    elif expression[-1:]=='/' or expression[-1:]=='*' or expression[-1:]=='-' or expression[-1:]=='+':
        double_star()
    else:
        expression = expression + "*"
        double_star()
def key_divide(event):
    global expression
    empty_expression()
    if expression[-1:]=='.':
        expression=expression[0:len(expression)-1]+"/"
        equation.set(expression)
    if expression[-2:]=='**':
        equation.set(double_star())
    elif expression[-1:]=='/' or expression[-1:]=='*' or expression[-1:]=='-' or expression[-1:]=='+':
        double_star()
    else:
        expression = expression + "/"
        double_star()
def key_enter(event):
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except ZeroDivisionError:
        equation.set("Cannot Divide by Zero")
    except:
        if expression == '':
            equation.set(expression + '0')
        else:
            if expression[-2:] == '**':
                temp = double_star()
                equation.set(temp)
                del temp
            else:
                double_star()
def key_delete(event):
    global  expression
    expression=""
    equation.set(expression+"0")
def key_dot(event):
    global expression
    empty_expression()
    fetch = entry.get()
    last_char = fetch[-1:]
    if last_char in ['+','-','/','*','^']:
        expression=expression+"0."
        double_star()
    if expression[-1:] == ".":
        double_star()
    else:
        expression = expression + "."
        double_star()
def key_backspace(event):
    global expression
    if expression[-2:] == "**":
        expression = expression[0:len(expression) - 2]
        double_star()
    else:
        if len(expression) == 1:
            expression = ""
            equation.set(expression + '0')
        if expression == "":
            equation.set(expression + '0')
        else:
            if expression[-2:] == "0." and len(expression) == 2:
                expression = expression[0:len(expression) - 2]
                equation.set(expression + '0')
            elif expression[-2:] == "0.":
                expression = expression[0:len(expression) - 2]
                double_star()
            else:
                expression = expression[0:len(expression) - 1]
                double_star()

#==================== defining functions for gui buttons ====================
def press_operator(operator):
    global expression
    empty_expression()
    if expression[-2:]=="**" or expression[-1:] in ['+','-','/','*']:
        pass
    elif expression[-1:]=='.' and operator == "**":
        temp = double_star()
        equation.set(temp[0:len(temp) - 1] + '^')
        del temp
        expression = expression[0:len(expression) - 1] + operator
    else:
        if operator=="**":
            if "**" in expression:
                temp=double_star()
                equation.set(temp+"^")
                del temp
            else:
                equation.set(expression+'^')
            expression = expression + str(operator)
    last_char = expression[-1:]
    if last_char=='.' and (operator in ['+','-','/','*']):
        expression=expression[0:len(expression)-1]+operator
        if "**" in expression:
            temp=double_star()
            equation.set(temp)
            del temp
        else:
            equation.set(expression)
    if last_char in ['+','-','/','*'] and operator=='.':
        if "**" in expression:
            expression = expression + "0."
            temp=double_star()
            equation.set(temp)
            del temp
        else:
            expression=expression+"0."
            double_star()
    if last_char in ['+','-','/','.','*']:
        pass
    else:
        expression = expression + str(operator)
        double_star()
def root_over():
    global expression
    if expression=='':
        expression='0'
    try:
        expression = float(expression)
        expression=math.sqrt(float(expression))
        expression = str(expression)
        if expression=="0.0":
            expression='0'
        equation.set(expression)
    except Exception:
        equation.set("Invalid Input")
        expression=""
def onedividebyx():
    global expression
    expression="1/"+expression
    double_star()
def square():
    global expression
    empty_expression()
    try:
        expression=float(expression)
        expression=math.pow(expression,2)
        if expression==0.0:
            expression='0'
        equation.set(expression)
        expression=str(expression)
    except Exception:
        equation.set("Invalid Input")
        expression=""
def press(num):
    global expression
    zero_expression()
    if expression[-2:]=="**":
        demo=double_star()
        equation.set(demo+str(num))
        expression = expression + str(num)
    else:
        expression=expression+str(num)
        double_star()
def equal():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=total
    except ZeroDivisionError:
        equation.set("Cannot Divide by Zero")
    except:
        if expression=='':
            equation.set(expression+'0')
        else:
            if expression[-2:]=='**':
                temp = double_star()
                equation.set(temp)
                del temp
            else:
                double_star()
def clear():
    global  expression
    expression=""
    equation.set(expression+'0')
def delete():
    global expression
    if expression[-2:] == "**":
        expression = expression[0:len(expression) - 2]
        double_star()
    else:
        if len(expression) == 1:
            expression = ""
            equation.set(expression + '0')
        if expression == "":
            equation.set(expression + '0')
        else:
            if expression[-2:] == "0." and len(expression) == 2:
                expression=expression[0:len(expression) - 2]
                equation.set(expression+'0')
            elif expression[-2:] == "0.":
                expression = expression[0:len(expression) - 2]
                double_star()
            else:
                expression = expression[0:len(expression) - 1]
                double_star()
def change_sign():
    global expression
    empty_expression()
    if expression[0]!='-' and expression!='0':
        expression="-"+expression
        double_star()
        return
    if expression[0]=='-':
        expression=expression[1:]
        empty_expression()
        double_star()
        return

root=Tk()

root.title("Calculator")
# root.iconbitmap(r'calc.ico')
root.geometry("352x468+500+180")
root.resizable(width=False, height=False)

root.bind("<Key-1>",key_1)
root.bind("<Key-2>", key_2)
root.bind("<Key-3>", key_3)
root.bind("<Key-4>", key_4)
root.bind("<Key-5>", key_5)
root.bind("<Key-6>", key_6)
root.bind("<Key-7>", key_7)
root.bind("<Key-8>", key_8)
root.bind("<Key-9>", key_9)
root.bind("<Key-0>", key_0)
root.bind("<Key-plus>", key_plus)
root.bind("<Key-minus>", key_minus)
root.bind("<Key-asterisk>", key_multiple)
root.bind("<Key-slash>", key_divide)
root.bind("<Return>", key_enter)
root.bind("<BackSpace>", key_backspace)
root.bind("<.>", key_dot)
root.bind("<Delete>", key_delete)

equation=StringVar()

#==================== row 0 ====================
entry=Entry(root,font='arial 20 bold',bg='gray',fg='black',bd=25,justify=RIGHT,textvariable=equation,state=DISABLED)
equation.set("0")
entry.grid(row=0,columnspan=4)

#==================== row 1 ====================
squareroot=Button(root,text="√",font='arial 15',bg='dark gray',padx=30,pady=10,bd=5,command=root_over)
squareroot.grid(row=1,column=0,columnspan=1)
dividebyx=Button(root,text="1/x",font='arial 15',bg='dark gray',padx=24,pady=10,bd=5,command=onedividebyx)
dividebyx.grid(row=1,column=1,columnspan=1)
wholesquare=Button(root,text="x²",font='arial 15',bg='dark gray',padx=26,pady=10,bd=5,command=square)
wholesquare.grid(row=1,column=2,columnspan=1)
power=Button(root,text="^",font='arial 15',bg='dark gray',padx=20,pady=10,bd=5,command=lambda: press_operator("**"))
power.grid(row=1,column=3,columnspan=1)

#==================== row 2 ====================
empty=Button(root,text="+/-",font='arial 15',bg='light gray',padx=23,pady=10,bd=5,command=change_sign)
empty.grid(row=2,column=0,columnspan=1)
clear=Button(root,text="C",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=clear)
clear.grid(row=2,column=1,columnspan=1)
deletebutton=Button(root,text="DEL",font='arial 15',bg='light gray',padx=16,pady=10,bd=5,command=delete)
deletebutton.grid(row=2,column=2,columnspan=1)
division=Button(root,text="/",font='arial 15',bg='dark gray',padx=20,pady=10,bd=5,command=lambda: press_operator("/"))
division.grid(row=2,column=3,columnspan=1)

#==================== row 3 ====================
button7=Button(root,text="7",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(7))
button7.grid(row=3,column=0,columnspan=1)
button8=Button(root,text="8",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(8))
button8.grid(row=3,column=1,columnspan=1)
button9=Button(root,text="9",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(9))
button9.grid(row=3,column=2,columnspan=1)
multiple=Button(root,text="*",font='arial 15',bg='dark gray',padx=20,pady=10,bd=5,command=lambda: press_operator("*"))
multiple.grid(row=3,column=3,columnspan=1)

#==================== row 4 ====================
button4=Button(root,text="4",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(4))
button4.grid(row=4,column=0,columnspan=1)
button5=Button(root,text="5",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(5))
button5.grid(row=4,column=1,columnspan=1)
button6=Button(root,text="6",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(6))
button6.grid(row=4,column=2,columnspan=1)
minus=Button(root,text="-",font='arial 15',bg='dark gray',padx=20,pady=10,bd=5,command=lambda: press_operator("-"))
minus.grid(row=4,column=3,columnspan=1)

#==================== row 5 ====================
button1=Button(root,text="1",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(1))
button1.grid(row=5,column=0,columnspan=1)
button2=Button(root,text="2",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(2))
button2.grid(row=5,column=1,columnspan=1)
button3=Button(root,text="3",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(3))
button3.grid(row=5,column=2,columnspan=1)
# ======== grid of plus operator occupies 5th and 6th row =============
plus=Button(root,text="+",font='arial 15',bg='dark gray',padx=18,pady=42,bd=5,command=lambda: press_operator("+"))
plus.grid(row=5,column=3,columnspan=1,rowspan=2)

#==================== row 6 ====================
dot=Button(root,text=" .",font='arial 15',padx=30,pady=10,bd=5,command=lambda: press_operator("."))
dot.grid(row=6,column=0,columnspan=1)
button0=Button(root,text="0",font='arial 15',bg='light gray',padx=30,pady=10,bd=5,command=lambda: press(0))
button0.grid(row=6,column=1,columnspan=1)
equals=Button(root,text="=",font='arial 15',padx=30,pady=10,bd=5,command=equal)
equals.grid(row=6,column=2,columnspan=1)

root.mainloop()