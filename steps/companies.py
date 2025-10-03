from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from helpers.waitForElement import waitHelper
from helpers.select_dropdown import select_dropdown
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helpers.clickElement import wait_and_click
from faker import Faker
import xpaths.xpath_web as locs
import pytest
import time

fake = Faker()
pytest_plugins = [
    "steps.login",
    "steps.companies"# <--- import login steps# <--- you can add more step files
]

@scenario('../features/companies.feature', 'User add new companies')
def test_scenario_companies():
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

@when("user choose companies button")
def click_companies_button(browser):
    home_menu = waitHelper(browser, locs.locators["text_home"])
    companies_menu = waitHelper(browser, locs.locators["text_companies"])
    assert home_menu.is_displayed()
    assert companies_menu.is_displayed()
    companies_menu.click()
    time.sleep(5)
    companies_button = waitHelper(browser, locs.locators["button_company"])
    assert companies_button.is_displayed()
    companies_button.click()
    time.sleep(5)

@then("user complete form companies")
def step_complete_form_companies(browser):
    company_name = waitHelper(browser, locs.locators["textbox_company_name"])
    company_name.send_keys(fake.company())
    email_company = waitHelper(browser, locs.locators["textbox_email_company"])
    email_company.send_keys(fake.email())
    time.sleep(5)
    phone = waitHelper(browser, locs.locators["textbox_phone_company"])
    phone.send_keys("812377700")

    select_dropdown(browser, locs.locators["dropdown_industry_type"], "Manufacturing")
    select_dropdown(browser, locs.locators["dropdown_company_type"], "Marketplace")
    select_dropdown(browser, locs.locators["dropdown_language"], "English")
    address = waitHelper(browser, locs.locators["textbox_address_company"])
    address.send_keys(fake.address())
    select_dropdown(browser, locs.locators["dropdown_country"], "Indonesia")

    # Still error when select province
    select_dropdown(browser, locs.locators["dropdown_province"], "MALUKU")
    search_input = waitHelper(browser, By.XPATH, "//input[@placeholder='Search']")
    search_input.clear()
    search_input.send_keys("MALUKU")
    select_dropdown(browser, locs.locators["dropdown_city"], "KOTA AMBON")
    select_dropdown(browser, locs.locators["dropdown_district"], "TELUK AMBON")
    select_dropdown(browser, locs.locators["dropdown_subdistrict"], "TAWIRI")
    button_next = waitHelper(browser, locs.locators["button_next"])
    button_next.click()
    time.sleep(5)

