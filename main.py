# Pachete
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# Configurare
timp_login = 10  # Timp pentru autentificare (în secunde)

# Creare driver
driver = webdriver.Chrome()

# Deschide browserul cu linkul implicit
baseurl = "https://web.whatsapp.com"
driver.get(baseurl)

time.sleep(timp_login)

# Parcurge lista de numere
with open("contacts.csv", newline='') as csvfile:
    readContacts = csv.reader(csvfile)
    for phone, msg in readContacts:
        phonenum = phone
        message = msg

        link = (baseurl + "/send/?phone=" + str(phonenum))
        driver.get(link)

        # Așteaptă inițializarea chat-ului (crește timpul de așteptare dacă este necesar)
        time.sleep(15)  # Ajustează după cum consideri necesar

        content = driver.switch_to.active_element
        content.send_keys(message)

        content.send_keys(Keys.RETURN)
        time.sleep(8)  # Așteaptă după trimiterea mesajului

# Închide driverul
driver.quit()
