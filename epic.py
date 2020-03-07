from account import Account
from accounts_connector import connector

choice = int(input(
"[1] Account 1\n"
"[2] Account 2\n"
"Choice: ")) - 1

conn = connector(choice)
user = Account(conn.get_user(), conn.get_pass(), conn.get_secret)
user.Login()