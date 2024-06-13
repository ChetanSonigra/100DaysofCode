PROMISED_DOWN = 100
PROMISED_UP = 80

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Adding below directory allows you to go directly to site without loging in.
chrome_options.add_argument("user-data-dir=C:/Users/{username}/AppData/Local/Google/Chrome/User Data/")


class InternetSpeedXBot:
    def __init__(self) -> None:
        self.down: float = 0
        self.up: float = 0
        self.driver = webdriver.Chrome(options=chrome_options)


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(15)
        # continue_ = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        # continue_.click()
        # time.sleep(2)
        go = self.driver.find_element(By.CLASS_NAME, "start-text")
        go.click()
        time.sleep(50)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        self.driver.quit()
        return self.up, self.down


    def tweet_at_provider(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://x.com/home/")
        time.sleep(5)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post.send_keys(f"Hello Internet Provider,\n My net is {self.up} Up/{self.down} Down, While I am promised {PROMISED_UP} Up/{PROMISED_DOWN} Down.")
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()
        time.sleep(3)
        print('Tweet sent')
        self.driver.quit()


internet_speed_x_bot = InternetSpeedXBot()
speed_up, speed_down = internet_speed_x_bot.get_internet_speed()
print(speed_down,speed_up)

if speed_down<PROMISED_DOWN or speed_up<PROMISED_UP:
    internet_speed_x_bot.tweet_at_provider()


