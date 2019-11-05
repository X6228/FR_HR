from django.urls import path
from ry import views

apps_name = 'ry'
urlpatterns = [
    path('test/',views.template),
    
]