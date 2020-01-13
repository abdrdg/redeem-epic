import time
import accounts_connector as acc_db
import pyotp
from selenium import webdriver


def sign_in(user, pw, secret):
    print("Sign-in process started")
    browser = webdriver.Chrome("C:/Chromedriver/chromedriver.exe")
    browser.get("https://www.epicgames.com/login")
    browser.implicitly_wait(100)

    time.sleep(8)
    email = browser.find_element_by_xpath('//form/div/div/input')
    password = browser.find_element_by_name('password')
    login_button = browser.find_element_by_id('login')

    email.send_keys(user)
    password.send_keys(pw)
    login_button.click()

    time.sleep(8)
    if browser.current_url.find('https://www.epicgames.com/id/login/mfa') != -1:
        browser.get(browser.current_url)
        code_box = browser.find_element_by_xpath('//*[@id="code"]')
        continue_button = browser.find_element_by_xpath('//form/div[3]/button[2]')
        print("Has 2FA. Entering 2FA code...")
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
    choice = int(input(
        "[1] Account 1\n"
        "[2] Account 2\n"
        "Pick account: ")) - 1
    sign_in(acc_db.get_user(choice), acc_db.get_pass(choice), acc_db.get_secret(choice))


start()
