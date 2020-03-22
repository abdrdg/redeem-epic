from tkinter import *
import accounts_connector

root = Tk()
root.title("Epic Games Account")
conn = accounts_connector.connector()
acc_users = ""

# String vars
username = StringVar()
password = StringVar()
content = StringVar() # For displaying out the accounts

for index in range(int(conn.user_len)):
    acc_users = acc_users + (conn.get_user(index) + "\n")

content.set(acc_users)

print(acc_users)

def save():
    new_cont = ''
    conn.save_acc(username.get(), password.get(), "")
    username.set('')
    password.set('')

    email_input.delete(0, 100)
    password_input.delete(0, 100)

    for index in range(int(conn.user_len+1)):
        new_cont = new_cont + (accounts_connector.connector().get_user(index) + "\n")
    
    print(new_cont)
    content.set(new_cont)
    conn.updateLen()

    content_label.update()


# Initializing
email_input = Entry(root, textvariable = username)
password_input = Entry (root, show="*", textvariable = password)
submit_button = Button(root, text="Save!", command=save)

main_label = Label(root, text="ACCOUNTS")
email_label = Label(root, text="Email: ")
password_label = Label(root, text="Password: ")
content_label = Label(root, textvariable = content)

# Account entries:
main_label.grid(column = 0, row = 0)
email_label.grid(column = 1, row = 0)
password_label.grid(column = 3, row = 0)

email_input.grid(column = 2, row = 0)
password_input.grid(column = 4, row = 0)
submit_button.grid(column = 5, row = 0)
 
content_label.grid(column = 0, row = 1)

root.mainloop()