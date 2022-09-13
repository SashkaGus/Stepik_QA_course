from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "img#treasure").get_attribute("valuex")
    x = x_element
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)
    chkbx1 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox.check-input")
    chkbx1.click()
    rdbtn1 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule.check-input")
    rdbtn1.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()