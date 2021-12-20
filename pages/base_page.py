from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    _time = 10

    def __init__(self, browser):
        self.browser = browser

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, self.browser.t) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        element.click()

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(element)

    def click_link(self, link_text):
        self._click((By.LINK_TEXT, link_text))
        return self

    def _find_element(self, locator, time=_time):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def _find_elements(self, locator, time=_time):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def _find_element_to_visibility_of_element_located(self, locator, time=_time):
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def _find_element_to_ivisibility_of_element_located(self, locator, time=_time):
        return WebDriverWait(self.browser, time).until(EC.invisibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def _presence_of_element_located(self, locator, time=_time):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")