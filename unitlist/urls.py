from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('unit/', views.unitlist, name='unitlist'),
    path('char/', views.charlist, name='charlist'),
    path('equip/', views.equiplist, name='equiplist'),
]