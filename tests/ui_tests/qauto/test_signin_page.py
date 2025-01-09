
def test_user_registration_positive(driver, signin_page):

    signin_page.click_signin_btn()
    signin_page.click_registration_btn()
    signin_page.fill_registration_form()
    signin_page.click_register_btn()
    signin_page.check_is_success_text()
    signin_page.check_is_expected_redirect_url()

