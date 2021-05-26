from django.contrib import admin
from django.contrib.auth.models import Group

from .models import RemoteUser


class RemoteUserAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(RemoteUser, RemoteUserAdmin)
admin.site.unregister(Group)
