from django.http import HttpResponse
from django.shortcuts import render 


def home(request):
   # return HttpResponse("hello , world you are at chai aur django home page ")
   return render(request, 'index.html')
def about(request):
    return HttpResponse("hello , world you are at chai aur django about page ")
def contact(request): 
    return HttpResponse("hello , world you are at chai aur django contact page ")
def contact(request): 
    return HttpResponse("hello , world you are at chai aur django contact page ")
def contact(request): 
    return HttpResponse("hello , world you are at chai aur django contact page ")
