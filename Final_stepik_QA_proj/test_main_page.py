from selenium.webdriver.common.by import By
from Final_stepik_QA_proj.pages.basket_page import BasketPage

from Final_stepik_QA_proj.pages.login_page import LoginPage
from .pages.Product_page import ProductPage
from .pages.main_page import MainPage


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     login_page = page.go_to_login_page()
#     login_page.should_be_login_page()

# def test_guest_should_see_login_link(browser):
#     #http://selenium1py.pythonanywhere.com/en-gb/accounts/login/
#     link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#     #"http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_form()
#     page.should_be_login_page()
#     page.should_be_login_url()

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_base()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()