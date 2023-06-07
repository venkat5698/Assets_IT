from django.urls import path
from .views import asset_details

urlpatterns = [
    path('asset_details/', asset_details, name='asset_details'),
]
