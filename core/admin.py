from django.contrib import admin
from .models import ContactInfo, SocialMediaIcon, Tag, Project, ProjectImage, Category, TeamMember, ContactUsPageData, \
    AboutUsSwiper, AccordionItem
from adminsortable2.admin import SortableAdminMixin

admin.site.register(ContactInfo)
admin.site.register(Tag)


@admin.register(SocialMediaIcon)
class SocialMediaIconAdmin(admin.ModelAdmin):
    fields = ("url", "icon", "color",)
    list_display = ("icon", "url", "color")


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


@admin.register(ContactUsPageData)
class ContactPageAdmin(admin.ModelAdmin):
    # fields = ["pretitle", "title", "description", "button_text", "button_url", "image", "pretitle_2", "title_2",
    #           "image2", ]
    list_display = ['get_image', 'pretitle', 'title', ]
    fieldsets = [
        (
            "1-ci hissə",
            {
                "fields": ["pretitle", "title", "description", "button_text", "button_url", "image", ]
            }
        ),
        (
            "2-ci hissə",
            {
                "fields": ["pretitle_2", "title_2", ]
            }
        ),

    ]

    class SwiperInline(admin.TabularInline):
        model = AboutUsSwiper
        extra = 1

    class AccordionInline(admin.TabularInline):
        model = AccordionItem
        extra = 1

    inlines = [SwiperInline, AccordionInline]
