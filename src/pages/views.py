from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 321, 789]
    }
    return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
