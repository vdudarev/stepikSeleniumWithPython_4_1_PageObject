from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest
link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.nomark
def test_login_page(browser):
    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    page.open()
    page.should_be_login_page()


@pytest.mark.nomark
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    page = MainPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    page.basket_is_empty()

