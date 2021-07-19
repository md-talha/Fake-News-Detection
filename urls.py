from django.urls import path

from . import views

urlpatterns=[
	path('',views.index, name='index'),
	path('insert',views.insert, name='insert'),
	path('alogin',views.alogin, name='alogin'),
	
	
]