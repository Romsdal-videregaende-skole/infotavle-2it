from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time,os,dotenv

def getVisma():
    def clickElement(type,element):
        time.sleep(1)
        object = driver.find_element(type,element)
        object.click()
    
    dotenv.load_dotenv()
    

    # Set the path to the ChromeDriver executable using the Service class
    chrome_driver_path = ChromeDriverManager().install()
    service = Service(chrome_driver_path)
    
    # Create a Chrome driver with the configured service
    
    options = Options()
    options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('start-maximized')

    driver = webdriver.Chrome(service=service, options=options)
    print("started")
    # Visit the desired URL
    driver.get("https://romsdal-vgs.inschool.visma.no/")
    
    # Locate the login button by its name and click it
    
    clickElement(By.ID,"onetrust-accept-btn-handler")
    
    clickElement(By.ID,"login-with-feide-button")
    
    Username = os.environ.get('feidenavn')
    Password = os.environ.get('feidepassord')
    
    username = driver.find_element(By.ID,"username")
    username.send_keys(Username)
    
    password = driver.find_element(By.ID,"password")
    password.send_keys(Password)
    
    clickElement(By.CLASS_NAME,"button-primary")
    
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"sr-only")))
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    time.sleep(5)
    info_element = soup.find("div",class_="active Timetable-TimetableDays_day")
    
    times = []
    
    if info_element:
        div_elements = info_element.find_all("div")
        
        for div_element in div_elements:
            h4_element = div_element.find("h4")
            if h4_element:
                h4_text = h4_element.get_text()
                words = h4_text.split()
                course_name = words[0]
                
                time_info = h4_text.split("klokken")
                
                lesson_start = time_info[1].split()
                times.append([course_name,lesson_start[0]])
    
    if times:
        driver.quit()
        return times
    getVisma()
    
    # Add a delay to keep the browser window open for 10 seconds (or adjust as needed)

if __name__ == "__main__":
    req = getVisma()
    print(req)
