import tkinter as tk
app = tk.Tk()
app.geometry("400x400")
app.title('Naya calculator')

def abc(n):
    answerVariable.set(answerVariable.get() + str(n))

def calc():
    answerVariable.set(eval(answerVariable.get()))

def clear():
    answerVariable.set('')

answerVariable = tk.Variable()

label1 = tk.Label(app, textvariable=answerVariable)
label1.place(x=300, y=50)

buttonClear = tk.Button(app, text='C', command=clear)
buttonClear.place(x=50, y=20)
button7 = tk.Button(app, text='7', command=lambda : abc('7'))
button7.place(x=50, y=100)
button8 = tk.Button(app, text='8', command=lambda : abc('8'))
button8.place(x=150, y=100)
button9 = tk.Button(app, text='9', command=lambda : abc('9'))
button9.place(x=250, y=100)
buttonPlus = tk.Button(app, text='+', command=lambda : abc('+'))
buttonPlus.place(x=350, y=100)
button4 = tk.Button(app, text='4', command=lambda : abc('4'))
button4.place(x=50, y=180)
button5 = tk.Button(app, text='5', command=lambda : abc('5'))
button5.place(x=150, y=180)
button6 = tk.Button(app, text='6', command=lambda : abc('6'))
button6.place(x=250, y=180)
buttonMinus = tk.Button(app, text='-', command=lambda : abc('-'))
buttonMinus.place(x=350, y=180)
button1 = tk.Button(app, text='1', command=lambda : abc('1'))
button1.place(x=50, y=260)
button2 = tk.Button(app, text='2', command=lambda : abc('2'))
button2.place(x=150, y=260)
button3 = tk.Button(app, text='3', command=lambda : abc('3'))
button3.place(x=250, y=260)
buttonProduct = tk.Button(app, text='*', command=lambda : abc('*'))
buttonProduct.place(x=350, y=260)
buttonDot = tk.Button(app, text='.', command=lambda : abc('.'))
buttonDot.place(x=50, y=340)
button0 = tk.Button(app, text='0', command=lambda : abc('0'))
button0.place(x=150, y=340)
buttonEqual = tk.Button(app, text='=', command=calc)
buttonEqual.place(x=250, y=340)
buttonDivide = tk.Button(app, text='/', command=lambda : abc('/'))
buttonDivide.place(x=350, y=340)

app.mainloop()