from django.contrib import admin
from .models import ContactInfo, SocialMediaIcon, Brand, Tag, Project, ProjectImage, Category, TeamMember
from adminsortable2.admin import SortableAdminMixin

admin.site.register(ContactInfo)
admin.site.register(Tag)


@admin.register(SocialMediaIcon)
class SocialMediaIconAdmin(admin.ModelAdmin):
    fields = ("url", "icon", "color",)
    list_display = ("icon", "url", "color")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ("title", "image", "url",)
    list_display = ("get_image", "title", "url",)


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
