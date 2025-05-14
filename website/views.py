from django.shortcuts import render
from website.models import Contact

# Create your views here.
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request, 'web_temp/index.html')


def about_view(request):
    return render(request, 'web_temp/about.html')


def contact_view(request):
    return render(request, 'web_temp/contact.html')


def test(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        c.save()
        print(name, email, subject, message)

    return render(request, 'test.html')
