from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    


class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "form#register_form")
    LOG_FORM = (By.CSS_SELECTOR, "form#login_form")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    BASK_BUT = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_LOC = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE_LOC = (By.CSS_SELECTOR, "div.alertinner p strong")
    PROD_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PROD_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUT = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)") 
    EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner > p")  