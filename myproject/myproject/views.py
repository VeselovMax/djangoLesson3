from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Message
from .models import Counter
from myapp.forms import NameForm

def home(request):
    return HttpResponse(f"Home")

def hello(request):
    form = NameForm()
    name = ""
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            Message.objects.create(name=name)
    return render (request, "hello.html", {"form": form, "name": name })


def stats(request):
    total_greetings = Message.objects.count()
    names = set(Message.objects.values_list('name', flat=True))
    return render(request, 'stats.html', {'total_greetings': total_greetings, 'names': names})

def stats_name(request, name):
    messages = Message.objects.filter(name=name)
    return render(request, 'stats_name.html', {'greetings': messages, 'name': name})