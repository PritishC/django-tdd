# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 12:38:42 2014

@author: pritishc
"""

from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string
from lists.models import Item
import pytest

# resolve internally resolves URLs (hooking a view function to deal with the
# HTTP request so made).
def test_root_url_resolving_to_home_page():
    found = resolve('/')
    
    # Test that resolve when called with '/' finds a function called home_page.
    assert found.func == home_page

@pytest.mark.django_db
def test_home_page_return_correct_html():
    """
    This test creates a HttpRequest object, and obtains the HttpResponse when
    applied to the home_page() view function.
    The content attribute of the HttpResponse object is tested to see that it
    has certain bits of HTML. The b'' syntax is because content is in bytes.
    """
    request = HttpRequest()
    response = home_page(request)
    assert response.content.startswith(b'<html>')
    #assert '<title>To-Do lists</title>' in response.content
    #assert response.content.strip().endswith(b'</html>')
    expected_html = render_to_string('home.html')
    assert response.content.decode() == expected_html

@pytest.mark.django_db
def test_home_page_saves_POST_request():
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item'

    response = home_page(request)

    assert Item.objects.count() == 1
    new_item = Item.objects.first()
    assert new_item.text == 'A new list item'

    assert 'A new list item' in response.content.decode()
    # render_to_string takes a dict as its second arg, which contains a mapping of variables to values.
    expected_html = render_to_string('home.html', {'new_item_text': 'A new list item'})
    assert response.content.decode() == expected_html

@pytest.mark.django_db
def home_page_saves_only_when_necessary():
    request = HttpRequest()
    home_page(request)
    assert Item.objects.count() == 0

# Model tests
@pytest.mark.django_db
def test_saving_retrieving_items():
    first_item = Item()
    first_item.text = 'The first (ever) list item'
    first_item.save()

    second_item = Item()
    second_item.text = 'Item the second'
    second_item.save()

    saved_items = Item.objects.all()
    assert saved_items.count() == 2

    first_saved = saved_items[0]
    second_saved = saved_items[1]
    assert first_saved.text == 'The first (ever) list item'
    assert second_saved.text == 'Item the second'