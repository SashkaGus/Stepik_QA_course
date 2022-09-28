from Final_stepik_QA_proj.pages.base_page import BasePage
from Final_stepik_QA_proj.pages.locators import BasePageLocators


class BasketPage(BasePage):
   
    def basket_should_be_empty(self):
        basket_fill = self.browser.find_element(*BasePageLocators.EMPTY_TEXT)
        assert basket_fill, "Basket isn't empty"
