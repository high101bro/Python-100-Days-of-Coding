
from tkinter import *

window = Tk()

window.title('DnD Dungeon Master')
window.minsize(width=500, height=300)

# Label
my_label = Label(text="name", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)
# my_label.place(x=0, y=0)
# my_label.pack(side='top')


# my_label['text'] = 'method 1'
# my_label.config(text='method 2')

def button_clicked():
    print('I got clicked')
    # my_label['text'] = "I got clicked"
    my_label.config(text=input.get())

button = Button(text='a button', font=('Courier', 12, 'normal'), command=button_clicked)
button.grid(column=1, row=2)
# button.pack()


input = Entry(width=20)
input.grid(column=1, row=3)
# input.pack(side='left')

text = Text(height=5, width=30)
text.focus()
text.insert(END, 'initial info')
print(text.get('1.0',END))
text.grid(column=2, row=1)
# text.pack(side='left')

def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
text.grid(column=2, row=4)
# spinbox.pack(side='right')

def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text='Is on?', variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=2, row=2)
# checkbutton.pack(side='right')


def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radio_state.set(1)
radiobutton1 = Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used, state='disabled')
radiobutton2 = Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used, state='active')
radiobutton3 = Radiobutton(text='Option2', value=3, variable=radio_state, command=radio_used, state='active')
radiobutton1.grid(column=3, row=1)
radiobutton2.grid(column=3, row=2)
radiobutton3.grid(column=3, row=3)
# radiobutton1.pack()
# radiobutton2.pack()
# radiobutton3.pack()


def listbox_used(event):
    my_label.config(text=listbox.get(listbox.curselection()))
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ['Apple','pear','orange','banana']
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=2, row=3)
# listbox.pack()



window.mainloop()



















