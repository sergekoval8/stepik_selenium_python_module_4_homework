from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_registration = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        email_registration.send_keys(email)
        password1_registration = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTRATION)
        password1_registration.send_keys(password)
        password2_registration = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTRATION)
        password2_registration.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        button_submit.click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not present 'login' in current login_link"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login_form  not present"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Reggister_form not present"
