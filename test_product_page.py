from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
import time
import pytest

@pytest.mark.parametrize('id', ["0", "1", "2", "3", "4", "5", "6", \
    pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, id):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" + \
            f"coders-at-work_207/?promo=offer{id}"
    page = ProductPage(browser, link)
    page.open()
    NameProduct = page.search_name_product()
    PriceProduct = page.search_price_product()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.check_the_name_of_the_product_added_to_the_cart(NameProduct)
    page.check_the_price_of_the_product_added_to_the_cart(PriceProduct)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/" + \
        "the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" + \
            "coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" + \
            "coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" + \
            "coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_disappeared_success_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/" + \
        "the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/" + \
        "the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.expect_no_items_in_the_basket()
    page.expect_text_that_the_basket_is_empty()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@test.org"
        password = "testtest123"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/" + \
                "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/" + \
                "coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        NameProduct = page.search_name_product()
        PriceProduct = page.search_price_product()
        page.add_product_in_basket()
        page.solve_quiz_and_get_code()
        page.check_the_name_of_the_product_added_to_the_cart(NameProduct)
        page.check_the_price_of_the_product_added_to_the_cart(PriceProduct)
