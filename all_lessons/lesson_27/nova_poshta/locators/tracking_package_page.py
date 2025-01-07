from selenium.webdriver.common.by import By


class TrackingPackagePageLocators:
    package_number_input_locator = (By.CSS_SELECTOR, '#en')
    search_package_number_btn_locator = (By.CSS_SELECTOR, 'input.track__form-group-btn.green-active')
    success_text_element = (By.CSS_SELECTOR, 'div.header__status-text')
    error_text_element = (By.CSS_SELECTOR, "#np-number-input-desktop-message-error-message > span")