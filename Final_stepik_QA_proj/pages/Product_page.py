from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def go_to_basket(self):
        basket_but = self.browser.find_element(*ProductPageLocators.BASK_BUT)
        basket_but.click()
    
    def should_be_equal_name(self, name):
        prod_name = self.browser.find_element(*ProductPageLocators.NAME_LOC)
        assert prod_name.text == name, "Product name is wrong"
    
    def should_be_equal_price(self, price):
        prod_price = self.browser.find_element(*ProductPageLocators.PRICE_LOC)
        assert  prod_price.text == price, "Price is wrong"
    
    def get_prod_name(self):
        name = self.browser.find_element(*ProductPageLocators.PROD_NAME)
        return name.text

    def get_prod_price(self):
        price = self.browser.find_element(*ProductPageLocators.PROD_PRICE)
        return price.text
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"