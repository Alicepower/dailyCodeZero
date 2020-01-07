#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/1/7 14:12
# @Author : 一个有趣的程序媛-liulizi
# @desc :用python自动化脚本
# @FileName: AutoLogin.py
# @Software: PyCharm
# chromedriver驱动包下载地址：http://chromedriver.storage.googleapis.com/index.html
from selenium import webdriver
import time
# driver = webdriver.Ie()
# driver=webdriver.Firefox()
# driver=webdriver.Opera()
driver = webdriver.Chrome()
url="登录接口地址"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)
acc="账户名"
pwd="账户密码"
driver.find_element_by_class_name('ant-input').send_keys(acc)
driver.find_element_by_id('password').send_keys(pwd)
driver.find_element_by_class_name('ant-btn ').click()
time.sleep(5)
driver.quit()