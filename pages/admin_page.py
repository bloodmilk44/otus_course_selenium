from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):

    USERNAME_INPUT = (By.XPATH, "//*[@id='input-username']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='input-password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button")
    LOGOUT_BUTTON = (By.XPATH, "//*[@id='header']/div/ul/li[2]")
    DASHBOARD_MENU = (By.XPATH, "//*[@id='menu-dashboard']/a")
    TOTAL_ORDER_HEADER = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/div/div[1]")
    TOTAL_CUSTOMER_HEADER = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div[3]/div/div[1]")

    def count_admin_login_page(self):
        username_input = len(self._find_elements(self.USERNAME_INPUT))
        password_input = len(self._find_elements(self.PASSWORD_INPUT))
        login_button = len(self._find_elements(self.LOGIN_BUTTON))
        return (username_input, password_input, login_button)

    def login_admin(self):
        username_input = self._find_element(self.USERNAME_INPUT)
        username_input.send_keys("user")
        password_input = self._find_element(self.PASSWORD_INPUT)
        password_input.send_keys("bitnami")
        login_button = self._find_element(self.LOGIN_BUTTON)
        login_button.click()

    def count_admin_is_autorization_page_elements(self):
        try:
            element = self._presence_of_element_located(self.LOGOUT_BUTTON)
        finally:
            dashboard_menu = len(self._find_elements(self.DASHBOARD_MENU))
            total_order_header = len(self._find_elements(self.TOTAL_ORDER_HEADER))
            total_customer_header = len(self._find_elements(self.TOTAL_CUSTOMER_HEADER))
            logout_button = len(self._find_elements(self.LOGOUT_BUTTON))
            return (dashboard_menu, total_customer_header, total_order_header, logout_button)

    def logout(self):
        logout_button = self._find_element(self.LOGOUT_BUTTON)
        logout_button.click()

    def count_admin_page_before_logout(self):
        try:
            element = self._presence_of_element_located(self.USERNAME_INPUT)
        finally:
            password_input = len(self._find_elements(self.PASSWORD_INPUT))
            return password_input


