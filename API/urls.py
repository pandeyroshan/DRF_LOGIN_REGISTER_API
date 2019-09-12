from django.contrib import admin
from django.urls import path
from core.views import login,sample_api,register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('api/register', register),
    path('api/test', sample_api)
]