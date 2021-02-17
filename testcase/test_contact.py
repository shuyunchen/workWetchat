#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/17 19:52
# @Author  : 陈庆云
# @File    : test_contact.py
# @Software: PyCharm
import json

from selenium.webdriver.common.by import By

from testcase.BaseTest import BaseTest


class TestContact(BaseTest):
    def write_cookies_json(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)

    def test_contact(self):
        # 获取cookies
        # self.write_cookies_json()
        # 注入cookies
        self.driver.get('https://work.weixin.qq.com/')
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.find_element(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]/span').click()
        assert '客户' == self.driver.find_element(By.XPATH, '//*[@data-name="analysis"]').text
