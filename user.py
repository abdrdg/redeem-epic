import time
import pyotp
import accounts_connector
from selenium import webdriver

class User:
    def __init__(self, username, password, secret=""):
        self.username = username
        self.password = password
        self.secret = secret


    def login(self):
        self.browser = webdriver.Chrome("C:/Chromedriver/chromedriver.exe")
        self.browser.get("https://www.epicgames.com/login")
        self.browser.implicitly_wait(1000)

        print("Signing in " + self.username + "...")
        time.sleep(8)

        email_field = self.browser.find_element_by_xpath('//form/div/div/input')
        password_field = self.browser.find_element_by_name('password')
        login_button = self.browser.find_element_by_id('login')

        email_field.send_keys(self.username)
        password_field.send_keys(self.password)
        time.sleep(2)
        login_button.click()

        time.sleep(8)
        
        if (self.secret != " "):
            self.browser.get(self.browser.current_url)
            code_field = self.browser.find_element_by_xpath('//*[@id="code"]')
            continue_button = self.browser.find_element_by_xpath('//form/div[3]/button[2]')
            totp = pyotp.TOTP(self.secret)
            code_field.send_keys(totp.now())
            continue_button.click()

        print("Sign-in complete!")


    def save_user(self):
        conn = accounts_connector.connector()
        conn.save_user(self.username, self.password, self.secret)


    def redeem(self):
        self.login()
        input()