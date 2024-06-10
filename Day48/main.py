from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Keep the browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

link = "https://www.amazon.in/dp/B0BY8JZ22K?FORM=SSAPC1&th=1"
driver.get(link)

# driver.close() # closes single tab
# driver.quit()  # quit entire browser

price_rs = driver.find_element(By.CLASS_NAME,value="a-price-whole")
price_ps = driver.find_element(By.CLASS_NAME,value="a-price-fraction")

print(f"The price is {price_rs.text}.{price_ps.text}")


driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME,"q")
print(search_bar)  # selenium element
print(search_bar.get_attribute("placeholder"))
print(search_bar.tag_name)

button = driver.find_element(By.ID, "submit")

print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")

print(documentation_link.get_attribute("href"))
print(documentation_link.text)

submit_bug = driver.find_element(By.XPATH, "//*[@id='site-map']/div[2]/div/ul/li[3]/a")
print(submit_bug.text)
print(submit_bug.get_attribute('href'))

# All above methods, you can get multiple elements using find_elements() method.

driver.quit()