from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")
driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element_by_xpath("//span[text()='Dubai']").click()
driver.find_element_by_name("checkin").send_keys("12/03/2020")
driver.find_element_by_name("checkout").send_keys("13/03/2020")
#alternatywna metoda to skorzystanie z kalendarza
# driver.find_element_by_name("checkin").click()
# # driver.find_element_by_xpath("//td[@class='day ' and text()='14']").click()
# # print(len(driver.find_elements_by_xpath("//td[@class='day ' and text()='16']")))
# # elementy = driver.find_elements_by_xpath("//td[@class='day ' and text()='16']")
# # for element in elementy:
# #     if (element.is_displayed()):
# #         element.click()
# #         break

driver.find_element_by_id("travellersInput").click()
driver.find_element_by_id("adultInput").clear()
driver.find_element_by_id("adultInput").send_keys("4")
driver.find_element_by_id("childInput").clear()
driver.find_element_by_id("childInput").send_keys("4")
driver.find_element_by_xpath("//button[text()=' Search']").click()
#//h4[contains(@class, 'list_title')]//b
hotels = driver.find_elements_by_xpath("//h4[contains(@class, 'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)
prices = driver.find_elements_by_xpath("//div[contains(@class, 'price_tab')]//b")
prices_euro = [price.get_attribute("textContent") for price in prices]
for name in prices_euro:
    print("Price for hotel: " + name)

# prices = driver.find_elements_by_xpath("//div[contains(@class, 'fs26 text-center')]//b")
# prices_euro = [price.get_attribute("textContent") for price in prices]
# for name in prices_euro:
#     print("Inny class text: " + name)

assert hotel_names[0] == 'Jumeirah Beach Hotel'
assert hotel_names[1] == 'Oasis Beach Tower'
assert hotel_names[2] == 'Rose Rayhaan Rotana'
assert hotel_names[3] == 'Hyatt Regency Perth'
assert prices_euro[0] == '€20.24'
assert prices_euro[1] == '€46'
assert prices_euro[2] == '€73.60'
assert prices_euro[3] == '€138'

driver.close()
