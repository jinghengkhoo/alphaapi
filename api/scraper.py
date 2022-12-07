import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

def scrape(ticker):
    DRIVER_PATH = '/home/ubuntu/jh/alphaapi/chromedriver/chromedriver'
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    cookies = pickle.load(open("/home/ubuntu/jh/alphaapi/cookie/cookie.pkl", "rb"))
    driver.get('https://seekingalpha.com')
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get(f'https://seekingalpha.com/symbol/{ticker}')
    time.sleep(5)
    rating_elements = driver.find_elements(by=By.XPATH, value='//span[@data-test-id="numeral-rating-badge"]')
    ratings = []
    for elemt in rating_elements:
        ratings.append(elemt.text)
    return ratings