from selenium.webdriver.common.by import By

from pageObjects.Checkout_Confirmation import Checkout_Confirmation
from utils.browserUtils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.product_cards = (By.CSS_SELECTOR, "div[class$='card h-100']")
        self.checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def add_product_to_card(self,product_name):
        productCards = self.driver.find_elements(*self.product_cards)

        for productCard in productCards:
            productName = productCard.find_element(By.CSS_SELECTOR, "div h4").text
            if productName == product_name:
                productCard.find_element(By.CSS_SELECTOR, "div button").click()

    def goToCart(self):

        self.driver.find_element(*self.checkout_button).click()

        checkout_confirmation = Checkout_Confirmation(self.driver)

        return checkout_confirmation