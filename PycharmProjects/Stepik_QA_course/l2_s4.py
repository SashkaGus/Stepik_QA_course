# http://suninjuly.github.io/execute_script.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    y = calc(a.text)
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    chkbx1 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    chkbx1.click()
    rdbtn1 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rdbtn1)
    rdbtn1.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()