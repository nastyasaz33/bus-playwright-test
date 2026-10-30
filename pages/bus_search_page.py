from playwright.sync_api import Page, expect
from datetime import datetime, timedelta
import re

class BusSearch:
    def __init__(self, page: Page):
        self.page = page
        self.smartdesk_bus_search = page.locator('[data-qa="smartdesk-search-bus"]')
        self.search_bus_menu_cities_from = page.locator('[data-qa="search-bus-menu-cities-from"]')
        self.swap_cities_button = page.locator("button.P_CDra_swap_button")
        self.first_city_from = page.locator('[data-qa="search-bus-panel-city-from-first-el"]')
        self.search_bus_menu_cities_to = page.locator('[data-qa="search-bus-menu-cities-to"]')
        self.first_city_to = page.locator('[data-qa="search-bus-panel-city-to-first-el"]')
        self.search_bus_menu_dates_from = page.locator('[data-qa="search-bus-menu-dates-from"]')
        self.search_button = page.locator('[data-qa="search-bus-menu-search-button"]')
        self.empty_city_from = page.get_by_text("Выберите город отправления")
        self.empty_city_to = page.get_by_text("Выберите город прибытия")
        self.empty_date = page.get_by_text("Выберите даты")
        self.ticket_bus_skeleton = page.locator('[data-qa="ticket-bus-skeleton"]')
        self.ticket_bus = page.locator('[data-qa="ticket-bus"]')
        self.select_seat_button = page.get_by_role("button", name="Выбрать место")
        self.search_bus_loading = page.locator('[data-qa="search-bus-loading"]')
        self.ticket_bus_detail = page.get_by_text("Выберите место из списка", exact=False)
        self.ticket_on_bus = page.get_by_role("button", exact=True)
        self.bus_add_to_cart = page.get_by_role("button", name="В корзину")
        self.go_to_card_from_modal = page.get_by_role("button", name="Перейти в корзину")
        self.successful_added_modal = page.get_by_text("Билет добавлен в корзину")
        self.successful_notification = page.get_by_text(re.compile(r"Билет на автобус.*добавлен в корзину"))
        self.button_close_modal = page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3)
        self.duplicate_notification = page.get_by_text(re.compile(r".* уже добавлено в корзину"))

    def open_bus_search(self):
        """Переход на вкладку поиска автобусов"""
        self.smartdesk_bus_search.click()

    def swap_cities(self):
        expect(self.swap_cities_button).to_be_visible()
        self.swap_cities_button.click()

    def check_cities_swapped(self):
        """Проверка смены городов местами"""
        expect(self.search_bus_menu_cities_from).to_have_value("Тольятти")
        expect(self.search_bus_menu_cities_to).to_have_value("Самара")

    def check_bus_search_page_is_open(self):
        """Проверка открытия страницы поиска автобусов""" 
        expect(self.search_bus_menu_cities_from).to_be_visible()
        expect(self.search_bus_menu_cities_to).to_be_visible()
        expect(self.search_bus_menu_dates_from).to_be_visible()

    def fill_cities(self, city_from, city_to):
        """Заполнение городов отправления и прибытия"""
        self.search_bus_menu_cities_from.press_sequentially(city_from, delay=100)
        self.first_city_from.wait_for(state="visible")
        self.first_city_from.click()
        
        self.search_bus_menu_cities_to.press_sequentially(city_to, delay=100)
        self.first_city_to.wait_for(state="visible")
        self.first_city_to.click()

    def select_departure_date(self, days_ahead: int = 5):
        """Выбирает дату через N дней от сегодня"""
        target_date = datetime.now() + timedelta(days=days_ahead)
        target_day = str(target_date.day)

        # Открываем календарь
        self.search_bus_menu_dates_from.click()

        # Ищем активную (не disabled) дату и кликаем
        active_day = self.page.locator(
            'div.E1yTWG_wrap:not(.E1yTWG_disabled)'
        ).get_by_text(target_day, exact=True).first
        active_day.click()

    def empty_bus_search(self):
        """Проверка отображения подсказок"""
        expect(self.empty_city_from).to_be_visible()
        expect(self.empty_city_to).to_be_visible()
        expect(self.empty_date).to_be_visible()

    def bus_search(self):
        """Выполнение поиска автобуса"""
        self.search_button.click()

    def check_search_results(self):
        """Проверка на успешный поиск и найденую непустую выдачу"""
        expect(self.ticket_bus_skeleton.first).not_to_be_visible(timeout=30000)
        expect(self.ticket_bus.first).to_be_visible(timeout=30000)

    def select_first_bus(self):
        """Переход к выбору места в автобусе"""
        expect(self.select_seat_button.first).to_be_visible(timeout=10000)
        self.select_seat_button.first.click()

    def check_bus_details_are_open(self):
        """Проверка на успешную загрузку мест автобуса"""
        expect(self.search_bus_loading).not_to_be_visible(timeout=30000)
        expect(self.ticket_bus_detail).to_be_visible(timeout=30000)

    def add_bus_seat_to_cart(self):
        """Добавление автобусного билета в корзину"""
        self.ticket_on_bus.nth(1).click()
        self.bus_add_to_cart.click()

    def check_bus_added_to_cart(self):
        expect(self.successful_added_modal).to_be_visible()
        expect(self.successful_notification).to_be_visible()

    def open_cart_from_confirmation(self):
        """Переход в корзину после добавления билета в корзину"""
        expect(self.successful_added_modal).to_be_visible()
        expect(self.successful_notification).to_be_visible()
        self.go_to_card_from_modal.click()

    def check_duplicate_bus_not_added(self):
        """Отображение уведомления об уже добавленном билете"""
        expect(self.duplicate_notification).to_be_visible()

    def close_confirmation_modal(self):
        """Закрытие модального окна"""
        self.button_close_modal.click()

    