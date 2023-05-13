from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

birth = ['03/10/1996', '05/02/1995', '30/01/1994',  '20/05/1993']
name = ['kelly', 'Dan', 'sam', 'raos', 'zuan', 'kate', 'tommy']
name2 = ['bun', 'bill', 'billy', 'gos', 'dum', 'jessy', 'robert', 'jones', 'tom']

for i in range(1000):
    driver = webdriver.Chrome()
    url = 'https://itf.tell-us-what-you-think.com/s3/Billie-Jean-King-Cup-Heart-Award-2023'
    driver.get(url)
    time.sleep(2)
    img = driver.find_element(By.CSS_SELECTOR, "img[alt='Barbora Krejcikova (CZE)']")
    img.click()
    time.sleep(2)
    img = driver.find_element(By.CSS_SELECTOR, "img[alt='Suzan Lamens (NED)']")
    img.click()
    time.sleep(2)
    img = driver.find_element(By.CSS_SELECTOR, "img[alt='Back Dayeon (KOR)']")
    img.click()
    time.sleep(2)
    img = driver.find_element(By.CSS_SELECTOR, "img[alt='Julia Riera (ARG)']")
    img.click()
    time.sleep(2)

    driver.find_element(By.ID, "sg_NextButton").click()
    time.sleep(2)

    first_name_field = driver.find_element(By.NAME, "sgE-90564668-4-22")
    first_name_field.send_keys(name[i % len(name)])

    second_name_field = driver.find_element(By.NAME, "sgE-90564668-4-23")
    second_name_field.send_keys(name2[i % len(name2)])

    country_dropdown = Select(driver.find_element(By.NAME, 'sgE-90564668-4-25'))
    country_dropdown.select_by_value('10671')

    birth_field = driver.find_element(By.NAME, "sgE-90564668-4-24")
    birth_field.send_keys(birth[i%4])

    second_name_field = driver.find_element(By.NAME, "sgE-90564668-4-26")
    email_id = f"{name[i%len(name)]}{i}@gmail.com"
    second_name_field.send_keys(email_id)

    label_element = driver.find_element(By.CSS_SELECTOR, "label[for='sgE-90564668-4-33-10751']")
    label_element.click()

    submit = driver.find_element(By.ID, "sg_SubmitButton")
    submit.click()




while(True):
    pass


driver.quit()