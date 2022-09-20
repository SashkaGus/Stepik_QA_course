from .pages.base_page import BasePage
from .pages.main_page import MainPage
import pytest
import time

# @pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i=='?', reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_name(name=page.get_prod_name())
    page.should_be_equal_price(price=page.get_prod_price())