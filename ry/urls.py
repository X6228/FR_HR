from django.urls import path
from ry import views

apps_name = 'ry'
urlpatterns = [
    path('test/',views.template),
    path('detail',views.detail),
    path('list',views.list),
    path('persons',views.PersonList.as_view()),
]