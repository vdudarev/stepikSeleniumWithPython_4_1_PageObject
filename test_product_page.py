from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest
import time


@pytest.mark.nomark
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


@pytest.mark.nomark
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    # Добавляем товар в корзину
    page.add_product_to_basket_simple()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present (а оно должно быть - тест xfail)
    page.should_not_be_success_message()


@pytest.mark.nomark
def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.nomark
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    # Добавляем товар в корзину
    page.add_product_to_basket_simple()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared (а оно должно быть - тест xfail)
    page.should_not_be_success_message_with_time()


@pytest.mark.nomark
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.nomark
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    lpage = LoginPage(browser=page.browser, url=page.browser.current_url)
    lpage.should_be_login_page()


@pytest.mark.nomark
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    page.basket_is_empty()


@pytest.mark.login
class TestLoginFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        lpage = LoginPage(browser=page.browser, url=page.browser.current_url)
        lpage.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации;
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        page.open()
        page.should_be_login_page()
        # зарегистрировать нового пользователя;
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, str(time.time())+"1234567890")
        # проверить, что пользователь залогинен.
        page.should_be_authorized_user()
        # yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе

    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        page.open()
        page.add_product_to_basket_simple()
