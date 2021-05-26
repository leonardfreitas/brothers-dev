from django.contrib import admin
from django.urls import path

from employee.views import create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create)
]
