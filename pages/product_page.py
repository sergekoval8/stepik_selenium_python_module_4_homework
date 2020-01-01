from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def find_name_product(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        return name

    def find_price_product(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return price

    def click_add_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button.click()

    def find_basket_name_product(self):
        bs_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME_PRODUCT).text
        return bs_name

    def find_basket_price_product(self):
        bs_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        return bs_price


