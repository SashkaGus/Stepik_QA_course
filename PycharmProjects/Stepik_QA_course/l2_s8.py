from hashlib import new
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = browser.find_element(By.CSS_SELECTOR, "h5#price")
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )

    but1 = browser.find_element(By.CSS_SELECTOR, 'button#book')
    but1.click()
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    input1.send_keys(y)

    but2 = browser.find_element(By.CSS_SELECTOR, "button#solve")
    but2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла