import time

# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from random_user_agent.user_agent import UserAgent
# from random_user_agent.params import SoftwareName, OperatingSystem
import undetected_chromedriver.v2 as uc

def scrape(ticker):
    # DRIVER_PATH = 'chromedriver/chromedriver'
    # software_names = [SoftwareName.CHROME.value]
    # operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    # user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    # useragent = user_agent_rotator.get_random_user_agent()
    options = Options()
    # options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_argument("user-data-dir=selenium") 

    driver = uc.Chrome(use_subprocess=True, options=options, version_main=105)

    driver.get(f'https://seekingalpha.com/symbol/{ticker}')

    time.sleep(3)

    WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-test-id="numeral-rating-badge"]')))
    
    rating_elements = driver.find_elements(by=By.XPATH, value='//span[@data-test-id="numeral-rating-badge"]')
    # actions = ActionChains(driver)

    ratings = []
    for element in rating_elements:
        # actions.pause(4).move_to_element(element).perform()
        ratings.append(element.get_attribute("textContent"))
    return ratings

print(scrape('JNPR'))