import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeDriver = webdriver.Chrome()

chromeDriver.get("https://rahulshettyacademy.com/angularpractice/")

chromeDriver.implicitly_wait(5)

chromeDriver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()

productCards = chromeDriver.find_elements(By.CSS_SELECTOR, "div[class$='card h-100']")

for productCard in productCards:
    productName = productCard.find_element(By.CSS_SELECTOR, "div h4").text
    if productName == "Nokia Edge":
        productCard.find_element(By.CSS_SELECTOR, "div button").click()

chromeDriver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

chromeDriver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

chromeDriver.find_element(By.ID, "country").send_keys("Azer")

WebDriverWait(chromeDriver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Azerbaijan")))

chromeDriver.find_element(By.LINK_TEXT, "Azerbaijan").click()

chromeDriver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

chromeDriver.find_element(By.CSS_SELECTOR, "input[class$='btn btn-success btn-lg']").click()

successMessage = chromeDriver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in successMessage

time.sleep(2)