from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(httprequest):
    item = Item()
    item.text = httprequest.POST.get('item_text', '')
    item.save()

    return render(httprequest, 'home.html',
        {'new_item_text': item.text,})