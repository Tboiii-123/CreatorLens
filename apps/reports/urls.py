from django.urls import path
from .views import get_reports
urlpatterns = [
    path('',get_reports, name='report')
]