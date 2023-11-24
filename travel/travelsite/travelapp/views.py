from django.shortcuts import render
from . models import place,founder

# Create your views here.
def func(request):
    fetch = place.objects.all()
    found = founder.objects.all()
    return render(request,'index.html',{'get':fetch,'pass':found})