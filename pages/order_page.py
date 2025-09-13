import allure

from locators.locators_for_order_page import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    
    @allure.step('Заполнение поля Имя')
    def set_name(self, text):
        self.send_keys_to_field(OrderPageLocators.name_field, text)

    @allure.step('Заполнение поля Фамилия')
    def set_last_name(self, text):
        self.send_keys_to_field(OrderPageLocators.last_name_field, text)

    @allure.step('Заполнение поля Адрес')
    def set_address(self, text):
        self.send_keys_to_field(OrderPageLocators.address_field, text)

    @allure.step('Заполнение поля Станция метро')
    def set_metro(self, text):
        self.click_button(OrderPageLocators.metro_field)
        self.send_keys_to_field(OrderPageLocators.metro_field, text)
        self.click_button(OrderPageLocators.metro)

    @allure.step('Заполнение поля Номер телефона')
    def set_telephone(self, text):
        self.send_keys_to_field(OrderPageLocators.telephone_field, text)

    @allure.step('Клик на кнопку Далее')
    def click_on_the_next_button(self):
        self.click_button(OrderPageLocators.button_next)

    @allure.step('''Заполнение формы "Для кого самокат" с переходом к форме "Про аренду"''')
    def complete_filling_of_the_who_is_scooter_form(self, user):
        self.set_name(user[1])
        self.set_last_name(user[2]) #
        self.set_address(user[3])
        self.set_metro(user[4])
        self.set_telephone(user[5])
        self.click_on_the_next_button()

    @allure.step('Заполнение поля Когда привезти заказ')
    def set_date(self, text):
        self.click_button(OrderPageLocators.deliver_order_field)
        self.send_keys_to_field(OrderPageLocators.deliver_order_field, text)

    @allure.step('Заполнение поля Срок аренды')
    def set_rental_period(self):
        self.click_button(OrderPageLocators.rent_period_field)
        self.click_button(OrderPageLocators.rent_period_three_days)

    @allure.step('Заполнение поля Цвет самоката')
    def select_color_scooter(self):
        self.click_button(OrderPageLocators.black_color_scooter_check)

    @allure.step('Заполнение поля Комментарий для курьера')
    def set_comment(self, text):
        self.send_keys_to_field(OrderPageLocators.comment_field, text)

    @allure.step('Клик на кнопку Заказать')
    def click_order_button(self):
        self.click_button(OrderPageLocators.order_button)

    @allure.step('''Заполнение формы "Про аренду" и переход к подтверждению заказа''')
    def complete_filling_of_the_about_rent_form(self, text):
        self.set_date(text[6])
        self.set_rental_period()
        self.select_color_scooter()
        self.set_comment(text[7])
        self.click_order_button()

    @allure.step('Клик на кнопку Нет')
    def click_button_no(self):
        self.click_button(OrderPageLocators.no_button)

    @allure.step('Клик на кнопку Да')
    def click_button_yes(self):
        self.click_button(OrderPageLocators.yes_button)

    @allure.step('''Заполнение формы "Для кого самокат", "Про аренду" и подтверждение заказа''')
    def fill_out_the_form_order_scooter(self, user, text):
        self.complete_filling_of_the_who_is_scooter_form(user)
        self.complete_filling_of_the_about_rent_form(text)
        self.click_button_yes()

    @allure.step('Проверка отображения окна с текстом подтверждения заказа')
    def check_order_title(self):
        return self.find_and_wait_locator(OrderPageLocators.order_placed_text).is_displayed()
    