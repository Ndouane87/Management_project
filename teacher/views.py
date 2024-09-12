from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def project(request):
    return render(request, 'main/project.html')