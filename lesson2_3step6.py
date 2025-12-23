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
    # 1. Открываем страницу
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # 2. Запоминаем текущую вкладку
    original_window = browser.current_window_handle

    # 3. Нажимаем кнопку
    browser.find_element(By.TAG_NAME, "button").click()

    # 4. Ждём появления новой вкладки
    wait.until(EC.number_of_windows_to_be(2))

    # 5. Переключаемся на новую вкладку
    for window_handle in browser.window_handles:
        if window_handle != original_window:
            browser.switch_to.window(window_handle)
            break

    # 6. Решаем капчу
    x = wait.until(
        EC.presence_of_element_located((By.ID, "input_value"))
    ).text

    answer = calc(x)

    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.TAG_NAME, "button").click()

    # 7. Получаем ответ
    alert = browser.switch_to.alert
    print("Ответ для Stepik:", alert.text)
    alert.accept()

finally:
    browser.quit()
