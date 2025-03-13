from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request, 'web_temp/index.html')


def about_view(request):
    return render(request, 'web_temp/about.html')


def contact_view(request):
    return render(request, 'web_temp/contact.html')
