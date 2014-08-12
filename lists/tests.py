# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 12:38:42 2014

@author: pritishc
"""

from django.core.urlresolvers import resolve
from lists.views import home_page
import pytest

# resolve internally resolves URLs (hooking a view function to deal with the
# HTTP request so made).
def test_root_url_resolving_to_home_page():
    found = resolve('/')
    
    # Test that resolve when called with '/' finds a function called home_page.
    assert found.func == home_page