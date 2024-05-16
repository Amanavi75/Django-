from django.http import HttpResponse


def home(request):
    return HttpResponse("hello , world you are at chai aur django home page ")
def about(request):
    return HttpResponse("hello , world you are at chai aur django about page ")
def contact(request):
    return HttpResponse("hello , world you are at chai aur django contact page ")
