from django.http import HttpResponse
from django.shortcuts import render
from .models import place, people


def about(request):
    obj=place.objects.all()
    obj1=people.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})


