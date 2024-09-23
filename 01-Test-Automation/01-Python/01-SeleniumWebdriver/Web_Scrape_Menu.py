# web scraping events from www.python.org main page and putting into a dictionary
from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# find 'upcoming events' on python.org and web scrape events
# using CSS selector
# events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget > div > ul > li > a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

# close browser
driver.quit()
