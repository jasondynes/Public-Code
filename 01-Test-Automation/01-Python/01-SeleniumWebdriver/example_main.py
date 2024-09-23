from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1&language=en_US&currency=USD"

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# amazon script
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(URL)
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
#
# # to close browser window (active tab)
# # driver.close()
#
# # will close multiple windows of browser
# driver.quit()


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
# using NAME attribute
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

# using ID attribute
button = driver.find_element(By.ID, value="submit")
print(button.text)
print(button.size)
print(button.location)

# using CSS selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# using Xpath - https://www.w3schools.com/xml/xpath_intro.asp
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# will close multiple windows of browser
driver.quit()
