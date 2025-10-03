import allure
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    outcome = yield
    driver = request.getfixturevalue("browser")
    if driver:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"Failure at step: {step.name}",
            attachment_type=allure.attachment_type.PNG
        )