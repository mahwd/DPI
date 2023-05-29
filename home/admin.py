from django.contrib import admin
from .models import MenuItems, Carousel, InfoTag, Brand, \
    ServiceIcon, MiniSwipe, SectionInfo, ServicePlan
from adminsortable2.admin import SortableAdminMixin


@admin.register(MenuItems)
class MenuItemsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'url', 'sort_order')
    list_display_links = ('title', 'url',)
    search_fields = ('title', 'url',)
    list_filter = ('parent',)
    readonly_fields = ('sort_order',)


@admin.register(Carousel)
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


@admin.register(Brand)
class BrandAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ("title", "image", "url",)
    list_filter = ('title', )
    # list_editable = ('title',)
    list_display = ("get_image", "title", "url", "sort_order")
    # readonly_fields = ('sort_order',)


@admin.register(InfoTag)
class InfoTagAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "url", "active", "sort_order",)
    fields = ("title", "url", "active", 'sort_order',)
    list_filter = ('title', 'sort_order',)
    # readonly_fields = ('sort_order',)


@admin.register(ServiceIcon)
class ServiceIconAdmin(admin.ModelAdmin):
    fields = ("title", "url", "type", "icon", "image", "description")
    list_display = ("get_image", "title", "type",)
    list_filter = ("title", "type",)


@admin.register(MiniSwipe)
class SwiperAdmin(admin.ModelAdmin):
    fields = ("idiom", "author", "author_profession", "author_image", "active",)
    list_display = ("get_image", "idiom", "author", "author_profession", "active",)


@admin.register(SectionInfo)
class SectionInfoAdmin(admin.ModelAdmin):
    fields = (
        "section", "pretitle", "title", "description", "button_text", "button_url", "secondary_button_text",
        "secondary_button_url", "video_source", "image", "image2",)
    list_display = ("get_image", "title", "section")
    search_fields = ('title', 'pretitle', "description")
    list_filter = ('section',)


@admin.register(ServicePlan)
class ServicePlanAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price", "currency", "active")
    fields = ("title", "description", "price", "currency", "active")
    list_filter = ('title',)
