from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

events = dict()
events2 = dict()

for i in range(5):
    event = driver.find_element(By.XPATH, f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time")
    link = driver.find_element(By.XPATH,f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a")
    events[i] = {"time": event.text, "name": link.text}



event_times = [x.text for x in driver.find_elements(By.CSS_SELECTOR,".event-widget time")]
links = [x.text for x in driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")]
events2 = {i:{event_times[i]:links[i]} for i in range(len(links))}


print(events)
print(events2)
# print(event_times,links,sep="\n")
driver.quit()