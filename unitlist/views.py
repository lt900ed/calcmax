from django.http import HttpResponse
from django.shortcuts import render
from .models import Unit, UnitType
from time import sleep


def index(request):
	return render(request, 'unitlist/index.html', {})

def unitlist(request):
	units = Unit.objects.all().order_by('unit_type', 'unit_no')
	sleep(5)
	return render(request, 'unitlist/unitlist.html', {'title': 'units' , 'units': units})

def charlist(request):
	units = Unit.objects.filter(unit_type=UnitType.objects.get(unit_type_desc='char')).order_by('unit_no')
	return render(request, 'unitlist/unitlist.html', {'title': 'chars', 'units': units})

def equiplist(request):
	units = Unit.objects.filter(unit_type=UnitType.objects.get(unit_type_desc='equip')).order_by('unit_no')
	return render(request, 'unitlist/unitlist.html', {'title': 'equips', 'units': units})
