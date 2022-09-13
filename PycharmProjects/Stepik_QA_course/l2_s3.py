# http://suninjuly.github.io/selects1.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(a, b):
  return str(int(a) + int(b))


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap")
    b = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap")
    y = calc(a.text, b.text)
    input1 = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    input1.select_by_value(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()