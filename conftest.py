import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.bus_search_page import BusSearch

load_dotenv()

@pytest.fixture
def user_email():
    return os.environ["BUS_TEST_EMAIL"]


@pytest.fixture
def user_password():
    return os.environ["BUS_TEST_PASSWORD"]

@pytest.fixture
def logged_in_search_page(page: Page, base_url, user_email, user_password):
    """Фикстура: логин и переход к поиску билетов (для переиспользования)"""
    login_page = LoginPage(page)
    login_page.open_login_page(base_url)
    login_page.sign_in(user_email, user_password)

    base_page = BasePage(page)
    base_page.check_page_is_open()
    
    return page

@pytest.fixture
def bus_search_page(logged_in_search_page: Page):
    """Фикстура: Переход к форме поиска автобусов"""
    bus_page = BusSearch(logged_in_search_page)
    bus_page.open_bus_search()

    return bus_page

@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

@pytest.fixture
def cart_page(logged_in_search_page: Page):
    return CartPage(logged_in_search_page)

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)