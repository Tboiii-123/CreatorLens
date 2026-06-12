from django.urls import path

from .views import (
    dashboard,
    post_analytics
)

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    
    path("<int:pk>/post/", post_analytics, name="post_analytics"),
    
]