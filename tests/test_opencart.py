from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


def test_opencart_url(browser, base_url):
    browser.get(url=base_url)
    url_name = browser.current_url
    assert url_name == base_url


def test_opencart_base_page_element(app, base_url):
    app.browser.get(url=base_url)
    element = app.get_count_element_main_page()
    assert element == (1, 1, 1, 1, 1, 1)


def test_opencart_product_category_20_page_element(app, base_url):
    app.browser.get(url=base_url + "index.php?route=product/category&path=20")
    element = app.get_count_element_category_20_page()
    assert element == (1, 1, 1, 1, 1, 1, 1, 1, 1)


def test_opencart_product_id_49_page_element(app, base_url):
    app.browser.get(url=base_url + "index.php?route=product/product&path=57&product_id=49")
    element = app.get_count_element_product_id_49_page()
    assert element == (1, 1, 1, 1, 1, 1, 1, 1)


def test_opencart_account_login_page_element(app, base_url):
    app.browser.get(url=base_url + "index.php?route=account/login")
    element = app.get_count_account_login_page_element()
    assert element == (1, 1, 1, 1, 1, 1, 1)


def test_opencart_admin_login_page_element(app, base_url):
    app.browser.get(url=base_url + "admin/")
    element = app.get_count_admin_login_page_element()
    assert element == (1, 1, 1)


def test_opencart_admin_login_page(app, base_url):
    app.browser.get(url=base_url + "admin/")
    app.login_in_admin()
    element = app.get_count_admin_page_elements()
    assert element == (1, 1, 1, 1)
    app.logout_admin()
    element_2 = app.get_count_admin_page_elements_before_logout()
    assert element_2 == 1
