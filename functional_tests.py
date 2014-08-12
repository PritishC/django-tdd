# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:47:08 2014

@author: pritishc
"""

from selenium import webdriver
import pytest

# This dict is used in the fixture that follows.
browsers = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome}

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

@pytest.mark.xfail(reason="To-Do not in title yet")
def test_start_list_retrieve_later(browser):
    # Obtain missile command from Firefox silos
    browser.get('http://localhost:8000')
    
    # Check title 
    #assert 'Django' in browser.title
    assert 'To-Do' in browser.title, "Browser title was " + browser.title