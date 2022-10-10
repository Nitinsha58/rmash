from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello! This is Rmush </h1>.")