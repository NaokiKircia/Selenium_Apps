import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultsPage

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'E:\PythonProjects\Selenium_Apps\chromedriver.exe')

# class TestHotelSearch:
#
#     @pytest.fixture()
#     def setup(self):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         yield
#         self.driver.quit()
#
#     def test_hotel_search(self, setup):
#         self.driver.get("http://www.kurs-selenium.pl/demo/")
#         search_hotel_page = SearchHotelPage(self.driver)
#         search_hotel_page.set_city("Dubai")
#         search_hotel_page.set_date_range("12/03/2020", "13/03/2020")
#         search_hotel_page.set_travellers("4", "4")
#         search_hotel_page.perform_search()
#         results_page = SearchResultsPage(self.driver)
#         hotel_names = results_page.get_hotel_names()
#         hotel_prices = results_page.get_hotel_prices()
#
#         assert hotel_names[0] == 'Jumeirah Beach Hotel'
#         assert hotel_names[1] == 'Oasis Beach Tower'
#         assert hotel_names[2] == 'Rose Rayhaan Rotana'
#         assert hotel_names[3] == 'Hyatt Regency Perth'
#         assert hotel_prices[0] == '$22'
#         assert hotel_prices[1] == '$50'
#         assert hotel_prices[2] == '$80'
#         assert hotel_prices[3] == '$150'

@pytest.fixture()
def setup(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.implicitly_wait(10)
    self.driver.maximize_window()
    yield
    self.driver.quit()


def test_hotel_search(self, setup):
    self.driver.get("http://www.kurs-selenium.pl/demo/")
    search_hotel_page = SearchHotelPage(self.driver)
    search_hotel_page.set_city("Dubai")
    search_hotel_page.set_date_range("12/03/2020", "13/03/2020")
    search_hotel_page.set_travellers("4", "4")
    search_hotel_page.perform_search()
    results_page = SearchResultsPage(self.driver)
    hotel_names = results_page.get_hotel_names()
    hotel_prices = results_page.get_hotel_prices()

    assert hotel_names[0] == 'Jumeirah Beach Hotel'
    assert hotel_names[1] == 'Oasis Beach Tower'
    assert hotel_names[2] == 'Rose Rayhaan Rotana'
    assert hotel_names[3] == 'Hyatt Regency Perth'
    assert hotel_prices[0] == '$22'
    assert hotel_prices[1] == '$50'
    assert hotel_prices[2] == '$80'
    assert hotel_prices[3] == '$150'

@pytest.mark.parametrize("skladnik, suma", [(5, 10), (2, 4), (2, 5)])
def test_dodawanie(skladnik, suma):
    assert skladnik + skladnik == suma, "Suma dwoch takich samych skladnikow: " + str(skladnik) + " powinna byc rowna: " + str(skladnik + skladnik)
