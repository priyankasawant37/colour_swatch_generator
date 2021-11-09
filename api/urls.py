from django.urls import path
from . import views


urlpatterns = [

path('', views.routes, name='routes'),
path('generate_colours/', views.generate_colours, name='generate_colours'),
path('show_swatch/', views.show_swatch, name='show_swatch'),
path('rgb_to_hls/', views.rgb_to_hls, name='rgb_to_hls')
]
