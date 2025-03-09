import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.CSS_SELECTOR, ".forgot-password-link").click()

driver.find_element(By.XPATH, "//form/div[1]/input[@type='email']").send_keys("demo@gmail.com")

driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input[type='password']").send_keys("salam123")

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("salam123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(2)

