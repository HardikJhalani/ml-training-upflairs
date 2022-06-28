import tkinter as tk
app = tk.Tk(__name__)
app.geometry("400x400")
app.title('My application')
# a = tk.Label(app, text='Hardik Jhalani')
# a.pack()
# b = tk.Label(app, text='Upflairs')
# b.pack()
# c = tk.Label(app, text='mine')
# c.place(x=300, y=300)
# c.grid()
# v.set('temp')
t1 = tk.Variable(app)
e1 = tk.Entry(app, textvariable=t1)
e1.place(x=130, y=50)
v = tk.Variable(app)
a = tk.Label(app, textvariable=v)
a.place(x=300, y=300)

def kuchkaamhai():
    v.set('Wow ' + e1.get())

def yebhikarnahai():
    v.set('Waah ' + e1.get())
    # pass

bt = tk.Button(app, text='Click', command=kuchkaamhai)
bt.place(x=100, y=200)
bt2 = tk.Button(app, text='Click here', command=yebhikarnahai)
bt2.place(x=200, y=200)
app.mainloop()