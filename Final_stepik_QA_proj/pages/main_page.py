from asyncio import base_tasks
import re
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click() 

    def should_be_login_link(self):
       assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "login link is not presented"
    
    def go_to_basket(self):
        basket_but = self.browser.find_element(*MainPageLocators.BASK_BUT)
        basket_but.click()
    
    def should_be_equal_name(self, name):
        prod_name = self.browser.find_element(*MainPageLocators.NAME_LOC)
        assert prod_name.text == name, "Product name is wrong"
    
    def should_be_equal_price(self, price):
        prod_price = self.browser.find_element(*MainPageLocators.PRICE_LOC)
        assert  prod_price.text == price, "Price is wrong"
    
    def get_prod_name(self):
        name = self.browser.find_element(*MainPageLocators.PROD_NAME)
        return name.text
        
    def get_prod_price(self):
        price = self.browser.find_element(*MainPageLocators.PROD_PRICE)
        return price.text