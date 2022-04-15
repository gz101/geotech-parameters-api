from django.urls import path

from . import views


urlpatterns = [
    path('water_standpipe', views.render_water_standpipe),
    path('pore_pressure', views.render_pore_pressure),
    path('settlement/<str:direction>', views.render_settlement),
    path('all', views.all, name='all'),
]
