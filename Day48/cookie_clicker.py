from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID,"cookie")

start = time.perf_counter()
click_time = time.perf_counter()
con = 0
while con<300:
    cookie.click()
    
    if time.perf_counter() - click_time >=10:
        store = driver.find_elements(By.XPATH,"//*[@id='store']/div")
        for store_item in store[::-1]:
            if store_item.get_attribute("class") != "grayed":
                store_item.click()
                click_time = time.perf_counter()
                break
    con = time.perf_counter() - start
    # print(con)

        
cps = driver.find_element(By.ID,"cps")
print(cps.text)
driver.quit()

