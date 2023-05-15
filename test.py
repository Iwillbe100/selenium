from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from faker import Faker

import time
import random
import string

for i in range(100000):
    driver = webdriver.Chrome()
    url = 'https://itf.tell-us-what-you-think.com/s3/Billie-Jean-King-Cup-Heart-Award-2023'
    driver.get(url)
    time.sleep(2)

    if i % 4 == 0:
        img = driver.find_element(By.CSS_SELECTOR, "img[alt='Barbora Krejcikova (CZE)']")
    elif i % 4 == 1:
        img = driver.find_element(By.CSS_SELECTOR, "img[alt='Leylah Fernandez (CAN)']")
    elif i % 4 == 2:
        img = driver.find_element(By.CSS_SELECTOR, "img[alt='Kaja Juvan (SLO)']")
    else:
        img = driver.find_element(By.CSS_SELECTOR, "img[alt='Tamara Zidansek (SLO)']")
    img.click()
    time.sleep(2)

    if i % 2 == 0:
        img = driver.find_element(By.CSS_SELECTOR, "img[alt='Suzan Lamens (NED)']")
    else:
        img = driver.find_element(By.CSS_SELECTOR, "img[alt='Rebecca Peterson (SWE)']")

    img.click()
    time.sleep(2)

    img = driver.find_element(By.CSS_SELECTOR, "img[alt='Back Dayeon (KOR)']")
    img.click()
    time.sleep(2)

    if i % 2 == 0:
        img = driver.find_element(By.CSS_SELECTOR, "img[alt='Julia Riera (ARG)']")
    else:
        img = driver.find_element(By.CSS_SELECTOR, "img[alt='Emiliana Arango (COL)']")

    img.click()
    time.sleep(2)

    driver.find_element(By.ID, "sg_NextButton").click()
    time.sleep(2)

    fake = Faker()
    name = fake.name()
    first_name_field = driver.find_element(By.NAME, "sgE-90564668-4-22")
    first_name_field.send_keys(name.split()[0])

    second_name_field = driver.find_element(By.NAME, "sgE-90564668-4-23")
    second_name_field.send_keys(name.split()[1])

    country = random.randint(10477, 10677)
    country_dropdown = Select(driver.find_element(By.NAME, 'sgE-90564668-4-25'))
    country_dropdown.select_by_value(str(country))
    date = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1950, 2015)
    birth = f"{date:02d}/{month:02d}/{year}"
    birth_field = driver.find_element(By.NAME, "sgE-90564668-4-24")
    birth_field.send_keys(birth)

    email = ['google.com', 'yahoo.com', 'hotmail.com', 'Outlook.com', 'aol.com', 'mail.com', 'protonmail.com', 'zoho.com', 'icloud.com', 'gmx.com']
    second_name_field = driver.find_element(By.NAME, "sgE-90564668-4-26")

    email_id = fake.email().split('@')[0]

    email_list = f"{email_id}@{email[i%len(email)]}"
    second_name_field.send_keys(email_list.lower())

    label_element = driver.find_element(By.CSS_SELECTOR, "label[for='sgE-90564668-4-33-10751']")
    label_element.click()

    submit = driver.find_element(By.ID, "sg_SubmitButton")
    submit.click()

    time.sleep(2)
    driver.quit()
