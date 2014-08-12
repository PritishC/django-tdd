# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:47:08 2014

@author: pritishc
"""

from selenium import webdriver

# Initiate Selenium blast sequence with Firefox missiles
browser = webdriver.Firefox()

# Obtain missile command from Firefox silos
browser.get('http://localhost:8000')

# Check title 
#assert 'Django' in browser.title
assert 'To-Do' in browser.title