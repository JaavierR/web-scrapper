region = driver.find_element_by_id('search-field-región')
region.click()

link = driver.find_element_by_xpath(
    "//div[contains(text(),'Metropolitana de Santiago')]")
link.click()

# time.sleep(5)

# amount = driver.find_element_by_id('search-field-precio-min')
# amount.click()

# link2 = driver.find_element_by_xpath(
#     "//div[contains(text(),'$4.000.000')]")
# link2.click()

# time.sleep(3)

# boton = driver.find_element_by_class_name('search-form-submit')
# boton.click()
