# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:47:08 2014

@author: pritishc
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import pytest

# This dict is used in the fixture that follows.
browsers = {'firefox': webdriver.Firefox}

# Session scope fixture.
@pytest.fixture(scope='session', params=browsers.keys())
def driver_init(request):
    if 'DISPLAY' not in os.environ:
        pytest.skip('Test requires display server (export DISPLAY)')
        
    # webdriver.Firefox() or webdriver.Chrome()    
    browse = browsers[request.param]() 
    
    # This line adds a finalizer to the request object, which here is a lambda
    # function that asks the browser to quit after it's done with the test.
    # Missile command shutdown.
    request.addfinalizer(lambda *args: browse.quit())
    
    return browse
    
# Fixture that returns the required browser object.
# Used as a per function fixture.
@pytest.fixture
def browser(driver_init):
    b = driver_init
    b.set_window_size(1200, 800)
    b.get('localhost:8000')
    
    return b

#@pytest.mark.xfail(reason="Need to add the requisite features")
def test_start_list_retrieve_later(browser):
    """
    This test does some stuff in the browser. We use some methods provided by
    the Selenium browser object. We test things like the text within <H1>. We
    obtain a reference to an inputbox by its ID, and check that its 'placeholder'
    attribute is as we set it. We also send text to the inputbox.
    Lastly, we check that a table's tr element has our required text in any of
    its rows.
    """
    browser.get('http://localhost:8000')
    
    #assert 'Django' in browser.title
    assert 'To-Do' in browser.title, "Browser title was " + browser.title
    header_text = browser.find_element_by_tag_name('h1').text
    assert 'To-Do' in header_text
    
    inputbox = broswer.find_element_by_id('id_new_item')
    assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'
    
    inputbox.send_keys('Buy peacock feathers')
    
    inputbox.send_keys(Keys.ENTER)
    
    table = browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    
    assert any(row.text == '1: Buy peacock feathers' for row in rows)
