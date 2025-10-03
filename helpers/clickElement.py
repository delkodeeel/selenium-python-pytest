from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_click(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()
    return element