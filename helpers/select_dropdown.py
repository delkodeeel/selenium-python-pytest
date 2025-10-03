from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def select_dropdown(driver, locator, value, timeout=10):
    dropdown = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
    dropdown.click()

    option_locator = (By.XPATH, f"//span[contains(text(), '{value}')]")
    option = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(option_locator)
    )
    option.click()

