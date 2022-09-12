from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

link = "http://selenium1py.pythonanywhere.com/catalogue/" + \
        "coders-at-work_207/"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_disappeared_success_message()
