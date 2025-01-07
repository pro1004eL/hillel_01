
def test_tracking_page_is_opened_and_set_existing_tracking_num(driver, tracking_page):

    tracking_page.set_package_num('20451033979291').click_search_btn()
    tracking_page.success_tracking_number()


def test_wrong_tracking_num(driver, tracking_page):

    tracking_page.set_package_num('9876543219655').click_search_btn()
    tracking_page.error_tracking_text()
