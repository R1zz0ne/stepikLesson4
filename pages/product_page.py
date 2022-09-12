from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def add_product_in_basket(self):
        add_basket_btn = self.browser.find_element( \
                            *ProductPageLocators.ADD_TO_BASKET_BTN)
        add_basket_btn.click()

    def search_name_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def search_price_product(self):
        return self.browser.find_element( \
                            *ProductPageLocators.PRODUCT_PRICE).text

    def check_name_product_alert_add_to_busket(self, nameproduct):
        alertname = self.browser.find_element( \
                                        *ProductPageLocators.ALERT_NAME).text
        assert alertname == nameproduct, "Product name does not match what " + \
                                            "was added to the cart"

    def check_price_product_alert_add_to_basket(self, priceproduct):
        alertprice = self.browser.find_element( \
                                        *ProductPageLocators.ALERT_PRICE).text
        assert alertprice == priceproduct, "Price of the product does not " + \
                                            "match what was added to the cart"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        # try:
        #     alert = self.browser.switch_to.alert
        #     alert_text = alert.text
        #     print(f"Your code: {alert_text}")
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present( \
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
