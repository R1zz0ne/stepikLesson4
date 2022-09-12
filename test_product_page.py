from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from selenium.common.exceptions import NoAlertPresentException
import time
import pytest

@pytest.mark.parametrize('id', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.xfail(reason="fixing this bug right now")
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, id):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" + \
            f"coders-at-work_207/?promo=offer{id}"
    page = ProductPage(browser, link)
    page.open()
    NameProduct = page.search_name_product()
    PriceProduct = page.search_price_product()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.check_name_product_alert_add_to_busket(NameProduct)
    page.check_price_product_alert_add_to_basket(PriceProduct)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.expect_no_items_in_the_basket()
    page.expect_text_that_the_basket_is_empty()
