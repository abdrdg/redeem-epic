class connector:
    def __init__(self):
        self.refresh()

    def refresh(self):
        file = open("accounts", "r")
        self.content = file.readlines()
        self.totalLines = len(self.content)
        self.totalUsers = int(self.totalLines / 3)
        file.close()

    def get_data(self, string):
        string = (string.strip("UPS0123456789:")).strip()
        return string

    def get(self, type, index):
        self.refresh()

        type = type.upper()
        if (type == "U" or type == "P" or type == "S"):
            count = 0
            while count < (self.totalUsers):
                for line in self.content:
                    if (type + str(index) + ": ") in line:
                        return self.get_data(line)
                count += 1
        else:
            print("Invalid get type.")


    def save_user(self, username, password, secret=""):
        file = open("accounts", 'a')
        file.write("\nU" + str(self.totalUsers) + ": " + username)
        file.write("\nP" + str(self.totalUsers) + ": " + password)
        file.write("\nS" + str(self.totalUsers) + ": " + secret)
        file.close()
        self.refresh()