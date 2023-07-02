from django.shortcuts import render
from .models import *
# Create your views here.
def AutoView(request):
    data = AutoComponents.objects.all()
    return render(request, 'auto.html', {'data': data})
