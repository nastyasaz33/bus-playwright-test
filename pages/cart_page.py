from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_counter = page.locator('[data-qa="header-cart-counter"]')
        self.item_in_cart = page.locator('[data-qa="cart-item-wrapper-0"]')
        self.employee_in_item = page.locator('[data-qa="cart-paid-seats-employee"]')
        self.first_employee_in_item = page.locator('[data-qa="cart-employee-suggest-first-el"]')
        self.cart_payment_button_disabled = page.locator('[data-qa="cart-payment-button-disabled"]')
        self.cart_payment_button_enabled = page.locator('[data-qa="cart-payment-button-enabled"]')
        self.cart_delete_all_title = page.locator('[data-qa="cart-delete-all-title"]')
        self.cart_delete_all_modal_success = page.locator('[data-qa="cart-delete-all-modal-success"]')
        self.cart_empty = page.locator('[data-qa="cart-empty"]')

    def clear_cart(self):
        """Очищение непустой корзины"""
        expect(self.cart_empty.or_(self.item_in_cart.first)).to_be_visible(timeout=10000)
        if self.cart_empty.is_visible():
            return
        
        expect(self.item_in_cart.first).to_be_visible()
        self.cart_delete_all_title.click()
        expect(self.cart_delete_all_modal_success).to_be_visible()
        self.cart_delete_all_modal_success.click()
        
        expect(self.cart_empty).to_be_visible(timeout=10000)

    def check_bus_in_cart(self):
        """Успешное добавление автобусного билета в корзину"""
        expect(self.cart_counter).to_be_visible()
        expect(self.item_in_cart).to_be_visible()

