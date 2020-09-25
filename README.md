# daily_health_screen_automation
An automated selenium web script to automate the daily health screen app from RIT.


By: Thomas Flaglor and Kyle Baptiste

Requirements: selenium needs to be installed and Chrome Version 85

Description: This simple script uses Selenium in headless mode to automate the Daily Health Screen App.
It also saves a screenshot in a folder, named after the username used, in the local directory to show it was completed.
All you have to do is fill in your username and password in a file named "Info.txt" (Format: User,Psk).
If there are multiple entries in the text file it will fill out the form for all of them.
To automate you can set up task scheduler on windows or set Loop to True
