from selenium.webdriver.common.by import By


class SignInPageLocators:
    signin_btn_locator = (By.XPATH, "//button[@class='btn btn-outline-white header_signin']")
    registration_btn_locator = (By.XPATH, "//div[@class='modal-footer d-flex justify-content-between']/button[1]")

    # registration form
    signupName_input_locator = (By.XPATH, "//input[@id='signupName']")
    name_input_locator = (By.ID, "signupName")
    last_name_input_locator = (By.ID, "signupLastName")
    email_input_locator = (By.ID, "signupEmail")
    pwd_input_locator = (By.ID, "signupPassword")
    confirm_pwd_input_locator = (By.ID, "signupRepeatPassword")
    register_btn_locator = (By.CSS_SELECTOR, "div.modal-footer > button")

    success_text_element = (By.CSS_SELECTOR, "div.alert.alert-success")