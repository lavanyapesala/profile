from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--disable-notification")

chrome_option.add_argument("--disable-infobars")

chrome_option.add_argument("start-maximized")

chrome_option.add_argument("--disable-extensions")

chrome_option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 2})

chrome_option.add_argument("use-fake-ui-for-media-stream")

path = r'C:\Users\asus\Downloads\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path,chrome_options=chrome_option)
driver.implicitly_wait(30)

driver.get("https://www.facebook.com/")
driver.maximize_window()
#enter user_name
driver.find_element_by_xpath('//input[@class="inputtext _55r1 _6luy"]').send_keys('aparnaindu1999@gmail.com')

#enter password
driver.find_element_by_xpath('//input[@class="inputtext _55r1 _6luy _9npi"]').send_keys("aparna7013")
# time.sleep(2)

#login button
driver.find_element_by_xpath('//button[@name="login"]').click()
# time.sleep(3)

#-------------------------profile icon
driver.find_element_by_xpath('//span[text()="Lavanya Sai"]').click()

# time.sleep(4)

#------------------------ Edit profile button
driver.find_element_by_xpath('//span[text()="Edit profile"]').click()

#-------------------------Edit profile photo
driver.find_element_by_xpath('//span[text()="Edit"]').click()

driver.find_element_by_xpath('(//div[@class="x1ey2m1c xlg9a9y x9f619 xds687c x10l6tqk x17qophe x13vifvy"])[2]').click()
driver.find_element_by_xpath('//span[text()="Save"]').click()
time.sleep(2)
driver.find_element_by_xpath('//span[text()="Edit profile"]').click()
#-------------------------Back to edit page
# driver.find_element_by_xpath('(//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"])').click()

# #-------------------------Add cover photo
driver.find_element_by_xpath('(//span[text()="Add"])[1]').click()
# # time.sleep(2)
# #
# #-------------------------Back to edit page
driver.find_element_by_xpath('(//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"])[2]').click()
# time.sleep(2)
#
# #-------------------------Add Bio
driver.find_element_by_xpath('(//span[text()="Add"])[2]').click()
# time.sleep(2)
#
# #-------------------------Describe
driver.find_element_by_xpath('//textarea[@placeholder="Describe who you are"]').send_keys('hii hello')
#
# #-------------------------Back to edit page
driver.find_element_by_xpath('(//span[text()="Cancel"])[1]').click()
# time.sleep(2)
#
# #-------------------------Customize your info
driver.find_element_by_xpath('(//span[text()="Add"])[3]').click()
# time.sleep(2)
#
# #-------------------------Back to edit page
driver.find_element_by_xpath('//span[text()="Cancel"]').click()
# time.sleep(2)
#
# #-------------------------Add Hobbies
driver.find_element_by_xpath('(//span[text()="Add"])[4]').click()
# time.sleep(2)
#
# #-------------------------Back tpageo edit
driver.find_element_by_xpath('(//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"])[2]').click()

# #-------------------------Add Featured
driver.find_element_by_xpath('(//span[text()="Add"])[5]').click()
# time.sleep(2)
#
# #-------------------------Back to edit page
driver.find_element_by_xpath('(//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"])[2]').click()
# time.sleep(2)
#
# #-------------------------Bck to profile page
driver.find_element_by_xpath('//div[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"]').click()
# time.sleep(2)
#
# #-------------------------Add To Story
driver.find_element_by_xpath('//span[text()="Add to Story"]').click()
# time.sleep(2)
#
# #------------------------Back to profile page
driver.find_element_by_xpath('//div[@class="x1hc1fzr x10l6tqk x10ja8i0 x1k90msu x6o7n8i xbxq160 xtzu7as"]').click()
# driver.find_element_by_xpath('//span[text()="Log Out"]').click()
##profile
driver.find_element_by_xpath('(//div[@class="x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z"])[1]').click()
##logout
# driver.find_element_by_xpath('(//div[@class="x78zum5 xdt5ytf xq8finb x1xmf6yo x1e56ztr x1n2onr6 xqcrz7y"])[15]').click()
driver.find_element_by_xpath('//span[text()="Log Out"]').click()
## again login
# driver.find_element_by_xpath('(//span[text()="Log in"])[2]').click()

