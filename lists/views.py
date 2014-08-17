from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(httprequest):
    if httprequest.method == 'POST':
        new_item_text = httprequest.POST['item_text']
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''

    return render(httprequest, 'home.html',
        {'new_item_text': new_item_text,})