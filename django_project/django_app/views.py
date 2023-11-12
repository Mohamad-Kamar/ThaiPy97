from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, this is a Django server!")
