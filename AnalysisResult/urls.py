from django.urls import path, include
from . import views

urlpatterns = [
    path('analysis/', views.analyze_apk, name='analyze_apk'),
]