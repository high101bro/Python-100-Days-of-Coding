
from tkinter import *
import pickle
import os
import secrets
import string
import pyperclip


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')


cred_path = 'credentials.pkl'
if os.path.exists(cred_path):
    with open(cred_path, 'rb') as file:
        credentials = pickle.load(file)
else:
    credentials = {}

def save():
    with open(cred_path, 'wb') as file:
        pickle.dump(credentials, file)


def copy_to_clipboard(text):
    pyperclip.copy(text)

def show():
    show_window = Toplevel(window)
    show_window.title("Credentials")
    show_window.config(padx=20, pady=20)

    row = 0
    for website, creds in credentials.items():
        Label(show_window, text=f"Website: {website}", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w")
        row += 1
        Label(show_window, text=f"Email/Username: {creds['email-username']}").grid(row=row, column=0, sticky="w")
        copy_username = Button(show_window, text="copy", command=lambda u=creds['email-username']: copy_to_clipboard(u))
        copy_username.grid(row=row, column=1)
        row += 1
        Label(show_window, text=f"Password: {creds['password']}").grid(row=row, column=0, sticky="w")
        copy_password = Button(show_window, text="copy", command=lambda p=creds['password']: copy_to_clipboard(p))
        copy_password.grid(row=row, column=1)
        delete_button = Button(show_window, text="delete", command=lambda w=website, sw=show_window: delete(w, sw))
        delete_button.grid(row=row - 2, column=1)
        row += 1
        Label(show_window, text="").grid(row=row, column=0)  # Additional label with no text
        row += 1



def add():
    credentials[website_entry.get()] = {
        'email-username': email_username_entry.get(),
        'password': password_entry.get(),
    }
    save()
    # print(credentials)

def delete(website, show_window):
    if website in credentials:
        del credentials[website]
        save()
        show_window.destroy()
        show()

def generate(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(characters) for i in range(length))
    password_entry.delete(0, END)
    password_entry.insert(0, secure_password)


canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_username_label = Label(text='E-mail/Username:')
email_username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)


website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_username_entry = Entry(width=36)
email_username_entry.insert(END, 'daniel.komnick@gmail.com')
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)


password_button = Button(text='Generate', command=generate)
password_button.grid(column=2, row=3)

add_button = Button(width=30, text='Update', command=add)
add_button.grid(column=1, row=4, columnspan=2)

show_button = Button(width=30, text='Show', command=show)
show_button.grid(column=1, row=5, columnspan=2)

window.mainloop()






