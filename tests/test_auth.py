def test_negative_login_wrong_password(login_page, base_url):
    """Аутентификация с некорректными данными"""
    login_page.open_login_page(base_url)
    login_page.sign_in("test@mail.ru", "wrong_password")
    login_page.check_login_error("Неверно введены данные для входа")

def test_positive_login(login_page, base_page, base_url, user_email, user_password):
    """Успешная аутентификация"""
    login_page.open_login_page(base_url)
    login_page.sign_in(user_email, user_password) 
    base_page.check_page_is_open()