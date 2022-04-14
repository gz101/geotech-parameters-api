from django.urls import path

from . import views


urlpatterns = [
    path('water_standpipe', views.water_standpipe, name='water_standpipe'),
    path('pore_pressure', views.pore_pressure, name='pore_pressure'),
    path('settlement_x', views.settlement_x, name='settlement_x'),
    path('settlement_y', views.settlement_y, name='settlement_y'),
    path('settlement_z', views.settlement_z, name='settlement_z'),
]
