import os
import time
import datetime
from selenium import webdriver

"""
    Requirements: selenium needs to be installed and Chrome Version 85
    
    Description: 
    This simple script uses Selenium in headless mode to automate the Daily Health Screen App. It also saves a
    screenshot in a folder, named after the username used, in the local directory to show it was completed
    All you have to do is fill in your username and password in the 'Info.txt' file
    To automate you can set up task scheduler on windows or set Loop to True
"""
Loop = False  # Loops the program every day if True


def folder_check(username):
    path = './' + username + '/'
    if not os.path.exists(path):
        os.makedirs(path)


def complete_form(username, password):
    options = webdriver.ChromeOptions()
    # makes it headless
    options.headless = True
    date = datetime.datetime.now()
    driver = webdriver.Chrome(executable_path='chromedriver\chromedriver.exe', chrome_options=options)
    driver.get('https://dailyhealth.rit.edu/')
    time.sleep(1)
    # Username
    driver.find_element_by_id('username').send_keys(username)
    # Password
    driver.find_element_by_id('password').send_keys(password)
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
    folder_check(username)
    driver.get_screenshot_as_file(
        username + "/dailyHealthScreen {month}-{day}-{year}.png".format(month=date.month, day=date.day, year=date.year))
    driver.quit()


def main():
    with open("Info.txt") as f:
        for line in f:
            fields = line.split(',')
            complete_form(fields[0], fields[1].replace('\n', ''))

    # Starts the loop if Loop is True
    while Loop:
        # Waits 24 Hours
        time.sleep(86400)
        with open("Info.txt") as f:
            for line in f:
                fields = line.split(',')
                complete_form(fields[0], fields[1].replace('\n', ''))


if __name__ == '__main__':
    main()
