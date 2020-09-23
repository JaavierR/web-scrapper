from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def complete_form(
    first_name="test5",
    last_name="test4",
    contact_email="test@test.com",
    phone_number="",
    question="some question",
):

    input_first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    )
    input_first_name.send_keys(first_name)

    input_last_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "lastName"))
    )
    input_last_name.send_keys(last_name)

    input_contact_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "contactEmail"))
    )
    input_contact_email.send_keys(contact_email)

    input_phone_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "phoneNumber"))
    )
    input_phone_number.send_keys(phone_number)

    input_question = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "question"))
    )
    input_question.send_keys(question)

    asking_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//form//input[@type='submit' and @value='Preguntar']")
        )
    )
    asking_button.click()

    sleep(10)


PATH = "D:\webdrivers\chromedriver.exe"
OPTS = Options()
OPTS.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

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

# full_path = (
#     AUTOS
#     + DIVISOR
#     + REGION
#     + DIVISOR
#     + COMUNA[idx_comuna]
#     + DIVISOR
#     + TRATO
#     + DIVISOR
#     + PRECIO
# )

driver = webdriver.Chrome(executable_path=PATH, chrome_options=OPTS)
# driver.get(full_path)
driver.get("https://vehiculos.mercadolibre.cl/otros/la-araucania/")

links = [
    x.get_attribute("href")
    for x in driver.find_elements_by_xpath("//*[contains(@class, 'andes-card')]/a")
]

count = 1

for link in links:
    if count != 3:
        try:
            driver.get(link)

            if count == 1:
                complete_form(
                    first_name="Pedro",
                    last_name="Pablo",
                    contact_email="pedro@testeo.com",
                    question="test2 jaolsa",
                )

                driver.refresh()

                sleep(2)

                complete_form(
                    first_name="Pedro",
                    last_name="Pablo",
                    contact_email="pedro@testeo.com",
                    question="test2 jaolsa",
                )
                driver.back()
                driver.back()
            else:
                asking_button = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//form//input[@type='submit' and @value='Preguntar']",
                        )
                    )
                )
                asking_button.click()

                sleep(10)

                driver.back()
                print("Done")
                sleep(5)

            count += 1

            sleep(3)

        except Exception as e:
            break
    else:
        print("Done")
        break

# htmls = []

# for link in links:
#     print(link)
#     # driver.get(link)
#     # htmls.append(driver.page_source)

# driver.quit()

# with open("test.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(links)