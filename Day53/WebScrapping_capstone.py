GOOGLE_FORM_URL = "https://forms.gle/mFJcXHhXF39rwEah7"
ZILLOW_SF_SITE = "https://appbrewery.github.io/Zillow-Clone/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

resp = requests.get(ZILLOW_SF_SITE)
zillow_data = BeautifulSoup(resp.text,"html.parser")

prices = [y.split("+")[0] for y in (x.string.split("/")[0] for x in zillow_data.find_all('span', class_='PropertyCardWrapper__StyledPriceLine'))]
# print(prices)

addresses = [x.string.strip() for x in zillow_data.find_all('address',attrs={"data-test":'property-card-addr'})]
# print(addresses)

links = [x.get('href') for x in zillow_data.find_all('a',attrs={'data-test': 'property-card-link'})]
# print(links)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
for i in range(len(prices)):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(5)

    address = driver.find_element(By.XPATH, '//div[@class="o3Dpx"]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(0.5)
    address.send_keys(addresses[i])

    price = driver.find_element(By.XPATH, '//div[@class="o3Dpx"]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(0.5)
    price.send_keys(prices[i])

    link = driver.find_element(By.XPATH, '//div[@class="o3Dpx"]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(0.5)
    link.send_keys(links[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()
    time.sleep(2)

# find google sheet in google forms/drive.
