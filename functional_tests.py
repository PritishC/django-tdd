# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:47:08 2014

@author: pritishc
"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title