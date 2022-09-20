from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASK_BUT = (By.CSS_SELECTOR, "button.btn-add-to-basket")

class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "form#register_form")
    LOG_FORM = (By.CSS_SELECTOR, "form#login_form")