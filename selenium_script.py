from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_dynamic_content():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') 
    
    print("Запускаємо браузер...")
    driver = webdriver.Chrome(options=options)

    try:
        url = "https://the-internet.herokuapp.com/dynamic_loading/2"
        print(f"Переходимо за адресою: {url}")
        driver.get(url)
        
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        print("Клікаємо на кнопку 'Start'...")
        start_button.click()
        
        print("Очікуємо завантаження контенту (імітація AJAX-запиту)...")
        wait = WebDriverWait(driver, 10)
        finished_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )
        
        result_text = finished_element.text
        print("\n--- Результат скрапінгу ---")
        print(f"Отриманий динамічний текст: '{result_text}'")
        return result_text
        
    finally:
        time.sleep(2) 
        driver.quit()

if __name__ == '__main__':
    scrape_dynamic_content()