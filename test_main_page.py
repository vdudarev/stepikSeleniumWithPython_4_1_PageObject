from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import pytest
link = "http://selenium1py.pythonanywhere.com/"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

#def test_guest_can_go_to_login_page(browser):
#    page = MainPage(browser, link)
#    page.open()
#    login_page = page.go_to_login_page()
#    login_page.should_be_login_page()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # try:
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        # except Exception as err:
        # print("Exception: {0}".format(err))


def test_login_page(browser):
    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    page = MainPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    page.basket_is_empty()

