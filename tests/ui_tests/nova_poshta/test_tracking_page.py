from all_lessons.lesson_27.nova_poshta.pages.tracking_package_page import TrackingPackagePage
from selenium.webdriver import Chrome

import pytest


@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.close()


@pytest.fixture()
def tracking_page(driver):
    tracking_page = TrackingPackagePage(driver)
    tracking_page.open_page()
    return tracking_page


def test_tracking_page_is_opened_and_set_existing_tracking_num(driver, tracking_page):
    tracking_page.set_package_num('20451033979291').click_search_btn()
    tracking_page.success_tracking_number()


def test_wrong_tracking_num(driver, tracking_page):
    tracking_page.set_package_num('9876543219655').click_search_btn()
    tracking_page.error_tracking_text()

