import time
import datetime

from selenium import webdriver

"""
    By: Thomas Flaglor
    Requirements: selenium needs to be installed and Chrome Version 85
    
    Description: 
    This simple script uses Selenium in headless mode to automate the Daily Health Screen App. It also saves a
    screenshot in the local file directory to show it was completed.
    All you have to do is fill in your username and password in this file
    To automate you can set up task scheduler on windows
"""


def main():
    options = webdriver.ChromeOptions()
    # makes it headless
    options.headless = True
    date = datetime.datetime.now()
    driver = webdriver.Chrome(executable_path='chromedriver\chromedriver.exe', chrome_options=options)
    driver.get('https://dailyhealth.rit.edu/')
    time.sleep(1)
    # Username
    driver.find_element_by_id('username').send_keys('putUsernameHere')
    # Password
    driver.find_element_by_id('password').send_keys('putPasswordHere')
    time.sleep(1)
    # clicks to login
    driver.find_element_by_xpath("//button[@name='_eventId_proceed']").click()
    time.sleep(2)
    # clicks let's start button
    driver.find_element_by_xpath("//a[@class='c0 c1 at c2 br b2 aq c3 c4 c5 c6 c7 c8']").click()
    time.sleep(2)
    # clicks no
    element = driver.find_element_by_xpath("//div[@class='dc dd de df dg dh di dj ai aj dk br dm dn']")
    driver.execute_script("arguments[0].click();", element)
    # waits for page to load so it can take screenshot of complete submission
    time.sleep(4)
    # takes screenshot and saves to directory of python file
    driver.get_screenshot_as_file(
        "dailyHealthScreen {month}-{day}-{year}.png".format(month=date.month, day=date.day, year=date.year))
    driver.quit()
    exit()


if __name__ == '__main__':
    main()
