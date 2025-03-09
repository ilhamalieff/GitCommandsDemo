import json

import pytest

from pageObjects.login import LoginPage


test_data_path = "../data/test_e2eTestFramework.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):

    driver = browserInstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    login_page = LoginPage(driver)

    print(login_page.getTitle())

    shopPage = login_page.Login(test_list_item["userEmail"],test_list_item["userPassword"])

    shopPage.add_product_to_card(test_list_item["productName"])

    print(shopPage.getTitle())

    checkout_confirmation = shopPage.goToCart()

    checkout_confirmation.checkout()

    checkout_confirmation.add_delivery_address("Azer")

    checkout_confirmation.validate_error()





