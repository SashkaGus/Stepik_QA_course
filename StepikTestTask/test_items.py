from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    browser.get(link)
    assert True == browser.find_element(By.CSS_SELECTOR, "button.btn-lg").is_enabled(), "Button is unavailable"

