def get_user(num):
    count = 0
    while count < (len(content) / 3):
        for line in content:
            if ("U" + str(num) + ": ") in line:
                return get_data(line)
        count += 1


def get_pass(num):
    count = 0
    while count < (len(content) / 3):
        for line in content:
            if ("P" + str(num) + ": ") in line:
                return get_data(line)
        count += 1


def get_secret(num):
    count = 0
    while count < (len(content) / 3):
        for line in content:
            if ("S" + str(num) + ": ") in line:
                return get_data(line)
        count += 1


def get_data(string):
    string = (string.strip("UPS0123456789:")).strip()
    return string
    

file = open("accounts", "r")
content = file.readlines()
file.close()
