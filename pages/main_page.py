from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    STORE_LOGO = (By.XPATH, "//*[@id='logo']/a/img")
    SEARCH_LINE = (By.XPATH, "//*[@id='search']/input")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search']/span/button")
    PHONE_NUMBER = (By.XPATH, "//*[@id='top-links']/ul/li[1]/span")
    CART_BUTTON = (By.XPATH, "//*[@id='cart']/button")
    NAVBAR = (By.XPATH, "//*[@id='menu']/div[2]")
    LIST_GROUP = (By.XPATH, "//*[@id='column-left']/div[1]")
    LIST_VIEW_BUTTON = (By.XPATH, "//*[@id='list-view']")
    GRID_VIEW_BUTTON = (By.XPATH, "//*[@id='grid-view']")
    PRODUCT_THUMB = (By.XPATH, "//*[@id='content']/div/div[1]/ul[1]")
    FAVORITE_BUTTON = (By.XPATH, "//*[@id='content']/div/div[2]/div[1]/button[1]")
    PRODUCT_NAME = (By.XPATH, "//*[@id='content']/div/div[2]/h1")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='button-cart']")
    CONTINUE_REGISTRATION_BUTTON = (By.XPATH, "//*[@id='content']/div/div[1]/div/a")
    EMAIL_INPUT = (By.XPATH, "//*[@id='input-email']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='input-password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='content']/div/div[2]/div/form/input")

    def count_element_main_page(self):
        store_logo = len(self._find_elements(self.STORE_LOGO))
        search_line = len(self._find_elements(self.SEARCH_LINE))
        search_button = len(self._find_elements(self.SEARCH_BUTTON))
        phone_number = len(self._find_elements(self.PHONE_NUMBER))
        cart_button = len(self._find_elements(self.CART_BUTTON))
        navbar = len(self._find_elements(self.NAVBAR))
        return (store_logo, search_line, search_button, phone_number, cart_button, navbar)

    def count_element_category_20_page(self):
        store_logo = len(self._find_elements(self.STORE_LOGO))
        search_line = len(self._find_elements(self.SEARCH_LINE))
        search_button = len(self._find_elements(self.SEARCH_BUTTON))
        phone_number = len(self._find_elements(self.PHONE_NUMBER))
        cart_button = len(self._find_elements(self.CART_BUTTON))
        navbar = len(self._find_elements(self.NAVBAR))
        list_group = len(self._find_elements(self.LIST_GROUP))
        list_view_button = len(self._find_elements(self.LIST_VIEW_BUTTON))
        grid_view_button = len(self._find_elements(self.GRID_VIEW_BUTTON))
        return (store_logo, search_line, search_button, phone_number, cart_button, navbar, list_group,
                                                                        list_view_button, grid_view_button)

    def count_element_product_id_49_page(self):
        product_thumb = len(self._find_elements(self.PRODUCT_THUMB))
        favorite_button = len(self._find_elements(self.FAVORITE_BUTTON))
        product_name = len(self._find_elements(self.PRODUCT_NAME))
        add_to_cart_button = len(self._find_elements(self.ADD_TO_CART_BUTTON))
        store_logo = len(self._find_elements(self.STORE_LOGO))
        search_line = len(self._find_elements(self.SEARCH_LINE))
        search_button = len(self._find_elements(self.SEARCH_BUTTON))
        phone_number = len(self._find_elements(self.PHONE_NUMBER))
        return (product_thumb, favorite_button, product_name, add_to_cart_button, store_logo, search_line,
                                                                                search_button, phone_number)

    def count_account_login_page_element(self):
        store_logo = len(self._find_elements(self.STORE_LOGO))
        search_line = len(self._find_elements(self.SEARCH_LINE))
        search_button = len(self._find_elements(self.SEARCH_BUTTON))
        continue_registration_button = len(self._find_elements(self.CONTINUE_REGISTRATION_BUTTON))
        email_input = len(self._find_elements(self.EMAIL_INPUT))
        password_input = len(self._find_elements(self.PASSWORD_INPUT))
        login_button = len(self._find_elements(self.LOGIN_BUTTON))
        return (store_logo, search_line, search_button, continue_registration_button, email_input,
                                                                                password_input, login_button)