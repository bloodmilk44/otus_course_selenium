import pytest

from selenium import webdriver
from pages.app import Application

def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser window")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox"], help="Browser", default="chrome")
    parser.addoption("--url", action="store", default="http://localhost/", help="This is request url")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception("No such browser")

    def fin():
        driver.close()

    if maximized:
        driver.maximize_window()
    request.addfinalizer(fin)

    return driver

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='module')
def app(browser):
    return Application(browser)

#@pytest.fixture(scope='module')
#def open_main_page(app):
