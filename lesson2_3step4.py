from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажимаем кнопку
    browser.find_element(By.TAG_NAME, "button").click()

    # Принимаем confirm
    alert = browser.switch_to.alert
    alert.accept()

    # ЖДЁМ появления x
    x_element = wait.until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = x_element.text

    answer = calc(x)

    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.TAG_NAME, "button").click()

    # Получаем финальный alert с ответом
    alert = browser.switch_to.alert
    print("Ответ для Stepik:", alert.text)
    alert.accept()

finally:
    browser.quit()
