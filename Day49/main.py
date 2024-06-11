# Automating Job Applications:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

linkedin_url = "https://www.linkedin.com/jobs/search/?currentJobId=3942491373&f_AL=true&f_E=2%2C3%2C4&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(linkedin_url)
# time.sleep(10)

# Automatic Sign In 
sign_in = driver.find_element(By.LINK_TEXT,"Sign in")
sign_in.click()

email = driver.find_element(By.NAME, "session_key")
email.send_keys("abc@gmail.com")
passwd = driver.find_element(By.NAME, "session_password")
passwd.send_keys("abc123",Keys.ENTER)


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[0]
    discard_button.click()
    time.sleep(2)

time.sleep(5)


# Applying:
for i in range(1,20):
    all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    for listing in all_listings:
        try:
            listing.click()
            time.sleep(2)
            easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
            easy_apply.click()
            time.sleep(2)
            try:
                next_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                print("_"*50,next_button.text, next_button.get_attribute("aria-label"),"_"*50, sep="\n")
                if next_button.text == "Submit application":
                    next_button.click()
                    time.sleep(2)
                else:
                    abort_application()
            except:
                continue
            # Click Close Button
            try:
                close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
                close_button.click()
            except:
                continue
        except:
            print("Application skipped.")
            continue
    pages = [x for x in driver.find_elements(By.CSS_SELECTOR, f".artdeco-pagination__indicator--number button")]
    next_page = pages[i]
    next_page.click()

time.sleep(10)
driver.quit()
