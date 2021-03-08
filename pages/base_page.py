from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        assert "login" in self.browser.current_url, "login should be in url " + self.browser.current_url

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()
        assert "basket" in self.browser.current_url, "basket should be in url " + self.browser.current_url

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def basket_is_empty(self):
        # Ожидаем, что в корзине нет товаров
        items = self.browser.find_elements(*BasketPageLocators.ITEMS)
        assert len(items)==0, "Basket is not empty"
        # Ожидаем, что есть текст о том что корзина пуста
        text = self.browser.find_element(*BasketPageLocators.CONTENT).text
        assert "Your basket is empty." in text, "Basket is not empty"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"
