from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
import time


class ProductPage(BasePage):

    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)     # <button type="submit" class="btn btn-lg btn-primary btn-add-to-basket"
        btn.click()
        # self.solve_quiz_and_get_code()   # решить задачу (в каком-то упражнении было)
        #time.sleep(100)
        pname = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text       #<h1>Coders at Work</h1>
        pprice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text    #<p class="price_color">£19.99</p>
        #PRODUCT_MSG_STRONG = (By.CSS_SELECTOR, "#messages .alertinner strong")
        realMsg = self.browser.find_elements(*ProductPageLocators.PRODUCT_MSG_STRONG)
        assert pname == realMsg[0].text, "PRODUCT_NAME '" + pname + "' expected, but '" + realMsg[0].text + "' found"
        assert pprice == realMsg[2].text, "PRODUCT_PRICE '" + pprice + "' expected, but '" + realMsg[2].text + "' found"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_with_time(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented (with_time), but should not be"

    def add_product_to_basket_simple(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)     # <button type="submit" class="btn btn-lg btn-primary btn-add-to-basket"
        btn.click()
