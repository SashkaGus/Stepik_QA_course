from .base_page import BasePage
from .locators import LoginPageLocators
import re
import faker

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
    
    def register_new_user(self, user_email, user_password):
        email_reg = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_reg = self.browser.find_element(*LoginPageLocators.PASSW_FIELD)
        password_check = self.browser.find_element(*LoginPageLocators.PASSW_CHECK)
        email_reg.send_keys(user_email)
        password_reg.send_keys(user_password)
        password_check.send_keys(user_password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTT)
        reg_button.click()
        