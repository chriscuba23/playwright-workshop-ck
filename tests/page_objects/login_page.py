from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practicetestautomation.com/practice-test-login/"

    # Locators
    USERNAME_LOCATOR = "#username"
    PASSWORD_LOCATOR = "#password"
    SUBMIT_BUTTON_LOCATOR = "#submit"
    SUCCESS_MESSAGE_LOCATOR = "text=Logged In Successfully"
    ERROR_MESSAGE_LOCATOR = "#error"

    # Actions
    def navigate_to_login_page(self):
        self.page.goto(self.url)

    def fill_username(self, username: str):
        self.page.locator(self.USERNAME_LOCATOR).fill(username)

    def fill_password(self, password: str):
        self.page.locator(self.PASSWORD_LOCATOR).fill(password)

    def click_submit(self):
        self.page.locator(self.SUBMIT_BUTTON_LOCATOR).click()

    def is_logged_in_successfully(self) -> bool:
        return self.page.locator(self.SUCCESS_MESSAGE_LOCATOR).is_visible()

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE_LOCATOR).inner_text()
