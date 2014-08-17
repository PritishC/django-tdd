from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(httprequest):
    if httprequest.method == 'POST':
        return HttpResponse(httprequest.POST['item_text'])
    return render(httprequest, 'home.html')