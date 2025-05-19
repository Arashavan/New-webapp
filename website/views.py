from django.shortcuts import render
from website.models import Contact
from website.forms import ContactForm
from django.contrib import messages


# Create your views here.
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request, 'web_temp/index.html')


def about_view(request):
    return render(request, 'web_temp/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your from has been sent!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Something Went Wrong!!!, Try again')
        form = ContactForm()
    return render(request, 'web_temp/contact.html')


def test(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.changed_data['subject']
            message = form.cleaned_data['message']
            print(name, email, subject, message)
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

            # name = request.POST.get('name')
            # email = request.POST.get('email')
            # subject = request.POST.get('subject')
            # message = request.POST.get('message')
            # c = Contact(
            #     name=name,
            #     email=email,
            #     subject=subject,
            #     message=message
            # )
            # c.save()

    form = NameForm()
    return render(request, 'test.html', {'form': form})
