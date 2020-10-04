"""Bot to automate form submits in the vehicule page og MercadoLibre."""

from time import sleep
from random import randint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AutoForm:
    """This is a class to autoexecute the bot for MeracadoLibre."""

    def __init__(
        self,
        first_name,
        last_name,
        contact_email,
        phone_number,
        question,
        full_path,
    ):
        """Constructor for the AutoForm.

        Args:
            driver (selenium object): Driver to execute the web browser.
            first_name (string): First name of the person.
            last_name (string): Last name of the person.
            contact_email (string): Contact email to the form test@test.com.
            phone_number (int, optional): Phone Number that it's optional.
            question (string): Text with the info to the contact.
            full_path (string): Path to the webpage that contains the products.
        """

        self.path = "./chromedriver.exe"
        self.opts = Options()
        self.opts.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
        )
        self.driver = webdriver.Chrome(
            executable_path=self.path,
            options=self.opts,
        )

        self.first_name = first_name
        self.last_name = last_name
        self.contact_email = contact_email
        self.phone_number = phone_number
        self.question = question
        self.full_path = full_path

    def autocomplete_input_form_by_name(self, wait_time, element_name, contact_info):
        input_form = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.NAME, element_name))
        )
        input_form.send_keys(contact_info)

    def click_submit_button(self, wait_time, element_xpath, sleep_time):
        button = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )
        button.click()
        sleep(sleep_time)

    def autocomplete_form(self):
        self.autocomplete_input_form_by_name(10, "firstName", self.first_name)
        self.autocomplete_input_form_by_name(10, "lastName", self.last_name)
        self.autocomplete_input_form_by_name(10, "contactEmail", self.contact_email)
        self.autocomplete_input_form_by_name(10, "phoneNumber", self.phone_number)
        self.autocomplete_input_form_by_name(10, "question", self.question)

        self.click_submit_button(
            20, "//form//input[@type='submit' and @value='Preguntar']", 10
        )

    def get_links(self):
        return [
            x.get_attribute("href")
            for x in self.driver.find_elements_by_xpath(
                "//*[contains(@class, 'andes-card')]/a"
            )
        ]

    def access_page(self):
        self.driver.get(self.full_path)

    def send_multiple_forms(self):
        self.driver.get(self.full_path)
        links = self.get_links()

        for idx, link in enumerate(links):
            try:
                self.driver.get(link)
                if idx == 0:
                    self.autocomplete_form()

                    self.driver.refresh()

                    sleep(randint(1, 3))

                    self.autocomplete_form()
                    self.driver.back()
                    self.driver.back()
                elif idx == 1:
                    self.click_submit_button(
                        30,
                        "//form//input[@type='submit' and @value='Preguntar']",
                        randint(3, 10),
                    )

                    self.driver.back()
                    print("Done")
                    sleep(randint(4, 7))
                else:
                    self.driver.quit()
            except Exception as e:
                print(e)
                break

        self.driver.quit()


def menu():
    """Generate a menu to config the path to the webpage.

    Returns:
        weblink (str): The link to access the main page of the products by a certain
        criteria.
    """
    paginas = {
        "Autos": "https://autos.mercadolibre.cl",
        "Motos": "https://motos.mercadolibre.cl",
    }
    region = "rm-metropolitana"
    comunas = [
        "las-condes",
        "vitacura",
        "nunoa",
        "providencia",
        "huechuraba",
        "colina",
        "lo-barnechea",
        "la-reina",
    ]
    trato = "trato-directo"
    precio = "_PriceRange_4000000-0"
    divisor = "/"

    for idx, comuna in enumerate(comunas):
        print(str(idx + 1), comuna)

    idx_comuna = (
        int(input("\nSeleccione el numero de la comuna con la cual desea trabajar: "))
        - 1
    )

    for idx, pagina in enumerate(list(paginas)):
        print(str(idx + 1), pagina)

    idx_pagina = (
        int(input("\nSeleccione el numero de la opción con la cual desea trabajar: "))
        - 1
    )

    tipo_vehiculo = list(paginas)[idx_pagina]

    if tipo_vehiculo == "Autos":
        main_link = paginas[tipo_vehiculo]
        page_link = (
            main_link
            + divisor
            + region
            + divisor
            + comunas[idx_comuna]
            + divisor
            + trato
            + divisor
            + precio
        )
    elif tipo_vehiculo == "Motos":
        main_link = paginas[tipo_vehiculo]
        page_link = (
            main_link
            + divisor
            + region
            + divisor
            + comunas[idx_comuna]
            + divisor
            + trato
            + divisor
        )

    return page_link


path = menu()
test = AutoForm(
    "Pedro",
    "Pablo",
    "test@test.cl",
    "756324456",
    "This is a test",
    path,
    # "https://vehiculos.mercadolibre.cl/otros/la-araucania/",
)

test.access_page()
# test = AutoForm(
#     driver,
#     "Pedro",
#     "Pablo",
#     "test@test.cl",
#     "756324456",
#     "This is a test",
#     "https://vehiculos.mercadolibre.cl/otros/la-araucania/",
# )
# test.send_multiple_forms()

# for idx, link in enumerate(links):
#     # This if is only for testing
#     if count != 3:
#         try:
#             driver.get(link)

#             if idx == 0:
#                 complete_form(
#                     first_name="Pedro",
#                     last_name="Pablo",
#                     contact_email="pedro@testeo.com",
#                     question="test2 jaolsa",
#                 )

#                 driver.refresh()

#                 sleep(2)

#                 complete_form(
#                     first_name="Pedro",
#                     last_name="Pablo",
#                     contact_email="pedro@testeo.com",
#                     question="test2 jaolsa",
#                 )
#                 driver.back()
#                 driver.back()
#             else:
#                 asking_button = WebDriverWait(driver, 30).until(
#                     EC.presence_of_element_located(
#                         (
#                             By.XPATH,
#                             "//form//input[@type='submit' and @value='Preguntar']",
#                         )
#                     )
#                 )
#                 asking_button.click()

#                 sleep(10)

#                 driver.back()
#                 print("Done")
#                 sleep(5)

#             sleep(3)

#         except Exception as e:
#             break
#     else:
#         print("Done")
#         break
# def complete_form(
#     first_name="test5",
#     last_name="test4",
#     contact_email="test@test.com",
#     phone_number="",
#     question="some question",
# ):
#     """Autocomplete the form in the vehicule page.

#     Args:
#         first_name (str, optional): [description]. Defaults to "test5".
#         last_name (str, optional): [description]. Defaults to "test4".
#         contact_email (str, optional): [description]. Defaults to "test@test.com".
#         phone_number (str, optional): [description]. Defaults to "".
#         question (str, optional): [description]. Defaults to "some question".
#     """
#     input_first_name = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "firstName"))
#     )
#     input_first_name.send_keys(first_name)

#     input_last_name = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "lastName"))
#     )
#     input_last_name.send_keys(last_name)

#     input_contact_email = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "contactEmail"))
#     )
#     input_contact_email.send_keys(contact_email)

#     input_phone_number = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "phoneNumber"))
#     )
#     input_phone_number.send_keys(phone_number)

#     input_question = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "question"))
#     )
#     input_question.send_keys(question)

#     asking_button = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located(
#             (By.XPATH, "//form//input[@type='submit' and @value='Preguntar']")
#         )
#     )
#     asking_button.click()

#     sleep(10)

# htmls = []

# for link in links:
#     print(link)
#     # driver.get(link)
#     # htmls.append(driver.page_source)

# driver.quit()

# with open("test.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(links)
