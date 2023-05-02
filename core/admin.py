from django.contrib import admin
from .models import MenuSubItems, MenuBaseItems, ContactInfo, SocialMediaIcon


class SocialMediaIconAdmin(admin.ModelAdmin):
    fields = ("url", "icon", "color", )
    list_display = ("icon", "url", "color")


admin.site.register(MenuBaseItems)
admin.site.register(MenuSubItems)
admin.site.register(ContactInfo)
admin.site.register(SocialMediaIcon, SocialMediaIconAdmin)
