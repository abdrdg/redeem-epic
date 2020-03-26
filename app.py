import user
import accounts_connector
import os
import getpass
class App:
    def __init__(self):
        if __name__ == "__main__":
            self.start_con_menu()
    
    def start_con_menu(self):
        conn = accounts_connector.connector()
        hr = "--------------------------------------"
        print(hr +
            "\nChoose an account:\n"
            "\n[0] Add Account")
        for index in range(conn.totalUsers):
            print("[%d] %s" % (index+1, conn.get("U", index)))
        print(hr)

        choice = int(input("Choice: "))
        os.system('cls')
        if choice != 0:
            choice -= 1
            acc = user.User(conn.get("U", choice), conn.get("P", choice), conn.get("S", choice))
            acc.redeem()
        
        elif choice == 0:
            print("Save an account")
            print(hr)
            correct = "N"
            while correct != "Y":
                password = "1"
                cpassword = "2"
                while password != cpassword:
                    username = input("Email: ")
                    password = getpass.getpass("Password: ")
                    cpassword  = getpass.getpass("Confirm Password: ")
                    secret = input("2FA Key (Press enter if not using 2FA): ")
                    os.system('cls')
                
                print("Is this correct?\n" + hr + "\n" + username)
                correct = input("Is this correct [Y/N]: ").upper()

            if correct == "Y":
                print("Saving...")
                acc = user.User(username, password, secret)
                acc.save_user()
                

if __name__ == "__main__":
    App()