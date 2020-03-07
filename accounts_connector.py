class connector:

    def __init__(self, num):
        self.num = num

        file = open("accounts", "r")
        self.content = file.readlines()
        file.close()

    def get_data(self, string):
        string = (string.strip("UPS0123456789:")).strip()
        return string


    def get_user(self):
        count = 0
        while count < (len(self.content) / 3):
            for line in self.content:
                if ("U" + str(self.num) + ": ") in line:
                    return self.get_data(line)
            count += 1


    def get_pass(self):
        count = 0
        while count < (len(self.content) / 3):
            for line in self.content:
                if ("P" + str(self.num) + ": ") in line:
                    return self.get_data(line)
            count += 1


    def get_secret(self):
        count = 0
        while count < (len(self.content) / 3):
            for line in self.content:
                if ("S" + str(self.num) + ": ") in line:
                    return self.get_data(line)
            count += 1



        
