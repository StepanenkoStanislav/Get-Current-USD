from django.urls import path, include


urlpatterns = [
    path('get-current-usd', include('apps.current_usd.urls')),
]
