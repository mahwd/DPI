from django.contrib import admin
from .models import MenuSubItems, MenuBaseItems, ContactInfo, SocialMediaIcon, Carousel, Brand, SectionInfo, \
    ServiceIcon, InfoTag, Tag, MiniSwipe, Project, ProjectImage, Category, TeamMember, ServicePlan
from adminsortable2.admin import SortableAdminMixin

admin.site.register(MenuBaseItems)
admin.site.register(MenuSubItems)
admin.site.register(ContactInfo)
admin.site.register(Tag)


@admin.register(SocialMediaIcon)
class SocialMediaIconAdmin(admin.ModelAdmin):
    fields = ("url", "icon", "color",)
    list_display = ("icon", "url", "color")


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
class BrandAdmin(admin.ModelAdmin):
    fields = ("title", "image", "url",)
    list_display = ("get_image", "title", "url",)


@admin.register(SectionInfo)
class SectionInfoAdmin(admin.ModelAdmin):
    fields = (
        "section", "pretitle", "title", "description", "button_text", "button_url", "secondary_button_text",
        "secondary_button_url", "video_source", "image", "image2",)
    list_display = ("get_image", "title", "section")
    search_fields = ('title', 'pretitle', "description")
    list_filter = ('section',)


@admin.register(ServiceIcon)
class ServiceIconAdmin(admin.ModelAdmin):
    fields = ("title", "url", "type", "icon", "image", "description")
    list_display = ("get_image", "title", "type",)
    list_filter = ("title", "type",)


@admin.register(InfoTag)
class InfoTagAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "url", "active", "sort_order",)
    fields = ("title", "url", "active", 'sort_order',)
    list_filter = ('title', 'sort_order',)
    # readonly_fields = ('sort_order',)


@admin.register(MiniSwipe)
class SwiperAdmin(admin.ModelAdmin):
    fields = ("idiom", "author", "author_profession", "author_image", "active",)
    list_display = ("get_image", "idiom", "author", "author_profession", "active",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display_links = ("get_image", "title", "slug", "category",)
    list_display = ("get_image", "title", "slug", "category",)
    fields = ("title", "content", 'category', 'tags')
    list_filter = ('category', 'tags')

    class ProjectImageInline(admin.TabularInline):
        model = ProjectImage
        extra = 1

    inlines = [ProjectImageInline]


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("get_image", "fullname", "profession", "info", "email",)
    fields = ("fullname", "profession", "image", "info", "email",)
    list_filter = ('profession',)


@admin.register(ServicePlan)
class ServicePlanAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price", "currency", "active")
    fields = ("title", "description", "price", "currency", "active")
    list_filter = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug",)
    fields = ("title",)
    list_filter = ('title', 'slug',)


# class FaqAdmin(admin.ModelAdmin):
#     list_display = ("get_image", "question", "sort_order",)
#     fields = ("question", "answer", "image",)
#     list_filter = ('sort_order',)

# admin.site.register(FAQ, FaqAdmin)
