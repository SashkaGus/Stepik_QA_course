from selenium.webdriver.common.by import By

from Final_stepik_QA_proj.pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    #http://selenium1py.pythonanywhere.com/en-gb/accounts/login/
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    #"http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_login_page()
    page.should_be_login_url()