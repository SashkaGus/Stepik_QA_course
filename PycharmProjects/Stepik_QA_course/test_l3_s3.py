import pytest
import time
import math
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', [    "https://stepik.org/lesson/236895/step/1",
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"])                            
class TestClass:
    def test_guest_should_see_login_link(self, browser, link):
        link = f"{link}"
        browser.get(link)
        browser.implicitly_wait(10)
        input1 = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
        input1.send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click() 
        browser.implicitly_wait(10)
        welcome_text = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        print(welcome_text.text)
        unittest.TestCase.assertEqual("Correct!",  welcome_text.text, welcome_text.text)
