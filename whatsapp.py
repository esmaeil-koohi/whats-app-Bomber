import os
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from colorama import init, Fore, Style


def what_test():
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    input('\n\nRUN?? \n\n')
    init()
    os.system('cls')

    Message = input(Fore.LIGHTCYAN_EX + "Enter a message : " + Fore.WHITE)
    time.sleep(0.3)
    Names = input(Fore.LIGHTCYAN_EX + "\nEnter names [& Splited] : " + Fore.WHITE).split('&')
    time.sleep(0.3)
    NameRange = int(input(Fore.LIGHTCYAN_EX + "\nEnter Number" + Fore.WHITE))
    time.sleep(0.8)

    for name in Names:
        driver.find_element(By.XPATH, f'//span[@title="{name}"]').click()
        time.sleep(0.5)
        for number in range(NameRange):
            driver.find_element(By.XPATH, '//div[@role="textbox" and @data-tab="10"]').send_keys(Message + Keys.ENTER)
        else:
            print(Fore.LIGHTGREEN_EX + '[+] - ' + Fore.RED + name)

    input('\n\nEXIT? \n\n')
    driver.quit()
