from tkinter import *

root = Tk()
root.title("Epic Games Account")

# String vars
username = StringVar()
password = StringVar()

# Initializing
email_input = Entry(root, textvariable = username)
password_input = Entry (root, show="*", textvariable = password)
submit_button = Button(root, text="Save!")


# Account entries:
Label(root, text="Email: ").grid(column = 0, row = 1)
email_input.grid(column = 1, row = 1)
Label(root, text="Password: ").grid(column = 2, row = 1)
password_input.grid(column = 3, row = 1)
submit_button.grid(column = 4, row = 1)

count = 0
for items in range(10):
    Label(root, text = "Account "+str((items+1))+": ").grid(column = 0, row = items+4)




root.mainloop()