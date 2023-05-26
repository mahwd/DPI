from django.db import models
import os
import uuid
from django.utils.html import mark_safe
from .custom import fields
from .custom.custom_tools import get_image_html
from django.core.files.uploadedfile import InMemoryUploadedFile
from .custom.custom_tools import slugify
from django.urls import reverse


class MyModel(models.Model):

    @classmethod
    def get_fields(cls, fields: tuple):
        return fields.__add__(('created_at', 'updated_at', 'active'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dəyişdirilmə tarixi")
    active = models.BooleanField(default=True, verbose_name="Aktivdirmi")

    class Meta:
        abstract = True


class ContactInfo(MyModel):
    email = models.EmailField(max_length=128, verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Phone")
    address = models.TextField(max_length=300, verbose_name="Ünvan")

    class Meta:
        verbose_name = "Əlaqə vasitələri"
        verbose_name_plural = "Əlaqə vasitələri informasiya"

    def __str__(self):
        return self.email


class SocialMediaIcon(MyModel):
    color_choices = [
        ("primary-color", "primary"),
        ("secondary-color", "secondary"),
        ("accent-color", "accent"),
        ("dark-color", "dark")
    ]

    url = models.CharField(max_length=128, verbose_name="URL")
    icon = models.CharField(max_length=128, verbose_name="Icon")
    color = models.CharField(max_length=128, choices=color_choices, verbose_name="Color")

    def __str__(self):
        return self.icon

    class Meta:
        verbose_name = "Sosial media"
        verbose_name_plural = "Sosiallar"


class Brand(MyModel):
    title = models.CharField(max_length=128, verbose_name="Ad")
    url = models.CharField(max_length=255, verbose_name="URL")
    image = models.ImageField(upload_to="brand_image/", verbose_name="Brend şəkli")

    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlər"

    def __str__(self):
        return self.title

    def get_image(self):
        return get_image_html(self.image.url, self.title)

    image.short_description = "Brand image"
    image.allow_tags = True


class Tag(MyModel):
    title = models.CharField(max_length=255, verbose_name="Teq adı")

    class Meta:
        verbose_name = "Teq"
        verbose_name_plural = "Teqlər"

    def __str__(self):
        return self.title


class Project(MyModel):
    title = models.CharField(max_length=255, verbose_name='Başlıq')
    slug = models.SlugField(unique=True, blank=True, default=uuid.uuid1, max_length=150, verbose_name="Slug")
    content = models.TextField(verbose_name='Mətn')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="projects")
    tags = models.ManyToManyField("Tag", related_name="tags", verbose_name="Teqlər")

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio proyektlər"

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("portfolio_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def get_image(self):
        return get_image_html(self.images.last().image.url if self.images.last() else None, self.title)


class Category(MyModel):
    title = models.CharField(max_length=255, verbose_name='Kateqorioya adı')
    slug = models.SlugField(unique=True, blank=True, default=uuid.uuid1, max_length=150, verbose_name="Slug")

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class ProjectImage(MyModel):
    image = models.ImageField(null=True, blank=True, upload_to='project_images', verbose_name='Şəkil')
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="images", verbose_name="Proyekt")

    class Meta:
        verbose_name = "Portfolio şəkli"
        verbose_name_plural = "Portfolio şəkilləri"

    def __str__(self):
        return f"{self.project.title}"

    def delete(self, *args, **kwargs):
        # Delete the image file from disk when the model is deleted
        self.image.delete() if self.image else None
        super().delete(*args, **kwargs)

    def get_image(self):
        return get_image_html(self.image.url if self.image else None, self.project.title)


# class FAQ(MyModel):
#     question = models.TextField(max_length=500, verbose_name='Sual')
#     answer = models.TextField(max_length=500, verbose_name='Cavab')
#     image = models.ImageField(null=True, blank=True, upload_to="faq_images", verbose_name="Şəkil")
#     sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
#
#     class Meta:
#         verbose_name = "FAQ"
#         verbose_name_plural = "FAQs"
#         ordering = ['sort_order']
#
#     def __str__(self):
#         return f"{self.title}"
#
#     def save(self, *args, **kwargs):
#         if self.sort_order is None:
#             try:
#                 last_item = type(self).objects.filter(sort_order__isnull=False).order_by('-sort_order').first()
#                 if last_item:
#                     self.sort_order = last_item.sort_order + 1
#             except type(self).DoesNotExist:
#                 pass
#         super().save(*args, **kwargs)
#
#     def get_image(self):
#         return get_image_html(self.image.url if self.image else None, self.question)


class TeamMember(MyModel):
    fullname = models.CharField(max_length=255, verbose_name='Əməkdaşın ad, soyadı')
    profession = models.CharField(max_length=255, verbose_name='Əməkdaşın vəzifəsi')
    image = models.ImageField(upload_to="member_images", verbose_name="Əməkdaşın şəkli")
    info = models.TextField(max_length=500, verbose_name='Əməkdaşın bio-su')
    email = models.EmailField(max_length=100, verbose_name='Əməkdaşın elektron poçt ünvanı')
    slug = models.SlugField(unique=True, default=uuid.uuid4, max_length=150, verbose_name="Slug")

    class Meta:
        verbose_name = "Əməkdaş"
        verbose_name_plural = "Əməkdaşlar"

    def __str__(self):
        return self.fullname

    def get_image(self):
        return get_image_html(self.image.url if self.image else None, self.fullname)

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fullname)
        super(TeamMember, self).save(*args, **kwargs)
