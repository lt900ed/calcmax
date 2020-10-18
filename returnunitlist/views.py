import json
from collections import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from unitlist.models import Unit, UnitType
from .models import UnitSet
from .forms import UnitSetForm
from time import sleep

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = UnitSetForm(request.POST)
		if form.is_valid():
			units_in = ['fire_dragon', 'pirates_girl', 'clarisse', 'battle_maid_xm19', 'compliment_oiran', 'heavenly_one', 'black_wolf_knight', 'tiger_treasure_hunter_smr20', 'brown_fighter', 'onmyoji_boy', 'lightbullet_wiz_ny20', 'ice_witch']
			units = Unit.objects.select_related('attribute').filter(unit_id__in = units_in).order_by('unit_no')

			data = serializers.serialize('json', units)

#			return render_json_response(request, data)
			return HttpResponse(data, content_type='application/javascript; charset=UTF-8', status=None)
	else:
		form = UnitSetForm()
		return render(request, 'returnunitlist/index.html', {'form': form})

def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response

def api(request):
	units = Unit.objects.all().order_by('unit_type', 'unit_no')
	sleep(5)
	return render(request, 'returnunitlist/unitlist.html', {'title': 'units' , 'units': units})
