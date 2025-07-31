from django.http import HttpResponse

def home(request):
    return HttpResponse("hello, this is our first Django website");

def about(request):
    return HttpResponse("hello, this is our about page");

def contact(request):
    return HttpResponse("hello, this is our contact page");