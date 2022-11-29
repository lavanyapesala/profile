from selenium import webdriver
from library.config import Config
import re
import time
import pytest_
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


from library.exel_lib import ReadExcel
from library.config import Config


class Facebookprofile:
    read_xl = ReadExcel()
    Profile_locators = read_xl.read_locators(Config.PROFILE_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver



    def user_name(self, username):

    # if isinstance(username, float):
        #     username = int(username)
        locator = self.Profile_locators["enter_username"]
        self.driver.find_element(*locator).send_keys(username)

    def pass_word(self, pwd):
        locator = self.Profile_locators["enter_password"]
        self.driver.find_element(*locator).send_keys(pwd)

    def login(self):


        locator = self.Profile_locators["login"]
        self.driver.find_element(*locator).click()

    def profile_icon(self):
        locator = self.Profile_locators["profile_icon"]
        self.driver.find_element(*locator).click()
        time.sleep(7)

    def click_edit_profile(self):
        locator = self.Profile_locators["click_edit_profile"]
        self.driver.find_element(*locator).click()

    def edit(self):
        locator = self.Profile_locators["edit"]
        self.driver.find_element(*locator).click()
        time.sleep(7)

    def select_profile_picture(self):
        locator = self.Profile_locators["select_profile_picture"]
        self.driver.find_element(*locator).click()
        # time.sleep(3)

    def save_profile_picture(self):
        locator = self.Profile_locators["save_profile_picture"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def edit_profile(self):
        locator = self.Profile_locators["edit_profile"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def edit_cover_photo(self):
        locator = self.Profile_locators["edit_cover_photo"]
        self.driver.find_element(*locator).click()
        time.sleep(7)

    def back_cover_photo(self):
        locator = self.Profile_locators["back_cover_photo"]
        self.driver.find_element(*locator).click()
        # time.sleep(3)

    def add_bio(self):
        locator = self.Profile_locators["add_bio"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def describe(self,status):
        locator = self.Profile_locators["describe"]
        self.driver.find_element(*locator).send_keys(status)
        time.sleep(3)

    def back_bio(self):
        locator = self.Profile_locators["back_bio"]
        self.driver.find_element(*locator).click()

    def customise_details(self):
        locator = self.Profile_locators["customise_details"]
        self.driver.find_element(*locator).click()


    def back_details(self):
        locator = self.Profile_locators["back_details"]
        self.driver.find_element(*locator).click()
        time.sleep(3)


    def add_Hobbies(self):
        locator = self.Profile_locators["add_Hobbies"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def back_hobbies(self):
        locator = self.Profile_locators["back_hobbies"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def add_features(self):
        locator = self.Profile_locators["add_features"]
        self.driver.find_element(*locator).click()
        time.sleep(7)

    def back_features(self):
        locator = self.Profile_locators["back_features"]
        self.driver.find_element(*locator).click()
        time.sleep(7)

    def back_to_profile(self):
        locator = self.Profile_locators["back_to_profile"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def add_to_story(self):
        locator = self.Profile_locators["add_to_story"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def back_story(self):
        locator = self.Profile_locators["back_story"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def profile(self):
        locator = self.Profile_locators["profile"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def log_out(self):
        locator=self.Profile_locators["log_out"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

