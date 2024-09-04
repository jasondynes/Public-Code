# test URL is http://secure-retreat-92358.herokuapp.com/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = "Jason"
last_name = "Dynes"
email = "jason.dynes@tester.com"

# find first name, last name and email fields
# first_name_field = driver.find_element(By.CSS_SELECTOR, value="body > form > input.form-control.top")
# last_name_field = driver.find_element(By.CSS_SELECTOR, value="body > form > input.form-control.middle")
# email_field = driver.find_element(By.CSS_SELECTOR, value="body > form > input.form-control.bottom")

# enter data into fields
# first_name_field.send_keys(first_name, Keys.TAB)
# last_name_field.send_keys(last_name, Keys.TAB)
# email_field.send_keys(email, Keys.ENTER)

driver.find_element(By.NAME, value="fName").send_keys(first_name, Keys.TAB)
driver.find_element(By.NAME, value="lName").send_keys(last_name, Keys.TAB)
driver.find_element(By.NAME, value="email").send_keys(email)

# click submit button
driver.find_element(By.CSS_SELECTOR, value="form button").click()
