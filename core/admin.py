from django.contrib import admin
from .models import MenuSubItems, MenuBaseItems, ContactInfo, SocialMediaIcon, Carousel, Brand
from adminsortable2.admin import SortableAdminMixin


class SocialMediaIconAdmin(admin.ModelAdmin):
    fields = ("url", "icon", "color",)
    list_display = ("icon", "url", "color")


class CarouselAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('get_image', 'pretitle', 'title', 'sort_order')
    list_editable = ('pretitle', 'title', )
    list_display_links = ('get_image', )
    search_fields = ('title', 'pretitle',)
    list_filter = ('pretitle',)
    fieldsets = (
        ('Text', {'fields': ('pretitle', 'title', 'description')}),
        ('Image', {'fields': ('image',)}),
        ('Left Button', {'fields': ('left_button_text', 'left_button_url')}),
        ('Right Button', {'fields': ('right_button_text', 'right_button_url')}),
    )
    readonly_fields = ('sort_order',)


class BrandAdmin(admin.ModelAdmin):
    fields = ("title", "image", "url",)
    list_display = ("get_image", "title", "url",)


admin.site.register(MenuBaseItems)
admin.site.register(MenuSubItems)
admin.site.register(ContactInfo)
admin.site.register(SocialMediaIcon, SocialMediaIconAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Brand, BrandAdmin)
