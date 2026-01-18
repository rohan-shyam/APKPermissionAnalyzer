from django.shortcuts import render

def home(request):
    return render(request, "main/index.html")


def analyze_apk(request):
    return render(request, "main/analysis.html")