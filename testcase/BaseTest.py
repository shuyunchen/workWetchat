#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/17 19:51
# @Author  : 陈庆云
# @File    : BaseTest.py
# @Software: PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest:
    def setup(self):
        chrome_args = Options()
        chrome_args.debugger_address = "127.0.0.1:9226"
        self.driver = webdriver.Chrome()  # options=chrome_args
        self.driver.implicitly_wait(3)

    def teardown(self):
        sleep(3)
        self.driver.quit()
        pass
