from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # in future we can fix our react-app here
    # return render(request, "index.htmx" )
    return HttpResponse("hi the application is running")