from django.contrib import admin
from .models import MenuSubItems, MenuBaseItems, ContactInfo, SocialMediaIcon, Carousel, Brand, SectionInfo, \
    ServiceIcon, Tag, MiniSwipe
from adminsortable2.admin import SortableAdminMixin


class SocialMediaIconAdmin(admin.ModelAdmin):
    fields = ("url", "icon", "color",)
    list_display = ("icon", "url", "color")


class CarouselAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('get_image', 'title', 'sort_order')
    list_editable = ('title',)
    list_display_links = ('get_image',)
    search_fields = ('title', 'pretitle',)
    list_filter = ('pretitle', 'sort_order',)
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


class TagAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "url", "sort_order",)
    fields = ("title", "url", 'sort_order',)
    list_filter = ('title', 'sort_order',)
    # readonly_fields = ('sort_order',)


class SwiperAdmin(admin.ModelAdmin):
    fields = ("idiom", "author", "author_profession", "author_image",)
    list_display = ("get_image", "idiom", "author", "author_profession",)


class SectionInfoAdmin(admin.ModelAdmin):
    fields = (
        "section", "pretitle", "title", "description", "button_text", "button_url", "secondary_button_text",
        "secondary_button_url", "video_source", "image", "image2",)
    list_display = ("get_image", "title", "section")
    search_fields = ('title', 'pretitle', "description")
    list_filter = ('section',)


class VideoSectionAdmin(admin.ModelAdmin):
    fields = ("pretitle", "title", "video_source", "image",)
    list_display = ("get_image", "title", "pretitle",)
    search_fields = ('title', 'pretitle',)
    list_editable = ('pretitle', 'title',)


class ServiceIconAdmin(admin.ModelAdmin):
    fields = ("title", "url", "type", "icon", "image", "description")
    list_display = ("get_image", "title", "type",)
    list_filter = ("title", "type",)


admin.site.register(MenuBaseItems)
admin.site.register(MenuSubItems)
admin.site.register(ContactInfo)
admin.site.register(SocialMediaIcon, SocialMediaIconAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SectionInfo, SectionInfoAdmin)
admin.site.register(ServiceIcon, ServiceIconAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(MiniSwipe, SwiperAdmin)
