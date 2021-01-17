from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    #try:
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    #except Exception as err:
        #print("Exception: {0}".format(err))

def test_login_page(browser):
    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    page.open()
    page.should_be_login_page()
