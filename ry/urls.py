from django.urls import path
from . import views

app_name = "ry"
urlpatterns = [
    path('test/',views.template),
    path('detail/',views.detail,name="ry_detail"),
    path('list/',views.list,name="ry_list"),
    path('persons/',views.PersonList.as_view(),name="list_person"),
    path("add-person/",views.addPerson_s.as_view(),name="add_person"),
]