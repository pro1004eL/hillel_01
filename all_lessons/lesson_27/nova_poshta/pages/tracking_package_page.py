from all_lessons.lesson_27.nova_poshta.locators.tracking_package_page import TrackingPackagePageLocators
from all_lessons.lesson_27.nova_poshta.pages.base_page import BasePage
from settings import settings


class TrackingPackagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = settings.NOVA_POSHTA_SEARCH_NUM_URL
        self.locators = TrackingPackagePageLocators()

    def _package_num_input(self):
        return self._input_field(self.locators.package_number_input_locator,
                                 message='Can`t find number package input at Tracking Page')

    def _search_num_btn(self):
        return self._btn(self.locators.search_package_number_btn_locator,
                         message='Can`t find search btn at Tracking Page', timeout=3)

    def set_package_num(self, package_num):
        self._package_num_input().send_keys(package_num)
        return self

    def click_search_btn(self):
        self._search_num_btn().click()
        return self

    def success_tracking_number(self):
        return self._present_text(self.locators.success_text_element,'Отримана')

    def error_tracking_text(self):
        return self._present_text(self.locators.error_text_element,"Ми не знайшли посилку за таким номером.")

