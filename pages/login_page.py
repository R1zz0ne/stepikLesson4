from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element( \
            *LoginPageLocators.REGISTER_EMAIL)
        pass_one_field = self.browser.find_element( \
            *LoginPageLocators.REGISTER_PASSONE)
        pass_two_field = self.browser.find_element( \
            *LoginPageLocators.REGISTER_PASSTWO)
        register_button = self.browser.find_element( \
            *LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        pass_one_field.send_keys(email)
        pass_two_field.send_keys(email)
        register_button.click()
