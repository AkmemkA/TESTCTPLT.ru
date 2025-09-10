import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage


class CalculatorPage(BasePage):
    # форма
    SENDER_BOOK_BTN = (By.CSS_SELECTOR, "[data-qa='sender-book']")
    SENDER_INPUT = (By.CSS_SELECTOR, "[data-qa='sender-input']")
    RECEIVER_MAP_BTN = (By.CSS_SELECTOR, "[data-qa='receiver-map']")
    RECEIVER_INPUT = (By.CSS_SELECTOR, "[data-qa='receiver-input']")
    WEIGHT_INPUT = (By.CSS_SELECTOR, "[data-qa='weight-input']")
    FIND_BTN = (By.CSS_SELECTOR, "[data-qa='find-button']")

    # результаты
    RESULT_ITEM = (By.CSS_SELECTOR, "[data-qa='tariff-item']")
    ORDER_PAGE_ROOT = (By.CSS_SELECTOR, "[data-qa='order-page']")

    # сортировки/фильтры/дата (при необходимости подставь реальные data-qa)
    SORT_SPEED = (By.CSS_SELECTOR, "[data-qa='sort-speed']")
    SORT_RATING = (By.CSS_SELECTOR, "[data-qa='sort-rating']")
    SORT_PRICE = (By.CSS_SELECTOR, "[data-qa='sort-price']")
    SORT_QUALITY = (By.CSS_SELECTOR, "[data-qa='sort-quality']")
    FILTER_EXPRESS = (By.CSS_SELECTOR, "[data-qa='filter-express']")
    FILTER_SERVICE = (By.CSS_SELECTOR, "[data-qa='filter-service']")
    FILTER_COMPANY = (By.CSS_SELECTOR, "[data-qa='filter-company']")
    DATE_PICKER = (By.CSS_SELECTOR, "[data-qa='date-picker']")

    @allure.step("Указать отправителя (адресная книга): {value}")
    def set_sender(self, value="Москва"):
        self.click(self.SENDER_BOOK_BTN)
        self.type(self.SENDER_INPUT, value)
        return self

    @allure.step("Указать получателя (карта): {value}")
    def set_receiver(self, value="Москва"):
        self.click(self.RECEIVER_MAP_BTN)
        self.type(self.RECEIVER_INPUT, value)
        return self

    @allure.step("Указать вес: {weight} кг")
    def set_weight(self, weight: float):
        self.type(self.WEIGHT_INPUT, str(weight))
        return self

    @allure.step("Найти предложения")
    def submit(self):
        self.click(self.FIND_BTN)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_all_elements_located(self.RESULT_ITEM)
        )
        return self

    @allure.step("Проверить, что предложений ≥ {count}")
    def should_have_offers(self, count=10):
        items = self.find_all(self.RESULT_ITEM)
        assert len(items) >= count, f"Ожидали ≥{count}, получили {len(items)}"
        return self

    @allure.step("Проверить обязательные КС присутствуют")
    def should_contain_required_companies(self):
        required = ["CDEK", "CSE", "Dostavista", "DPD", "Flip POST", "Fox Express", "Pony Express"]
        texts = [el.text for el in self.find_all(self.RESULT_ITEM)]
        for name in required:
            assert any(name in t for t in texts), f"{name} отсутствует в выдаче"
        return self

    @allure.step("Проверить сортировку: {name}")
    def check_sort(self, locator, name=""):
        self.click(locator)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.RESULT_ITEM)
        )
        return self

    @allure.step("Проверить фильтры")
    def check_filters(self):
        self.click(self.FILTER_EXPRESS)
        self.click(self.FILTER_SERVICE)
        self.click(self.FILTER_COMPANY)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.RESULT_ITEM)
        )
        return self

    @allure.step("Сменить дату забора")
    def change_date(self):
        self.click(self.DATE_PICKER)
        # тут: выбор другой даты; при необходимости добавь локаторы конкретных дней
        return self

    @allure.step("Открыть первое предложение → страница оформления")
    def open_first_offer(self):
        self.find_all(self.RESULT_ITEM)[0].click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.ORDER_PAGE_ROOT))
        return self
