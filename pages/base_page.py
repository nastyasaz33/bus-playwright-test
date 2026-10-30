from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page_loaded_marker = page.locator('[data-qa="app-is-loaded"]')
        self.cart = page.locator('[data-qa="header-cart"]')
        self.smartdesk = page.locator('[data-qa="header-smartdesk"]')

    def check_page_is_open(self):
        """Успешная загрузка стартовой страницы"""
        expect(self.page_loaded_marker).to_be_visible(timeout=10000)

    def open_cart(self):
        """Переход в корзину"""
        self.cart.click()

    def open_smartdesk(self):
        """Переход на смартдеск"""
        self.smartdesk.click()