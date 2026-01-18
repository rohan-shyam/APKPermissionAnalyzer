import subprocess
from django.http import HttpResponseBadRequest
from django.shortcuts import render
import tempfile 

def home(request):
    return render(request, "main/index.html")


