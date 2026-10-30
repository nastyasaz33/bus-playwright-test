def test_bus_search_page_is_open(bus_search_page):
    """Проверка на успешное открытие страницы поиска автобусов"""
    bus_search_page.check_bus_search_page_is_open()

def test_swap_cities(bus_search_page):
    """Проверка кнопки смены направлений"""
    bus_search_page.fill_cities("Самара", "Тольятти")
    bus_search_page.swap_cities()
    bus_search_page.check_cities_swapped()

def test_empty_bus_ticket_search(bus_search_page):
    """Поиск автобусного билета с пустыми полями"""
    bus_search_page.bus_search()
    bus_search_page.empty_bus_search()

def test_bus_ticket_search(bus_search_page):
    """Поиск автобусного билета"""
    bus_search_page.fill_cities("Самара", "Тольятти")
    bus_search_page.select_departure_date()    
    bus_search_page.bus_search()
    bus_search_page.check_search_results()

def test_add_bus_ticket_to_cart(bus_search_page, base_page, cart_page):
    """Добавление автобусного билета в корзину"""
    base_page.open_cart()
    cart_page.clear_cart()
    base_page.open_smartdesk()
    bus_search_page.open_bus_search()
    bus_search_page.fill_cities("Самара", "Тольятти")
    bus_search_page.select_departure_date()
    bus_search_page.bus_search()
    bus_search_page.check_search_results()
    bus_search_page.select_first_bus()
    bus_search_page.check_bus_details_are_open()
    bus_search_page.add_bus_seat_to_cart()
    bus_search_page.check_bus_added_to_cart()
    bus_search_page.open_cart_from_confirmation()
    cart_page.check_bus_in_cart()

def test_add_duplicate_bus_ticket_to_cart(bus_search_page, base_page, cart_page):
    """Проверка на дублирование автобусного билета в корзине"""
    base_page.open_cart()
    cart_page.clear_cart()
    base_page.open_smartdesk()
    bus_search_page.open_bus_search()
    bus_search_page.fill_cities("Самара", "Тольятти")
    bus_search_page.select_departure_date()
    bus_search_page.bus_search()
    bus_search_page.check_search_results()
    bus_search_page.select_first_bus()
    bus_search_page.check_bus_details_are_open()
    bus_search_page.add_bus_seat_to_cart()
    bus_search_page.close_confirmation_modal()
    bus_search_page.add_bus_seat_to_cart()
    bus_search_page.check_duplicate_bus_not_added()
    base_page.open_cart()
    cart_page.check_bus_in_cart()
    