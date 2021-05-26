from django.contrib import admin

from .models import Service, Target, Action

admin.site.register(Service)
admin.site.register(Target)
admin.site.register(Action)
