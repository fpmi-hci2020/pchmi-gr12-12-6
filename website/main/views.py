from django.shortcuts import render
from .models import Tickets

def mainpage(request):
    return render(request, 'main/mainpage.html')


def news(request):
    return render(request, 'main/news.html')


def tickets(request):
    tickets = Tickets.objects.all()
    return render(request, 'main/tickets.html', {'tickets': tickets})

