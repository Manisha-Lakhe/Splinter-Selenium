from splinter import Browser  #to install both the libraries :- pip install splinter
from selenium import webdriver

executable_path = {'executable_path':r'C:\Users\Me\Desktop\chromedriver_win32\chromedriver'}
#install this driver from https://chromedriver.chromium.org 


options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

browser = Browser('chrome', **executable_path, headless = False, options = options)

browser.visit("https://www.instagram.com")

username_box = browser.find_by_name("username") #You can find the name of feild by inspecting the website 
username_box.fill('Enter your Username here')

password_box = browser.find_by_name('password')
password_box.fill('Enter your password here')

submit = browser.find_by_text('Log In').first.click()
