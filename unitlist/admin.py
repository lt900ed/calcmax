from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Attribute)
admin.site.register(UnitType)
admin.site.register(Unit)
admin.site.register(Role)