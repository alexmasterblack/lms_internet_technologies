from django.shortcuts import render
from django.http import HttpResponse
from users.models import Person

# Create your views here.

def my_first_view(request):
    p: Person = Person.objects.first()
    a = Person()
    a.first_name = 'Henrik'
    a.last_name = 'Hansen'
    a.save()
    #g: Person = Person.objects.filter(first_name__contains='Henrik')
    return HttpResponse(f'name: {p.first_name}, surname: {p.last_name}')