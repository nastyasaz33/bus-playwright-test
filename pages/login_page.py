from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('[data-qa="sign-in-email-input"]')
        self.password_input = page.locator('[data-qa="sign-in-password-input"]')
        self.sign_button = page.locator('[data-qa="sign-in-form-button"]')
        self.error_message = page.locator('[data-qa="not-valid-pass"]')

    def open_login_page(self, url):
        """Метод для открытия страницы"""
        self.page.goto(url)

    def sign_in(self, email, password):
        """Метод для заполнения формы и нажатия кнопки авторизации"""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.sign_button.click()

    def check_login_error(self, expected_text):
        """Метод для проверки ошибки при авторизации"""
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_text)
