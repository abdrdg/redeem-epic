import time
import os
import signal
import pyotp
from selenium import webdriver


def redeem(user, pw):
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

    time.sleep(15)
    browser.get(browser.current_url)
    time.sleep(3)
    browser.find_element_by_xpath('//span[4]/div/div/div/section/div/div[1]/div/a').click()

    time.sleep(10)
    browser.get(browser.current_url)
    time.sleep(3)
    get_button = browser.find_element_by_xpath('//div[3]/div/div/button/span')
    game_title = browser.find_element_by_xpath('//div[4]/div[3]/div/div[1]/div/div/div/ul/li[2]/a/span').text
    get_button.click()

    time.sleep(10)
    browser.get(browser.current_url)
    time.sleep(3)
    place_order = browser.find_element_by_xpath('//div[4]/div[1]/div[2]/div[5]/div/div/button')
    place_order.click()
    time.sleep(5)
    browser.close()
    browser.quit()
    print("YOU HAVE REDEEMED: ", game_title)


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

    redeem(user, pw)


def should_exit():
    choice = input("Do you want to quit? (Y/N)").upper()

    if choice == "Y":
        time.sleep(5)
        os.kill(os.getppid(), signal.SIGHUP)
    elif choice == "N":
        start()
    else:
        print("Invalid answer")
        should_exit()


start()
