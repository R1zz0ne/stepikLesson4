from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" + \
            "coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    NameProduct = page.search_name_product()
    PriceProduct = page.search_price_product()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.check_name_product_alert_add_to_busket(NameProduct)
    page.check_price_product_alert_add_to_basket(PriceProduct)
    time.sleep(30)
