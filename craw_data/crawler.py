from lib2to3.pgen2 import driver
from tkinter import SEL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class craigslist_crawler(object):
    def __init__(self):
        self.url = f"https://shopee.vn/D%E1%BA%A7u-%C4%83n-Neptune-Light-2L-i.469064007.6695405166"
        self.driver = webdriver.Chrome("C:\Users\dinhc\OneDrive - Hanoi University of Science and Technology\Project\transformer\craw_data\chromedriver.exe")
        self.deplay = 5

    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        data_comment = driver.find_elements_by_class_name("shopee-product-rating")
        for data in data_comment:
            print(data.text)


if __name__ == "__main__":
    crawler = craigslist_crawler()
    crawler.load_page()