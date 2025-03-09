from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browserUtils import BrowserUtils


class Checkout_Confirmation(BrowserUtils):
    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver
        self.checkbox_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_option = (By.LINK_TEXT, "Azerbaijan")
        self.checkout_button = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.success_button = (By.CSS_SELECTOR, "input[class$='btn btn-success btn-lg']")
        self.success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")



    def checkout(self):

        self.driver.find_element(*self.checkbox_button).click()

    def add_delivery_address(self,country_name):

        self.driver.find_element(By.ID, "country").send_keys(country_name)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.country_option))

        self.driver.find_element(*self.country_option).click()

        self.driver.find_element(*self.checkout_button).click()

        self.driver.find_element(*self.success_button).click()


    def validate_error(self):
        successMessage = self.driver.find_element(*self.success_message).text

        assert "Success! Thank you!" in successMessage