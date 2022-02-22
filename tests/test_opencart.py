import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_opencart_url(browser, base_url):
    browser.get(url=base_url)
    url_name = browser.current_url
    assert url_name == base_url

def test_opencart_base_page_element(browser, base_url):
    browser.get(url=base_url)
    store_logo = len(browser.find_elements(By.XPATH, "//*[@id='logo']/a/img"))
    search_line = len(browser.find_elements(By.XPATH, "//*[@id='search']/input"))
    search_button = len(browser.find_elements(By.XPATH, "//*[@id='search']/span/button"))
    phone_number = len(browser.find_elements(By.XPATH, "//*[@class='hidden-xs hidden-sm hidden-md'][text()='123456789']"))  # Такой селектор выбран в том числе для проверки правильности номера телефона на стренице
    cart_button = len(browser.find_elements(By.XPATH, "//*[@id='cart']/button"))
    navbar = len(browser.find_elements(By.XPATH, "//*[@class='collapse navbar-collapse navbar-ex1-collapse']"))
    assert store_logo == 1
    assert search_line == 1
    assert search_button == 1
    assert phone_number == 1
    assert cart_button == 1
    assert navbar == 1

def test_opencart_product_category_20_page_element(browser, base_url):
    browser.get(url=base_url + "index.php?route=product/category&path=20")
    store_logo = len(browser.find_elements(By.XPATH, "//*[@id='logo']/a/img"))
    search_line = len(browser.find_elements(By.XPATH, "//*[@id='search']/input"))
    search_button = len(browser.find_elements(By.XPATH, "//*[@id='search']/span/button"))
    cart_button = len(browser.find_elements(By.XPATH, "//*[@id='cart']/button"))
    navbar = len(browser.find_elements(By.XPATH, "//*[@class='collapse navbar-collapse navbar-ex1-collapse']"))
    list_group = len(browser.find_elements(By.XPATH, "//*[@class='list-group']"))
    list_view_button = len(browser.find_elements(By.XPATH, "//*[@id='list-view']"))
    grid_view_button = len(browser.find_elements(By.XPATH, "//*[@id='grid-view']"))
    assert store_logo == 1
    assert search_line == 1
    assert search_button == 1
    assert cart_button == 1
    assert navbar == 1
    assert list_group == 1
    assert list_view_button == 1
    assert grid_view_button == 1

def test_opencart_product_id_49_page_element(browser, base_url):
    browser.get(url=base_url + "index.php?route=product/product&path=57&product_id=49")
    product_thumb = len(browser.find_elements(By.XPATH, "//*[@class='thumbnails']"))
    favorite_button = len(browser.find_elements(By.XPATH, "//*[@data-original-title='Add to Wish List']"))
    product_name = len(browser.find_elements(By.XPATH, "//*[@id='content']/descendant::h1"))
    add_to_cart_button = len(browser.find_elements(By.XPATH, "//*[@id='button-cart']"))
    store_logo = len(browser.find_elements(By.XPATH, "//*[@id='logo']/a/img"))
    search_line = len(browser.find_elements(By.XPATH, "//*[@id='search']/input"))
    search_button = len(browser.find_elements(By.XPATH, "//*[@id='search']/span/button"))
    assert product_thumb == 1
    assert favorite_button == 1
    assert product_name == 1
    assert add_to_cart_button == 1
    assert store_logo == 1
    assert search_line == 1
    assert search_button == 1

def test_opencart_account_login_page_element(browser, base_url):
    browser.get(url=base_url + "index.php?route=account/login")
    continue_registration_button = len(browser.find_elements(By.XPATH, "//*[@class='btn btn-primary'][text()=('Continue')]"))
    email_input = len(browser.find_elements(By.XPATH, "//*[@id='input-email']"))
    password_input = len(browser.find_elements(By.XPATH, "//*[@id='input-password']"))
    login_button = len(browser.find_elements(By.XPATH, "//input[@value='Login']"))
    store_logo = len(browser.find_elements(By.XPATH, "//*[@id='logo']/a/img"))
    search_line = len(browser.find_elements(By.XPATH, "//*[@id='search']/input"))
    search_button = len(browser.find_elements(By.XPATH, "//*[@id='search']/span/button"))
    assert continue_registration_button == 1
    assert email_input == 1
    assert password_input == 1
    assert login_button == 1
    assert store_logo == 1
    assert search_line == 1
    assert search_button == 1

def test_opencart_admin_login_page_element(browser, base_url):
    browser.get(url=base_url + "admin/")
    username_input = len(browser.find_elements(By.XPATH, "//*[@id='input-username']"))
    password_input = len(browser.find_elements(By.XPATH, "//*[@id='input-password']"))
    login_button = len(browser.find_elements(By.XPATH, "//*[@class='btn btn-primary']"))
    assert username_input == 1
    assert password_input == 1
    assert login_button == 1

def test_opencart_admin_login_page(browser, base_url):
    browser.get(url=base_url + "admin/")
    username_input = browser.find_element(By.XPATH, "//*[@id='input-username']")
    username_input.send_keys("user")
    password_input = browser.find_element(By.XPATH, "//*[@id='input-password']")
    password_input.send_keys("bitnami")
    login_button = browser.find_element(By.XPATH, "//*[@class='btn btn-primary']")
    login_button.click()
    try:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   "//*[@id='user-profile']")))
    finally:
        dashboard_menu = len(browser.find_elements(By.XPATH, "//*[@id='menu-dashboard']/a"))
        total_order_header = len(browser.find_elements(By.XPATH,
                                                       "//*[@class='tile-heading'][text()=('Total Orders ')]"))  # Пробел в содержимом тексте содержится в локаторе елемента на странице
        total_customer_header = len(browser.find_elements(By.XPATH,
                                                          "//*[@class='tile-heading'][text()=('Total Customers ')]"))  # Пробел в содержимом тексте содержится в локаторе елемента на странице
        logout_button = len(browser.find_elements(By.XPATH, "//*[@class='fa fa-sign-out']/parent::a"))
        assert dashboard_menu == 1
        assert total_order_header == 1
        assert total_customer_header == 1
        assert logout_button == 1
        logout_button = browser.find_element(By.XPATH, "//*[@class='fa fa-sign-out']/parent::a")
        logout_button.click()
    try:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   "//*[@id='input-username']")))
    finally:
        password_input = len(browser.find_elements(By.XPATH, "//*[@id='input-password']"))
        assert password_input == 1

