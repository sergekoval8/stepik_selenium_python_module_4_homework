import time
import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

# Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear)
# Нажимаем на кнопку "Добавить в корзину".
# Посчитать результат математического выражения и ввести ответ.

# Ожидаемый результат:
#   Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
#   который вы действительно добавили.
#   Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                    pytest.param(\
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                        marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     name = page.find_name_product()
#     price = page.find_price_product()
#     page.click_add_basket()
#     page.solve_quiz_and_get_code()
#
#     # print([i for k, i in enumerate(page.find_basket_name_product()) if i != name[k]])
#     assert page.find_basket_name_product().strip().lower() == name.strip().lower(), "Name product in basket is different"
#     # print(len(page.find_basket_price_product()), len(price))
#     assert page.find_basket_price_product().strip() == price.strip(), "Price product in basket is different"
#
#     time.sleep(5)

#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    # Переходит в корзину по кнопке в шапке
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_goods_in_basket()
    basket_page.should_be_message_empty()


