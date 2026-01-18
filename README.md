**APK Permission Analyzer**

A web-based static analysis tool that inspects Android APK files and evaluates their security risk based on the permissions declared in the AndroidManifest.xml.

The APK is never installed or executed. All analysis is static and performed using official Android SDK tooling.

---
<img width="1920" height="1080" alt="Screenshot From 2026-01-18 20-28-32" src="https://github.com/user-attachments/assets/01f3c266-fa7c-4dd3-a381-f7bb2359843f" /> <img width="1920" height="1080" alt="Screenshot From 2026-01-18 20-28-39" src="https://github.com/user-attachments/assets/6aac356b-9fdf-4bcb-9115-7e659630ad6f" />
--- 
**How The Analysis Works**

- The user uploads an APK file
- Django stores the APK in a temporary location
- Android SDK tool aapt extracts manifest data
- Permissions are parsed on the server
- A deterministic risk model assigns weighted values
- The final score is normalized and displayed
- No dynamic execution, emulation, or decompilation is performed.
---
**Security Risk Scoring Model**

Permissions are grouped by sensitivity:

**Low impact permissions**
Examples: Bluetooth, Wake Lock, Foreground Service

**Medium impact permissions**
Examples: Network access, Boot completed, Billing

**Sensitive permissions**
Examples: Microphone, Camera, Location

**Critical permissions**
Examples: SMS access, Package installation

---

**Technology Used**

Backend: Django (Python)

Android Analysis: Android SDK Build Tools (aapt)

Frontend: HTML,CSS

---

**Setup Steps**

- Clone the repository
- Create and activate a virtual environment
    1. python -m venv .venv
    2. source .venv/bin/activate
 - Install dependencies
    1. pip install django
 - Install Android build tools
    1. sdkmanager "build-tools;34.0.0"

- Verify aapt is available
  1. which aapt
- Run the development server
  1. python manage.py runserver
  2. Open the app in your browser
     https://127.0.0.1:8000/




