from account import Account
from accounts_connector import connector

conn = connector()
user_len = int(conn.user_len)

print("Which account will you use?")
for index in range(user_len):
    print("["+ str(index+1) + "] " + conn.get_user(index))
print("[" + str(user_len+1) + "] All Accounts")

choice = int(input("Choice: ")) - 1

if (choice == user_len+1):
    print("Using all accounts!")
    for index in range(user_len):
        user = Account(conn.get_user(index), conn.get_pass(index), conn.get_secret(index))
        print("~Logging in " + conn.get_user(index) + "...")
        user.Login()
        print("~Redeeming!")
        user.Redeem()
        print("~Logging out of " + conn.get_user(index) + "...")
        user.Logout()

else:
    user = Account(conn.get_user(choice), conn.get_pass(choice), conn.get_secret(choice))
    print("~Logging in " + conn.get_user(choice) + "...")
    user.Login()
    print("~Redeeming!")
    user.Redeem()
    print("~Logging out of " + conn.get_user(choice) + "...")
    user.Logout()