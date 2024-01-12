
from tkinter import *

window = Tk()

window.title('Unit Converter')
window.minsize(width=500, height=300)

header = Label(text='Mile to Kilometer Converter', font=('Arial',14,'bold'))
header.grid(column=2, row=1)


input = Entry(width=20)
input.grid(column=2, row=2)


miles = Label(text='Miles', font=('Arial',12,'normal'))
miles.grid(column=3, row=2)


equal = Label(text='is equal to', font=('Arial',12,'normal'))
equal.grid(column=1, row=3)

result = Label(text=0, font=('Arial',12,'normal'))
result.grid(column=2, row=3)

km = Label(text='Km', font=('Arial',12,'normal'))
km.grid(column=3, row=3)

def calc():
    r = int(input.get()) * 1.609344
    print(r)
    result.config(text=r)



calculate = Button(text='Calculate', font=('Arial',12,'normal'), command=calc)
calculate.grid(column=2, row=4)



window.mainloop()
