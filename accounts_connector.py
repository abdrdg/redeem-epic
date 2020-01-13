def get_user(num):
    count = 0
    while count < (len(content) / 3):
        for line in content:
            if ("U" + str(num) + ": ") in line:
                return line.strip("UPS0123456789: ")
        count += 1


def get_pass(num):
    count = 0
    while count < (len(content) / 3):
        for line in content:
            if ("P" + str(num) + ": ") in line:
                return line.strip("UPS0123456789: ")
        count += 1


def get_secret(num):
    count = 0
    while count < (len(content) / 3):
        for line in content:
            if ("S" + str(num) + ": ") in line:
                return line.strip("UPS0123456789: ")
        count += 1


file = open("accounts", "r")
content = file.readlines()
file.close()
