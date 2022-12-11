from selenium import webdriver
from time import sleep

def pizza():
    driver = webdriver.Chrome(r"C:\Users\user\OneDrive\Desktop\chromedriver.exe")
    driver.maximize_window()

    #talk("Opening Pizza")
    driver.get('https://www.dominos.co.id/')
    sleep(2)

    # talk("Getting ready to order")
    driver.find_element_by_link_text('PESAN SEKARANG').click()
    sleep(2)

    # talk("Finding your location")
    driver.find_element_by_class_name('srch-cnt-srch-inpt').click()
    sleep(2)

pizza()