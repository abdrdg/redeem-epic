class connector:

    def __init__(self):

        file = open("accounts", "r")
        self.content = file.readlines()
        self.user_len = (len(self.content) / 3)
        print(self.user_len)
        file.close()

    def get_data(self, string):
        string = (string.strip("UPS0123456789:")).strip()
        return string

    def get_user(self, num):
        count = 0
        while count < (self.user_len):
            for line in self.content:
                if ("U" + str(num) + ": ") in line:
                    return self.get_data(line)
            count += 1

    def get_pass(self, num):
        count = 0
        while count < (self.user_len):
            for line in self.content:
                if ("P" + str(num) + ": ") in line:
                    return self.get_data(line)
            count += 1

    def get_secret(self, num):
        count = 0
        while count < (self.user_len):
            for line in self.content:
                if ("S" + str(num) + ": ") in line:
                    return self.get_data(line)
            count += 1
