from .base_page import BasePage
from .locators import BasketPageLokators

class BasketPage(BasePage):
    def expect_no_items_in_the_basket(self):
        assert self.is_not_element_present( \
            *BasketPageLokators.BASKET_ITEMS), \
            "Items basket is presented, but should not be"

    def expect_text_that_the_basket_is_empty(self):
        text_empty_basket = self.browser.find_element( \
            *BasketPageLokators.BASKET_EMPTY_TEXT).text
        assert text_empty_basket == "Your basket is empty. Continue shopping", \
            "Basket is not empty"
