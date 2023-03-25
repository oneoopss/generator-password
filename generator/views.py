from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    abc = list('qwertyuiopasdfghjklzxcvbnm')
    length = request.GET.get('length')

    if request.GET.get('uppercase'):
        abc.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    if request.GET.get('numbers'):
        abc.extend('0123456789')
    if request.GET.get('symbols'):
        abc.extend('!@#$%^&*()')

    for i in range(int(length)):
        thepassword += random.choice(abc)


    return render(request, 'generator/password.html', {'password':thepassword})

def discription(request):
    return render(request, 'generator/discription.html')