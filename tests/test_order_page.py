import allure

from data_tests.data import Users
from pages.home_page import HomePage, HomePageHeader
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка позитивного сценария с точкой входа в виде кнопки «Заказать» вверху страницы.')
    @allure.description('''1) Вверху главной страницы кликаем на кнопку "Заказать";
                        2) Вводим данные в форму "Для кого самокат' и кликаем на кнопку "Далее";
                        3) Вводим данные в форму "Про аренду" и кликаем на кнопку "Заказать";
                        4) Подтверждаем заказ и проверяем открытие окна с текстом оформления заказа''')
    def test_order_scooter_by_order_button_from_header(self, driver):
        header_page = HomePageHeader(driver)
        order_page = OrderPage(driver)
        header_page.order_button_click()
        order_page.fill_out_the_form_order_scooter(Users.user)
        assert order_page.check_order_title()

    @allure.title('Проверка позитивного сценария с точкой входа в виде кнопки «Заказать» внизу страницы.')
    @allure.description('''1) Внизу главной страницы кликаем кнопку "Заказать";
                        2) Вводим данные в форму "Для кого самокат' и кликаем на кнопку "Далее";
                        3) Вводим данные в форму "Про аренду" и кликаем на кнопку "Заказать";
                        4) Подтверждаем заказ и проверяем открытие окна с текстом оформления заказа''')
    def test_order_scooter_by_order_button_from_home_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.scroll_and_click_on_the_order_button()
        order_page.fill_out_the_form_order_scooter(Users.user_2)
        assert order_page.check_order_title()

        