from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
    BASKET_ROW = (By.CSS_SELECTOR, 'div.basket-items>div.row')


class MainPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group>a.btn.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    BUTTON_SUBMIT = (By.NAME, "registration_submit")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-email')
    LOGIN_URL = (By.CSS_SELECTOR, 'ru/accounts/login/')
    LOGIN_FORM = (By.ID, 'login_form')
    PASSWORD1_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD2_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    BASKET_NAME_PRODUCT = (By.CSS_SELECTOR, 'div.alertinner>strong')
    BASKET_PRICE = (By.XPATH, "//p[contains(text(), 'Your basket total is now')]/strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, 'ul.breadcrumb>li.active')
    PRICE = (By.CSS_SELECTOR, '.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")





