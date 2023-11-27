from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
try:
    import src.lib.kryptering as kryptering
except ImportError:
    import kryptering

from functools import cache
from bs4 import BeautifulSoup
import time
import os
import dotenv







@cache
def getVisma():

    def waitUntil(byType: By, item: str):

        wait = WebDriverWait(driver, timeout=10)

        wait.until(EC.visibility_of_element_located((byType, item)))
        revealed = driver.find_element(byType, item)
        print(f"Waited for {item}")

        return revealed

    dotenv.load_dotenv()

    # Set the path to the ChromeDriver executable using the Service class
    chrome_driver_path = ChromeDriverManager().install()
    service = Service(chrome_driver_path)

    # Create a Chrome driver with the configured service

    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument('start-maximized')

    driver = webdriver.Chrome(service=service, options=options)
    print("started") #Debug

    # Visit the desired URL
    driver.get("https://romsdal-vgs.inschool.visma.no/")

    # Locate the login button by its name and click it
    time.sleep(.5)

    button = waitUntil(By.ID, "onetrust-accept-btn-handler")

    button.click()

    login = waitUntil(By.ID, "login-with-feide-button")
    login.click()


    encrypter = kryptering.encrypter()
    Username = encrypter.decrypt(os.environ.get('feidenavn'))
    Password = encrypter.decrypt(os.environ.get('feidepassord'))
    print("logging in")

    username = driver.find_element(By.ID, "username")
    username.send_keys(Username)

    password = driver.find_element(By.ID, "password")
    password.send_keys(Password)

    driver.find_element(By.CLASS_NAME, "button-primary").click()
    driver.implicitly_wait(2.5)
    print("parsing html")

    waitUntil(By.CLASS_NAME, "Timetable-TimetableDays_day")

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Replace with the actual class of the parent div

    parent_div = soup.find(
        'div', class_='active Timetable-TimetableDays_day', recursive=True)

    if not parent_div:

        parent_div = soup.find(
            'div', class_='Timetable-TimetableDays_day', recursive=True)

    if parent_div:
                
        # Find all <h4> elements within the parent <div>
        h4_tags = parent_div.find_all('h4')

        teacher_item = parent_div.find('div', class_="Timetable-Items", recursive=True)
        teachers = []

        for teacher in teacher_item:

            items=teacher.find("div", {"teachername": True})
            teacher_name = items['teachername']
            teachers.append(teacher_name)
        
        
        lessons = [h4tag.get_text().split()[0] for h4tag in h4_tags]

        timestart = [h4tag.get_text().split('klokken')[1].split()[0] for h4tag in h4_tags]
        

    dump = {i:[j,k] for i,j,k in zip(timestart, lessons, teachers)}
    driver.close()

    return dump



if __name__ == "__main__":
    timeplan = getVisma()

    print(timeplan)
