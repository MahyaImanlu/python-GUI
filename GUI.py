
from tkinter import *
from tkinter import ttk
import math

BMIROOT = Tk()
BMIROOT.title('BMI and Quadratic Equation')
BMIROOT.geometry("870x420")

frame = Frame(BMIROOT, bg='#E0E0E0', highlightbackground="#808080", highlightthickness=3)

#BMI
def calculate_bmi():       #BMI function
   try:
        W = float(weight.get())
        H = float(height.get())
        bmi = W / (H ** 2)

        if W < 0 or H < 0:
            result = 'not acceptable'
            Label1.config(text=result, fg="#CC0000")

        elif W and H > 0:
            if bmi <= 18.5:
                result = (f'BMI : {bmi} \n You are Underweight') + "\n" + "Gain" + str(18.5 * (H ** 2) - W) + "weight"
            elif 18.5 < bmi <= 24.9:
                result = (f'BMI : {bmi} \n You are Normal') + "\n" + "keep it up"
            elif 25 <= bmi <= 29.9:
                result = (f'BMI : {bmi} \n You are Overweight') + "\n" + "Lose" + str(W - 25 * (H ** 2)) + "weight"
            elif bmi >= 30:
                result = (f'BMI : {bmi} \n You are Obesity') + "\n" + "Lose" + str(W - 25 * (H ** 2)) + "weight"
            if bmi <= 18.5:
                Label1.config(text=result, fg="#004C99")
            elif 18.5 < bmi <= 24.9:
                Label1.config(text=result, fg="green")
            elif 25 <= bmi <= 29.9:
                Label1.config(text=result, fg="#FF8000")
            elif bmi >= 30:
                Label1.config(text=result, fg="#CC0000")

   except ZeroDivisionError:
       Label1.config(text='not acceptable', fg='red')
   except ValueError:
       Label1.config(text='inter both weight&height', fg='red')

def clear_heightandweight():     #clear function for BMI

    weight.delete(0, END)
    height.delete(0, END)


Label(frame, text="Enter your weight(kg):", bg="#E5CCFF", padx=1, pady=1, fg='#190033',
       font=('arial', 9)).grid(row=0, column=0, sticky=N, pady=20, padx=20)
weight = Entry(frame, bg='#FFCCFF')
weight.grid(row=0, column=1, sticky=W, padx=2, pady=2)

Label(frame, text="Enter your height(m):", bg="#E5CCFF", padx=1, pady=1, fg='#190033',
      font=('arial', 9)).grid(row=0, column=2, sticky=N, pady=20, padx=20)
height = Entry(frame, bg='#FFCCFF')
height.grid(row=0, column=3, sticky=W, padx=2, pady=2)

Label1 = Label(frame, text="BMI:", bg="#E5CCFF", padx=2, pady=2, fg='#190033',
      font=('arial', 9))
Label1.grid(row=5, column=3, sticky=N)

Label(frame, text="Gender:", fg='#330066', font=('arial', 9, 'bold')).grid(row=3, column=0, sticky=N)

Radiobutton(frame, text="Female", value=1, fg='#330066', font=('arial', 9, 'bold')).grid(row=3, column=1, sticky=N)
Radiobutton(frame, text="Male", value=2, fg='#330066', font=('arial', 9, 'bold')).grid(row=3, column=2, sticky=N)

Label(frame, text="Age:", bg="#E5CCFF", fg='#190033', font=('arial', 9)).grid(row=0, column=4, sticky=E, pady=20, padx=20)
age = ttk.Combobox(frame, width=5, values=[i for i in range(18, 46)]).grid(row=0, column=5, sticky=W, pady=20, padx= 20)

Button(frame, text="calculate BMI", bg="#E5CCFF", fg='#190033',  width=12,
       font=('arial', 9), command=calculate_bmi).grid(row=5, column=1, sticky=E, pady=30, columnspan=1)
Button(frame, text="clear", bg="#E5CCFF", fg='#190033', width=12,
       font=('arial', 9), command=clear_heightandweight).grid(row=5, column=2, sticky=W, pady=30, columnspan=1)


########################################################################################################################

#Quadratic Equation
def Root():                      #Quadratic Equation function

    try:
        a = float(A.get())
        b = float(B.get())
        c = float(C.get())
        delta = (b ** 2) - (4 * a * c)
        if a == 0:
            x1 = -c / b
            X1.config(text=x1, bg="#66CC00")
            if c == 0:
                x = 'zero'
                X1.config(text=x, bg="#66CC00")
        elif delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            x = (f'X1 : {x1}') + "\n" + (f'X2 : {x2}')
            X1.config(text=x, bg="#66CC00")
        elif delta == 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x = (f'X1 : {x1}')
            X1.config(text=x, bg="#66B2FF")
        else:
            x = 'no root'
            X1.config(text=x, bg="#FF6666")
    except ZeroDivisionError:
        x = 'not acceptable'
        X1.config(text=x, bg="#FFB266")
    except ValueError:
        X1.config(text='inter all of them', bg="#FFB266")

def clear():        #clear function for Quadratic Equation

    A.delete(0, END)
    B.delete(0, END)
    C.delete(0, END)

frame2 = Frame(BMIROOT, bg='#E0E0E0', highlightbackground="#808080", highlightthickness=3)

A = Entry(frame2, bg='#FFCCFF', width=20)
A.grid(row=0, column=0, sticky=E, padx=20, pady=20, columnspan=1)
Label(frame2, text="X ** 2 + ",bg='#E0E0E0', padx=1, pady=1, fg='#190033', font=('arial', 10)).grid(row=0, column=1,
                                                                                                   sticky=E, padx=20, pady=20)
B = Entry(frame2, bg='#FFCCFF', width=20)
B.grid(row=0, column=3, sticky=W, padx=20, pady=20)
Label(frame2, text="X + ", bg='#E0E0E0', padx=1, pady=1, fg='#190033', font=('arial', 10)).grid(row=0, column=4,
                                                                                               sticky=E, padx=20, pady=20)
C = Entry(frame2, bg='#FFCCFF', width=20)
C.grid(row=0, column=5, sticky=E, padx=30, pady=30)
Label(frame2, text="= 0 ", bg='#E0E0E0', padx=1, pady=1, fg='#190033', font=('arial', 10)).grid(row=0, column=6,
                                                                                               sticky=E, padx=20, pady=20)
X1 = Label(frame2, bg='#E0E0E0', padx=1, pady=1, fg='#190033', font=('arial', 9))
X1.grid(row=1, column=3, sticky=N, columnspan=2, padx=20, pady=20)

Button(frame2, text="Submit", bg="#E5CCFF", fg='#190033', width=6,
       font=('arial', 9), command=Root).grid(row=4, column=1, sticky=E, padx=5, pady=20)
Button(frame2, text="clear", bg="#E5CCFF", fg='#190033', width=6,
       font=('arial', 9), command=clear).grid(row=4, column=4, sticky=W, padx=5, pady=20)
frame2.grid(padx=40)
frame.grid(padx=40)


BMIROOT.mainloop()