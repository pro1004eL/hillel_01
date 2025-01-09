from all_lessons.lesson_28.qauto.pages.signin_page import SignInPage
from selenium.webdriver import Chrome
import pytest


@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.close()


@pytest.fixture()
def signin_page(driver):
    signin_page = SignInPage(driver)
    signin_page.open_page()
    signin_page.check_is_correct_url()
    return signin_page