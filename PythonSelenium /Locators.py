import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"email").send_keys("ilham@gmail.com")

driver.find_element(By.ID,"exampleInputPassword1").send_keys("salam123@")

driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("IlhamAliyev")

successMessage = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success" in successMessage

print(successMessage)







time.sleep(2)