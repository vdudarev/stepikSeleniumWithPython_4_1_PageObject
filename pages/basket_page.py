from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        # Ожидаем, что в корзине нет товаров
        items = self.browser.find_elements(*BasketPageLocators.ITEMS)
        assert len(items)==0, "Basket is not empty"
        # Ожидаем, что есть текст о том что корзина пуста
        text = self.browser.find_element(*BasketPageLocators.CONTENT).text
        assert "Your basket is empty." in text, "Basket is not empty"
