from django.shortcuts import render
from . models import Persons

# Create your views here.
def demo(request):
    obj = Persons.objects.all()
    return render(request, "index.html", {'result': obj})


