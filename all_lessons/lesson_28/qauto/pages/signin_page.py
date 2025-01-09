from all_lessons.lesson_28.qauto.locators.signin_page import SignInPageLocators
from all_lessons.lesson_28.qauto.pages.base_page import BasePage
from settings import settings
from faker import Faker


class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = settings.QAUTO_BASE_API_URL
        self.locators = SignInPageLocators()
        self.faker = Faker()


    def _signin_btn(self):
        return self._btn(self.locators.signin_btn_locator,
                         message='Can`t find signin button at SignIn Page', timeout=2)

    def _registration_btn(self):
        return self._btn(self.locators.registration_btn_locator,
                         message='Can`t find registration button at SignIn Page', timeout=2)

    def _register_btn(self):
        return self._btn(self.locators.register_btn_locator,
                         message='Can`t find register button at SignIn Page', timeout=2)

    def click_signin_btn(self):
        self._signin_btn().click()
        return self

    def click_registration_btn(self):
        self._registration_btn().click()
        return self

    def click_register_btn(self):
        self._register_btn().click()
        return self

    def check_is_success_text(self):
        return self._present_text(self.locators.success_text_element,'Registration complete',
                                  message="Expected success text was not found on the page.")

    def fill_registration_form(self, name=None, last_name=None, email=None, password=None, confirm_password=None):
        name = name or self.faker.first_name()
        last_name = last_name or self.faker.last_name()
        email = email or self.faker.email()
        password = password or "SomePassword!"
        confirm_password = confirm_password or password

        fields = {
            self.locators.name_input_locator: name,
            self.locators.last_name_input_locator: last_name,
            self.locators.email_input_locator: email,
            self.locators.pwd_input_locator: password,
            self.locators.confirm_pwd_input_locator: confirm_password
        }

        for locator, value in fields.items():
            element = self._input_field(locator, timeout=5)
            element.clear()
            element.send_keys(value)

    def check_is_expected_redirect_url(self):
        expected_url = "https://guest:welcome2qauto@qauto2.forstudy.space/panel/garage"
        current_url = self._wait_for_redirection(expected_url)
        assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
