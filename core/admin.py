from django.contrib import admin
from .models import MenuSubItems, MenuBaseItems

admin.site.register(MenuBaseItems)
admin.site.register(MenuSubItems)
