from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

PATH = "D:\webdrivers\chromedriver.exe"
OPTS = Options()
OPTS.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome(executable_path=PATH, chrome_options=OPTS)
driver.get("https://www.chileautos.cl/")

region = driver.find_element_by_id("search-field-región")
region.click()

link = driver.find_element_by_xpath(
    "//div[contains(text(),'Metropolitana de Santiago')]"
)
link.click()

sleep(5)

amount = driver.find_element_by_id("search-field-precio-min")
amount.click()

link2 = driver.find_element_by_xpath("//div[contains(text(),'$4.000.000')]")
link2.click()

sleep(3)

boton = driver.find_element_by_class_name("search-form-submit")
boton.click()
