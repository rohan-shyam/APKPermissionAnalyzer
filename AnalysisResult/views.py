from django.shortcuts import render
from django.http import HttpResponseBadRequest
import subprocess
import tempfile


# Create your views here.
def analyze_apk(request):
    if request.method == "POST":

        apk_file = request.FILES.get("apk")

        if not apk_file or not apk_file.name.endswith(".apk"):
            return HttpResponseBadRequest("Please upload a valid APK file.")
        
        with tempfile.NamedTemporaryFile(suffix=".apk", delete=False) as tmp:
            for chunk in apk_file.chunks():
                tmp.write(chunk)
            apk_path = tmp.name
    
       
    else:
        return HttpResponseBadRequest("Invalid request method.")
    
    result = subprocess.run(
        ["aapt", "dump", "badging", apk_path],
        capture_output=True,
        text=True,
        timeout=10
    )

    if result.returncode != 0:
        return HttpResponseBadRequest("aapt failed")
    
    permissions = []
    for line in result.stdout.splitlines():
        if line.startswith("uses-permission:"):
            perm = line.split("name='")[1].split("'")[0]
            permissions.append(perm)

    return render(
        request,
        "main/analysis.html",
        {
            "apk_name": apk_file.name,
            "permissions": [
                {
                    "name": p,
                    "risk": "Unknown",
                    "description": "Declared in AndroidManifest.xml"
                }
                for p in permissions
            ]
        }
    )
    