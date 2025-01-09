from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self._driver = driver  # на пряму цей драйвер використовувати не потрібно
        self.url = None

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    def check_is_correct_url(self):
        assert self._driver.current_url == self.url, (f'Expected url is {self.url}, '
                                                      f'but actual url is {self._driver.current_url}')

    def _input_field(self, locator, timeout=1, message=''):
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=message)

    def _btn(self, locator, timeout=1, message=''):
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(locator), message=message)

    def _present_text(self, locator, text, timeout=3, message=''):
        return WebDriverWait(self._driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text), message=message)

    def _wait_for_redirection(self, expected_url, timeout=3, message=''):
        WebDriverWait(self._driver, timeout).until(EC.url_to_be(expected_url), message=message)
        return self._driver.current_url
