from django.urls import path
from .views import get_videos, add_api_key

urlpatterns = [
    path('video', get_videos),
    path('api-key', add_api_key),
]
