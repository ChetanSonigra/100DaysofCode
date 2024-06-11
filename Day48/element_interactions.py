from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT,"Content portals")
# all_portals.click()

search_bar = driver.find_element(By.NAME,"search")
search_bar.send_keys("Python",Keys.ENTER)


# filling form data:

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME,"lName")
email = driver.find_element(By.NAME,"email")

fname.send_keys("Chetan")
lname.send_keys("Sonigra")
email.send_keys("abc@fmail.com",Keys.ENTER)