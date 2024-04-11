from django.urls import path
from . import views

urlpatterns=[
  path('', views.index, name='index'),
  path('areas', views.areas, name='areas'),
  path('attractions', views.attractions, name='attractions'),
  path('areas/<int:id>', views.single_area, name='single_area'),
]