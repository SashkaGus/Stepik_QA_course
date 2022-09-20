from .base_page import BasePage
from .locators import LoginPageLocators
import re

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # assert True
        url = self.browser.current_url
        assert re.search(r"login", str(url)), f"URL addres invalid: {url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # assert True
        assert self.is_element_present(*LoginPageLocators.LOG_FORM), "login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # assert True
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "registration form is not presented"