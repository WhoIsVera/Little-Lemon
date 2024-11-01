from django.shortcuts import render
#from .models import Menu
# Create your views here La vista recibe el objeto de solicitud HTTP.

def index(request):
    return render(request, 'index.html', {})


