import time
import os
import signal
import pyotp
from selenium import webdriver


def sign_in(user, pw):
    browser = webdriver.Chrome("C:/Chromedriver/chromedriver.exe")
    browser.get("https://www.epicgames.com/login")
    browser.implicitly_wait(100)

    time.sleep(5)
    email = browser.find_element_by_xpath('//form/div/div/input')
    password = browser.find_element_by_name('password')
    login_button = browser.find_element_by_id('login')
    email.send_keys(user)
    password.send_keys(pw)
    login_button.click()

    time.sleep(5)
    if browser.current_url.find('https://www.epicgames.com/id/login/mfa') != -1:
        browser.get(browser.current_url)
        code_box = browser.find_element_by_xpath('//*[@id="code"]')
        continue_button = browser.find_element_by_xpath('//form/div[3]/button[2]')
        print("Has 2FA. Entering 2FA code...")
        secret = "IJEVQRKKJNFUCWRUKFATIV2QIVFEWTCVIFKEGWSXKFKVMRCVKBJA"
        totp = pyotp.TOTP(secret)
        code_box.send_keys(totp.now())
        continue_button.click()
        print("The 2FA code is : ", totp.now())
    else:
        print("No 2FA, proceeding...")

    choice = input("Sign in complete. Press \"Y\" to login to another account, press any to quit: ")
    if choice.upper() == "Y":
    	browser.quit()
    	start()

def start():
    is_Valid = False
    while not is_Valid:
        choice = input("[A] Account 1\n"
                       "[B] Account 2\n"
                       "Pick account: ").upper()

        if choice == "A":
            user = "abeydeguzman@gmail.com"
            pw = "AiraBeb2015112888"
            is_Valid = True
        elif choice == "B":
            user = "whoopsywoozi@gmail.com"
            pw = "987258987258zxc"
            is_Valid = True
        else:
            print("\nInvalid choice\n")

    sign_in(user, pw)

start()
