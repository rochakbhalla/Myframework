from selenium import webdriver

class GoogleLanding:

    def __init__(self, driver):
        self.driver = driver

    def openPage(self, url):
        self.driver.get(url)
        
    def search(self, class_locator):
        self.driver.find_element_by_class(class_locator)
        
