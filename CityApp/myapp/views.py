from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello world!!")

def login(request):
    return render(request, 'login.html')