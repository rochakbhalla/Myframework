import unittest, time 
from selenium import webdriver
from src.main.preconfig import PreConfig
from src.main.googlelanding import GoogleLanding

class FirstTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pc = PreConfig()
        cls.chromedriver = cls.pc.create_driver("Chrome") #webdriver.Chrome("./drivers/chromedriver")

    def test_open_google(self):
        self.chromedriver.get("https://google.com")

    def test_search_contntent(self):
        self.chromedriver.find_element_by_name("q").send_keys("My Search")
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.chromedriver.close()
        cls.chromedriver.quit()
    

if __name__ == "__main__":
    unittest.main()