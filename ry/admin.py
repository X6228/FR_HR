from django.contrib import admin
from ry.models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ("Name","Gender","Id_Number","Birthday")

admin.site.register(Person,PersonAdmin)
