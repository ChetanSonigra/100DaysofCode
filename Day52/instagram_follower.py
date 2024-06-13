from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import ElementClickInterceptedException,NoSuchElementException
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

insta_login_url = "https://www.instagram.com/accounts/login/?hl=en"
insta_url  = "https://www.instagram.com"
SIMILAR_ACCOUNT = 'example'

class InstaFollower():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.email = "abc@gmail.com"
        self.passwd = "abc@123"
        self.is_authenticated = False

    def login(self):
        self.driver.get(insta_login_url)
        time.sleep(5)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(self.email)
        passwd = self.driver.find_element(By.NAME, 'password')
        passwd.send_keys(self.passwd,Keys.ENTER)
        time.sleep(7)
        self.is_authenticated = True

    def find_followers(self,n: int):
        self.driver.get(f"{insta_url}/{SIMILAR_ACCOUNT}")
        time.sleep(3)
        followers = self.driver.find_element(By.XPATH, f'//a[@href="/{SIMILAR_ACCOUNT}/followers/"]')
        followers.click()        
        # followers.click()   
        time.sleep(5)
        self.dialog = self.driver.find_element(By.XPATH, '//div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(n):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.dialog)
            time.sleep(3)

    def follow(self,n: int):
        buttons = self.dialog.find_elements(By.TAG_NAME, 'button')               
        for button in buttons[:n]:
            try:
                self.driver.execute_script("arguments[0].click();",button)
                time.sleep(1)
                print('clicked')
                cancel_button = self.driver.find_elements(By.XPATH, '//button[contains(text(),"Cancel")]')
                if cancel_button:
                    cancel_button[0].click()
                    print('canceled')
                    time.sleep(1)
            except Exception as e:
                print(e)


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers(4)
insta_follower.follow(20)

