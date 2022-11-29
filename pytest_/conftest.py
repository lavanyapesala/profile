import pytest
from selenium import webdriver
from library.config import Config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from msedge.selenium_tools import EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome"])
def init_driver(request):

    # browser = request.param

    if request.param == "chrome":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--disable-notification")
        chrome_option.add_argument("--disable-infobars")
        chrome_option.add_argument("start-maximized")
        chrome_option.add_argument("--disable-extensions")
        chrome_option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        chrome_option.add_argument("use-fake-ui-for-media-stream")
        driver = webdriver.Chrome(executable_path=Config.chrome_path,chrome_options=chrome_option)

    elif request.param=="firefox":
        option=Options()
        option.binary_location=r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=r'C:\Users\asus\OneDrive\Desktop\gecko\geckodriver.exe',options=option)
        driver.set_page_load_timeout(20)


    # elif request.param == "Edge":
    #     option=EdgeOptions
    #     option.use_chromium=True
    #
    #     driver = webdriver.Edge(executable_path=Config.edge_path)


    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver

    path=r'C:\Users\asus\PycharmProjects\facebook_1\Screenshot\\'
    driver.save_screenshot(path+"profile.png")
    driver.close()