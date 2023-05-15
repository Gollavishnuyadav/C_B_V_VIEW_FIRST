from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View
# Create your views here.
def fbv(request):
    return HttpResponse("view")

class Cbv(View):
    def get(self,request):
        return HttpResponse('Cbv')

def f_t(request):
    return render(request,'f_t.html')


class c_t(View):
    def get(self,request):
        return render(request,'c_t.html')
    

def formm(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        DD=TopicForm(request.POST)
        if DD.is_valid():
            DD.save()
            return HttpResponse('Done')
    return render(request,'ff_t.html',d)

class CBB(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'ff_t.html',d)

    def post(self,request):
        DD=TopicForm(request.POST)
        if DD.is_valid():
            DD.save()
            return HttpResponse('Data Inserted Done')