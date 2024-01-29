
from tkinter import *
import json
import secrets
import string
import pyperclip


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')


cred_path = 'credentials.json'
try:
    with open(cred_path, 'r') as file:
        credentials = json.load(file)
except FileNotFoundError as error:
    print(f"{error} does not exist, initializing dictionary.")
    credentials = {}


def save():
    with open(cred_path, 'w') as save_file:
        json.dump(credentials, save_file, indent=4)


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


def search():
    search_website = website_entry.get()  # Get the website name from the entry widget
    search_window = Toplevel(window)
    search_window.title(f"Credentials for {search_website}")
    search_window.config(padx=20, pady=20)

    if search_website in credentials:
        creds = credentials[search_website]
        row = 0
        Label(search_window, text=f"Website: {search_website}", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w")
        row += 1
        Label(search_window, text=f"Email/Username: {creds['email-username']}").grid(row=row, column=0, sticky="w")
        copy_username = Button(search_window, text="copy", command=lambda: copy_to_clipboard(creds['email-username']))
        copy_username.grid(row=row, column=1)
        row += 1
        Label(search_window, text=f"Password: {creds['password']}").grid(row=row, column=0, sticky="w")
        copy_password = Button(search_window, text="copy", command=lambda: copy_to_clipboard(creds['password']))
        copy_password.grid(row=row, column=1)
        delete_button = Button(search_window, text="delete", command=lambda w=search_website, sw=search_window: delete(w, sw))
        delete_button.grid(row=row - 2, column=1)
    else:
        Label(search_window, text="No credentials found.").grid(row=0, column=0, sticky="w")


canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_username_label = Label(text='E-mail/Username:')
email_username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)


website_entry = Entry(width=26)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_username_entry = Entry(width=36)
email_username_entry.insert(END, 'john.doe@gmail.com')
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)


website_button = Button(text='Search', width=7, command=search)
website_button.grid(column=2, row=1)

password_button = Button(text='Generate', width=7, command=generate)
password_button.grid(column=2, row=3)

add_button = Button(width=30, text='Update', command=add)
add_button.grid(column=1, row=4, columnspan=2)

show_button = Button(width=30, text='Show All', command=show)
show_button.grid(column=1, row=5, columnspan=2)

window.mainloop()






