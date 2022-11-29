import time
from behave import *
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@given(u'launch Chrome browser')
def lauchbrowser(context):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--disable-notification")
    chrome_option.add_argument("--disable-infobars")
    chrome_option.add_argument("start-maximized")
    chrome_option.add_argument("--disable-extensions")
    chrome_option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    chrome_option.add_argument("use-fake-ui-for-media-stream")
    context.driver = webdriver.Chrome(executable_path=r'C:\Users\asus\Downloads\chromedriver_win32\chromedriver.exe', chrome_options=chrome_option)


@when(u'Open the facebook browser')
def facebook_loginpage(context):
    context.driver.get("https://www.facebook.com/")
    context.driver.maximize_window()
    time.sleep(2)
    context.driver.implicitly_wait(30)

@then(u'Enter username "{username}"')
def enter_username(context,username):
    time.sleep(2)
    context.driver.find_element_by_xpath('//input[@class="inputtext _55r1 _6luy"]').send_keys(username)


@then(u'Enter password "{pwd}"')
def enter_password(context,pwd):
    context.driver.find_element_by_xpath('//input[@class="inputtext _55r1 _6luy _9npi"]').send_keys(pwd)

@then(u'Click on Login')
def login(context):
    context.driver.find_element_by_xpath('//button[@name="login"]').click()

@then(u'Click on Profile icon')
def profile_icon(context):
    context.driver.find_element_by_xpath('//span[text()="Lavanya Sai"]').click()
    time.sleep(5)


@then(u'Click on Edit Profile')
def click_edit_profile(context):
    context.driver.find_element_by_xpath('//span[text()="Edit profile"]').click()
    time.sleep(3)


@then(u'Click on Edit')
def edit(context):
    context.driver.find_element_by_xpath('//span[text()="Edit"]').click()
    time.sleep(3)


@then(u'Choose Profile Picture')
def select_profile_picture(context):
    context.driver.find_element_by_xpath('(//div[@class="x1ey2m1c xlg9a9y x9f619 xds687c x10l6tqk x17qophe x13vifvy"])[2]').click()
    time.sleep(3)


@then(u'Click on Save')
def save_profile_picture(context):
    context.driver.find_element_by_xpath('//span[text()="Save"]').click()
    time.sleep(3)


@then(u'Click on EditProfile')
def edit_profile(context):
    context.driver.find_element_by_xpath('//span[text()="Edit profile"]').click()
    time.sleep(3)


@then(u'Choose Cover Photo')
def edit_cover_photo(context):
    context.driver.find_element_by_xpath('(//span[text()="Add"])[1]').click()
    time.sleep(5)


@then(u'Close Cover Photo')
def back_cover_photo(context):
    context.driver.find_element_by_xpath('(//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"])[2]').click()
    time.sleep(5)


@then(u'Enter Bio')
def add_bio(context):
    context.driver.find_element_by_xpath('(//span[text()="Add"])[2]').click()
    time.sleep(3)


@then(u'Describe the Bio "{status}"')
def describe(context,status):
    context.driver.find_element_by_xpath('//textarea[@placeholder="Describe who you are"]').send_keys(status)
    time.sleep(5)

@then(u'Back to Edit page')
def back_bio(context):
    context.driver.find_element_by_xpath('(//span[text()="Cancel"])[1]').click()
    time.sleep(5)

@then(u'Click on Customize Details')
def customise_details(context):
    context.driver.find_element_by_xpath('(//span[text()="Add"])[3]').click()
    time.sleep(3)


@then(u'Back from Details')
def back_details(context):
    context.driver.find_element_by_xpath('//span[text()="Cancel"]').click()
    time.sleep(5)


@then(u'Click on Add Hobbies')
def add_Hobbies(context):
    context.driver.find_element_by_xpath('(//span[text()="Add"])[4]').click()
    time.sleep(3)


@then(u'Back from Hobbies')
def back_hobbies(context):
    context.driver.find_element_by_xpath('(//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"])[2]').click()
    time.sleep(5)


@then(u'Click on Featured')
def add_features(context):
    context.driver.find_element_by_xpath('(//span[text()="Add"])[5]').click()
    time.sleep(3)

@then(u'Back from Featured')
def back_features(context):
    context.driver.find_element_by_xpath('(//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"])[2]').click()
    time.sleep(3)


@then(u'Back to Profile page')
def back_to_profile(context):
    context.driver.find_element_by_xpath('//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"]').click()
    time.sleep(7)


@then(u'Click on Add Story')
def add_to_story(context):
    context.driver.find_element_by_xpath('//span[text()="Add to Story"]').click()
    time.sleep(3)


@then(u'Click on Back')
def back_story(context):
    context.driver.find_element_by_xpath('//div[@class="x6s0dn4 x9f619 x78zum5 x1iyjqo2 x1s65kcs x1d52u69 xixxii4 x17qophe x13vifvy xzkaem6"]').click()
    time.sleep(7)



@then(u'Click on ProfileIcon')
def profile(context):
    context.driver.find_element_by_xpath('(//div[@class="x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z"])[1]').click()
    time.sleep(3)



@then(u'Click on LogOut')
def log_out(context):
    context.driver.find_element_by_xpath('//span[text()="Log Out"]').click()
    time.sleep(3)


@then('Close Browser')
def Close(context):
    context.driver.close()