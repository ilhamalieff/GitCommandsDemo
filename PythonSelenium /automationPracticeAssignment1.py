import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

productNames = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")

actualResult = []

for resultText in productNames:
    actualResult.append(resultText.text)

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

assert actualResult == expectedList

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver,10)

element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

assert driver.find_element(By.CLASS_NAME, "promoInfo").text == "Code applied ..!"

totalPrices = driver.find_elements(By.XPATH, "//tr/td[5]/p")

summary = 0

for price in totalPrices:
    summary = summary + int(price.text)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert summary == totalAmount

totalAmountAfterDiscount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

assert totalAmount > totalAmountAfterDiscount



time.sleep(2)






