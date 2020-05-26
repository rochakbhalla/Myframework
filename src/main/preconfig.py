
from selenium import webdriver
import os,sys

class PreConfig:

    def create_driver(self, browser):
        # print(sys.path)
        driver = webdriver.Chrome("./drivers/chromedriver") if browser.casefold() == "chrome" else print("No browser foudn for this ->"+ browser)
        return driver