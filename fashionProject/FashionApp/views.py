from django.http import HttpResponse
from django.shortcuts import render
from FashionApp.models import *
import datetime
from FashionApp.forms import *

# Create your views here.

def inicio(request):
    return render(request , 'index.html')

def fashionIconsList(request):
    fashionIcons = FashionIcons.objects.all()
    data = {'data' : fashionIcons}

    return render(request, 'fashionIconsList.html', data)


def fashionBrandsList(request):
    fashionBrands = FashionBrands.objects.all()
    data = {'data' : fashionBrands}

    return render(request, 'fashionBrandsList.html', data)

def fashionShowsList(request):
    fashionShows = FashionShows.objects.all()
    data = {'data' : fashionShows}

    return render(request, 'fashionShowsList.html', data)

def form_fashionIcons(request):

    if request.method == 'POST':
        my_form = FashionIcons_form( request.POST )

        if my_form.is_valid():
            data = my_form.cleaned_data

            icon = FashionIcons(name = data['name'] , age = data['age'] , dateOfBirth = data['dateOfBirth'] , profession = data['profession'] , description = data['description'])
            icon.save()

            return render(request, 'form_fashionIcons.html')

    return render(request, 'form_fashionIcons.html')

def form_fashionBrands(request):

    if request.method == 'POST':
        my_form = FashionBrands_form( request.POST )

        if my_form.is_valid():
            data = my_form.cleaned_data

            brand = FashionBrands(name = data['name'] , founder = data['founder'] , foundedDate = data['foundedDate'] , headquarters = data['headquarters'], description = data['description'])
            brand.save()

            return render(request, 'form_fashionBrands.html')

    return render(request, 'form_fashionBrands.html')

def form_fashionShows(request):
    if request.method == 'POST':
        my_form = FashionShows_form( request.POST )

        if my_form.is_valid():
            data = my_form.cleaned_data

            show = FashionShows(name = data['name'] , brand = data['brand'] , date = data['date'] , fashionCapital = data['fashionCapital'], collectionPresented = data['collectionPresented'] , description = data['description'])
            show.save()

            return render(request, 'form_fashionShows.html')

    return render(request, 'form_fashionShows.html')


def search_fashionIcons(request):

    return render(request, 'search_fashionIcons.html')

def searchResults_fashionIcons(request):
    if request.GET['name']:
        name= request.GET['name']
        icons = FashionIcons.objects.filter(name__icontains = name)
        return render(request, 'searchResults_fashionIcons.html', {'icons': icons})
    else:
        return HttpResponse("There wasn't a match.")