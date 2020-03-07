import time
import os
import signal
import pyotp
from selenium import webdriver

class Account:

    def __init__(self, username, password, secret):
        self.username = username
        self.password = password
        self.secret = secret

        self.browser = webdriver.Chrome("C:/Chromedriver/chromedriver.exe")
        self.browser.get("https://www.epicgames.com/login")
        self.browser.implicitly_wait(1000)

    def Is2FA(self):
        if self.browser.current_url.find('https://www.epicgames.com/id/login/mfa') != -1:
            return True
        else:
            print("No 2FA, proceeding...")
            return False

    def Login(self):
        print("Sign-in process started")
        
        time.sleep(8)

        email_field = self.browser.find_element_by_xpath('//form/div/div/input')
        password_field = self.browser.find_element_by_name('password')
        login_button = self.browser.find_element_by_id('login')

        email_field.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button.click()

        time.sleep(8)
        if self.Is2FA():
            self.browser.get(self.browser.current_url)
            code_field = self.browser.find_element_by_xpath('//*[@id="code"]')
            continue_button = self.browser.find_element_by_xpath('//form/div[3]/button[2]')
            totp = pyotp.TOTP(self.secret)
            code_field.send_keys(totp.now())
            continue_button.click()
        
        print("Sign-in complete!")

    def Redeem(self):
        return False

    def Logout(self):
        return False