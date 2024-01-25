from django.urls import path

from apps.current_usd.views import get_current_usd


urlpatterns = [
    path('/', get_current_usd)
]
