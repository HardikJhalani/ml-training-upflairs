import tkinter as tk
app = tk.Tk()
app.geometry('400x400')
app.title('Sasta Calculator')

# ********* Answer *********
answer = 0
answerVariable = tk.Variable()
answerVariable.set(answer)

answerLabel = tk.Label(app, textvariable=answerVariable)
answerLabel.place(x=196, y=300)

# ******** functions ********

# * addition function
def additionFunction():
    answerVariable.set(int(textBox1.get()) + int(textBox2.get()))

# * subtraction function
def subtractionFunction():
    answerVariable.set(int(textBox1.get()) - int(textBox2.get()))

# * multiplication function
def multiplicationFunction():
    answerVariable.set(int(textBox1.get()) * int(textBox2.get()))

# * division function
def divisionFunction():
    answerVariable.set(int(textBox1.get()) / int(textBox2.get()))

# ********* input boxes ********

# * text box 1
input1 = tk.Variable(app)
textBox1 = tk.Entry(app, textvariable=input1)
textBox1.place(x=50, y=50)

# * text box 2
input2 = tk.Variable(app)
textBox2 = tk.Entry(app, textvariable=input2)
textBox2.place(x=220, y=50)

# ******* working buttons ********

# * Addition Button
additionButton = tk.Button(app, text='Addition', command=additionFunction)
additionButton.place(x=80, y=150)

# * Subtraction Button
subtractButton = tk.Button(app, text='Subtraction', command=subtractionFunction)
subtractButton.place(x=240, y=150)

# * Multiplication Button
multiplyButton = tk.Button(app, text='Multiplication', command=multiplicationFunction)
multiplyButton.place(x=70, y=200)

# * Division Button
divisionButton = tk.Button(app, text='Division', command=divisionFunction)
divisionButton.place(x=250, y=200)

app.mainloop()