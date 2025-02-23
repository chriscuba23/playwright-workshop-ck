from playwright.sync_api import sync_playwright
from tests.page_objects.login_page import LoginPage

def test_login_successful():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.navigate_to_login_page()
        login_page.fill_username("student")
        login_page.fill_password("Password123")
        login_page.click_submit()

        assert login_page.is_logged_in_successfully()

        browser.close()

def test_login_wrong_username():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.navigate_to_login_page()
        login_page.fill_username("wrong_username")
        login_page.fill_password("Password123")
        login_page.click_submit()

        assert login_page.get_error_message() == "Your username is invalid!"

        browser.close()
