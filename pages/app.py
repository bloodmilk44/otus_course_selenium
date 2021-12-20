from pages.main_page import MainPage
from pages.admin_page import AdminPage

class Application(object):

    def __init__(self, browser):
        self.browser = browser
        self.main_page = MainPage(browser)
        self.admin_page = AdminPage(browser)

    def get_count_element_main_page(self):
        mp = self.main_page
        element_main_page = mp.count_element_main_page()
        return element_main_page

    def get_count_element_category_20_page(self):
        mp = self.main_page
        element_main_page = mp.count_element_category_20_page()
        return element_main_page

    def get_count_element_product_id_49_page(self):
        mp = self.main_page
        element_main_page = mp.count_element_product_id_49_page()
        return element_main_page

    def get_count_account_login_page_element(self):
        mp = self.main_page
        element_main_page = mp.count_account_login_page_element()
        return element_main_page

    def get_count_admin_login_page_element(self):
        ap = self.admin_page
        element_main_page = ap.count_admin_login_page()
        return element_main_page

    def login_in_admin(self):
        ap = self.admin_page
        ap.login_admin()

    def get_count_admin_page_elements(self):
        ap = self.admin_page
        element_main_page = ap.count_admin_is_autorization_page_elements()
        return element_main_page

    def logout_admin(self):
        ap = self.admin_page
        ap.logout()

    def get_count_admin_page_elements_before_logout(self):
        ap = self.admin_page
        element_main_page = ap.count_admin_page_before_logout()
        return element_main_page