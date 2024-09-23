import selenium.webdriver.common.devtools.v85.page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# capture article count from wikipedia
article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(f"{article_count.text} obtained using XPath")

# alternative way of capturing sale element
article_count2 = driver.find_element(By.CSS_SELECTOR, value="#articlecount > a")
print(f"{article_count2.text} obtained using CSS selector")

# click anchor tag above
# article_count2.click()

# find link by name
click_link = driver.find_element(By.LINK_TEXT, value="Content portals")
click_link.click()

search_box = driver.find_element(By.NAME, value="search")
search_box.send_keys("Python", Keys.ENTER)


# driver.quit()
