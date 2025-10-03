from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from helpers.waitForElement import waitHelper
from helpers.clickElement import wait_and_click
from faker import Faker
import xpaths.xpath_web as locs
import pytest
import time

fake = Faker()

@scenario('../features/login.feature', 'User login to website')
def test_scenario_login():
    pass

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    # using incognito related to popup from google chrome
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@given("user on login page")
def step_impl(browser):
    browser.get('https://esuite.edot.id/')
    time.sleep(5)
    locator_email = locs.locators["button_email"]
    browser.find_element(*locator_email).click()
    time.sleep(5)

@when(parsers.parse("user input {username} and {password}"))
def step_input_credentials(browser, username, password):
    # username
    locator_username = locs.locators["textbox_username"]
    browser.find_element(*locator_username).send_keys(username)
    time.sleep(2)

    # click login
    locator_login = locs.locators["button_login"]
    browser.find_element(*locator_login).click()
    time.sleep(2)

    # password
    locator_password = locs.locators["textbox_password"]
    browser.find_element(*locator_password).send_keys(password)
    time.sleep(2)

    # click login again
    browser.find_element(*locator_login).click()
    time.sleep(2)


@then(parsers.parse("user {status} logged in"))
def verify_login(browser, status):
    if status in ["successfully", "success"]:
        home_menu = waitHelper(browser, locs.locators["text_home"])
        companies_menu = waitHelper(browser, locs.locators["text_companies"])
        assert home_menu.is_displayed()
        assert companies_menu.is_displayed()

    elif status in ["failed", "unsuccessfully"]:
        error_login = waitHelper(browser, locs.locators["error_password"])
        assert error_login.is_displayed()

    else:
        raise ValueError(f"Unknown outcome: {status}")

@scenario('../features/login.feature', 'User login with unregistered user')
def test_scenario_login_unregistered(browser):
    pass

@when(parsers.parse("user click {locator_name}"))
def step_impl(browser, locator_name):
    locator = locs.locators.get(locator_name)
    if not locator:
        raise ValueError(f"Locator '{locator_name}' not found in xpath_login.py")
    wait_and_click(browser, locator)

@when(parsers.parse("user input unregistered {username}"))
def step_impl(browser, username):
    if username.lower() in ["random", "auto", "faker"]:
        username = fake.email()
    locator_username = locs.locators["textbox_username"]
    browser.find_element(*locator_username).send_keys(username)
    time.sleep(2)
    locator_login = locs.locators["button_login"]
    browser.find_element(*locator_login).click()
    time.sleep(2)

@then("user gets popup message to register")
def step_impl(browser):
    locator_unregistered = waitHelper(browser, locs.locators["text_unregistered"])
    locator_continue_register = waitHelper(browser, locs.locators["text_continue_register"])
    locator_btn_register = waitHelper(browser, locs.locators["button_register"])
    locator_btn_edit = waitHelper(browser, locs.locators["button_edit"])
    assert locator_unregistered.is_displayed()
    assert locator_continue_register.is_displayed()
    assert locator_btn_register.is_displayed()
    assert locator_btn_edit.is_displayed()

@scenario('../features/login.feature', 'User login with invalid format email')
def test_scenario_login_invalid_format_email(browser):
    pass

@when("user input invalid format email")
def step_invalid_format_email(browser):
    locator_username = locs.locators["textbox_username"]
    browser.find_element(*locator_username).send_keys("test@test")
    time.sleep(2)

@then("user get error message")
def step_impl(browser):
    locator_invalid_format_email = waitHelper(browser, locs.locators["text_invalid_format_email"])
    assert locator_invalid_format_email.is_displayed()

