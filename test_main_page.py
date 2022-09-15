from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        loginpage = LoginPage(browser, browser.current_url)
        loginpage.should_be_login_page()
        time.sleep(1)

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, \
            browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.expect_no_items_in_the_basket()
        page.expect_text_that_the_basket_is_empty()
