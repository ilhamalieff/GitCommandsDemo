import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")

driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

windows = driver.window_handles

driver.switch_to.window(windows[1])

wholeText = driver.find_element(By.XPATH, "//div/p[@class='im-para red']").text

wholeList = wholeText.split(" ")

email = None

for email in wholeList:
    if "@" in email:
        break

driver.close()

driver.switch_to.window(windows[0])

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)

driver.find_element(By.NAME, "password").send_keys("salam123")

driver.find_element(By.XPATH, "//input[@value='user']").click()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-body")))

driver.find_element(By.CSS_SELECTOR, "#okayBtn").click()

dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))

dropdown.select_by_visible_text("Teacher")

agreeTerm = driver.find_element(By.CSS_SELECTOR, "#terms")

if not agreeTerm.is_selected():
    agreeTerm.click()

driver.find_element(By.ID, "signInBtn").click()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))

alertText = driver.find_element(By.CLASS_NAME, "alert").text

print(alertText)

time.sleep(2)



