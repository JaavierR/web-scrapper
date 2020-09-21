import time
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# PATH = "D:\webdrivers\geckodriver.exe"
PATH = "D:\webdrivers\chromedriver.exe"

AUTOS = "https://autos.mercadolibre.cl"
REGION = "rm-metropolitana"
COMUNA = [
    "las-condes",
    "vitacura",
    "nunoa",
    "providencia",
    "huechuraba",
    "colina",
    "lo-barnechea",
    "la-reina",
]
TRATO = "trato-directo"
PRECIO = "_PriceRange_4000000-0"
DIVISOR = "/"

# for idx, comuna in enumerate(COMUNA):
#     print(str(idx + 1), comuna)

# idx_comuna = (
#     int(input("\nSeleccione el numero de la comuna con la cual desea trabajar: ")) - 1
# )

full_path = (
    AUTOS
    + DIVISOR
    + REGION
    + DIVISOR
    + COMUNA[idx_comuna]
    + DIVISOR
    + TRATO
    + DIVISOR
    + PRECIO
)

driver = webdriver.Chrome(executable_path=PATH)
# driver.get(full_path)

# links = [
#     x.get_attribute("href")
#     for x in driver.find_elements_by_xpath("//*[contains(@class, 'andes-card')]/a")
# ]

# with open("test.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(links)


# first_name = driver.find_element_by_name("firstName")
# first_name.send_keys("Catalina")

# last_name = driver.find_element_by_name("lastName")
# last_name.send_keys("Puerta")

# contact_email = driver.find_element_by_name("contactEmail")
# contact_email.send_keys("contacto@prueba.cl")

# phone_number = driver.find_element_by_name("phoneNumber")
# phone_number.send_keys("+56 9 5123 4984")

# question = driver.find_element_by_name("question")
# question.send_keys("Hola soy margarita de los rios")
time.sleep(5)

driver.find_element_by_xpath("//input[@type='submit' and @value='Preguntar']").submit()

time.sleep(10)

# htmls = []

# for link in links:
#     print(link)
#     # driver.get(link)
#     # htmls.append(driver.page_source)

driver.quit()

# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.