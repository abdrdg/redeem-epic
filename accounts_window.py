from tkinter import *
import accounts_connector

conn = accounts_connector.connector()

root = Tk()
root.title("Epic Games Account")

def save():
    conn.save_acc(username.get(), password.get(), "")
    username.set=''
    password.set=''
    email_input.delete(0, 100)
    password_input.delete(0, 100)

# String vars
username = StringVar()
password = StringVar()

# Initializing
email_input = Entry(root, textvariable = username)
password_input = Entry (root, show="*", textvariable = password)
submit_button = Button(root, text="Save!", command=save)

# Account entries:
Label(root, text="ACCOUNTS").grid(column = 0, row = 0)
Label(root, text="Email: ").grid(column = 1, row = 0)
email_input.grid(column = 2, row = 0)
Label(root, text="Password: ").grid(column = 3, row = 0)
password_input.grid(column = 4, row = 0)
submit_button.grid(column = 5, row = 0)

count = 0
for index in range(int(conn.user_len)):
    Label(root, text = str((index+1))+"     "+ conn.get_user(index)).grid(column = 0, row = index+4)

root.mainloop()