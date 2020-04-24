from django.shortcuts import render
from django.http import request
from ry import models
from django.views.generic import ListView
import os

# Create your views here.

def template(request):
    return render(request,'test.html',{'num':2})

def detail(request):
    errors = []
    if 'sfid' in request.GET :
        number = request.GET['sfid']
        thisDir = os.path.dirname(__file__)
        photoPath = os.path.join(thisDir,"static\photo")
        photoFile =  r"/static/photo/noPhoto.jpg"
              
        try:
            person = models.Person.objects.get(Id_Number = number)
            photofiles = [number+'.jpg',number+'.gif',number+'.png']
            for file in photofiles:
                testPath = os.path.join(photoPath,file)
                if(os.path.exists(testPath)):
                    photoFile = r"/static/photo/"+file
                    break 
             
            return render(request,'ry/detail.html',{'person':person,'photoFile':photoFile})
        except models.Person.DoesNotExist:
            if len(number) == 0:
                errors.append('请输入身份证号！')
            elif len(number) != 18:
                errors.append('身份证号格式不对！')
            else:
                errors.append('没有此人信息！')
                      
    return render(request,'ry/detail.html',{'errors':errors})

def list(request):
    persons = models.Person.objects.all()
    return render(request,'ry/list.html',{'persons':persons})

class PersonList(ListView):
    model = models.Person

    