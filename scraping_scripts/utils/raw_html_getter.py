import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime as dt
import shutil
import os
import time


class HtmlParser:
    def __init__(self, websites):
        self.websites = websites
        self.relative_path = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(self.relative_path, f"../../html_bank/html_latest/")
        self.output = os.path.join(self.relative_path, f"../../html_bank/html_archive/")

    def html_writer(self, url):
        chromedriver = (
            "/usr/lib/chromium-browser/chromedriver"  # NEEDS TO BE REFERENCED CORRECTLY
        )
        driver = webdriver.Chrome(chromedriver)
        driver.get(url)
        elm = driver.find_element_by_tag_name("html")
        elm.send_keys(Keys.END)
        time.sleep(3)
        elm.send_keys(Keys.END)
        time.sleep(4)
        soup = BeautifulSoup(driver.page_source, "lxml")
        current_time = dt.now()
        tag = current_time.strftime("%Y_%m_%d_%H")
        split = url.split("/")[2]
        count_check = split.count(".")
        if count_check == 2:
            x, y, z = split.split(".")
            name = y + "dot" + z + "_" + tag
        else:
            x, y, z, a = split.split(".")
            name = y + "dot" + z + a + "_" + tag

        with open(f"{self.path}{name}.html", "w", encoding="utf-8") as f_out:
            f_out.write(soup.prettify())

        driver.quit()

    def html_getter(self):

        if len(os.listdir(self.path)) == 0:
            for url in self.websites:
                self.html_writer(url)
        else:
            files = os.listdir(self.path)
            for i in files:
                shutil.move(self.path + i, self.output)
            for url in self.websites:
                self.html_writer(url)
