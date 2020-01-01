from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, 'ru/accounts/login/')
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'ul.breadcrumb>li.active')
    PRICE = (By.CSS_SELECTOR, '.price_color')
    BASKET_NAME_PRODUCT = (By.CSS_SELECTOR, 'div.alertinner>strong')
    BASKET_PRICE = (By.XPATH, "//p[contains(text(), 'Your basket total is now')]/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")



