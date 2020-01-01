from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ROW), "There should be no items in the basket"


    def should_be_message_empty(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert message.find("Your basket is empty.") > -1 , "There now message about empty basket"
