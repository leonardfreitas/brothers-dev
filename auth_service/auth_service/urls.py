from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

from tickets.views import can_access

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signin/', views.obtain_auth_token),
    path('api/can-access/<int:id>/', can_access)
]
