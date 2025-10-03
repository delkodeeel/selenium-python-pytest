from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitHelper(driver, locator, timeout=10, condition=EC.visibility_of_element_located):
    return WebDriverWait(driver, timeout).until(condition(locator))