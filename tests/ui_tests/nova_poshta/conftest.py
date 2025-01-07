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
    tracking_page.check_is_correct_url()
    return tracking_page