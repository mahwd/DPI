from django.db import models
from django.utils.html import mark_safe
from .custom.custom_tools import get_carousel_image, get_brand_image, get_image_html
from io import BytesIO
from PIL import Image, ImageEnhance
from django.core.files import File
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize
import os
from django.core.files.uploadedfile import InMemoryUploadedFile


def optimise_image(image):
    # Open the image using PIL
    pil_image = Image.open(image)

    # Convert the image to RGB mode if it's not already
    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')

    # Resize the image to a maximum size of 1920x1080
    pil_image.thumbnail((1920, 1080))

    # Optimize the image and save it to a BytesIO buffer
    buffer = BytesIO()
    pil_image.save(buffer, format='JPEG', optimize=True, quality=90)
    buffer.seek(0)

    # Create a new InMemoryUploadedFile from the buffer and return it
    image_name = os.path.basename(image.name)
    return InMemoryUploadedFile(buffer, None, image_name, 'image/jpeg', buffer.getbuffer().nbytes, None)


class MyModel(models.Model):

    @classmethod
    def get_fields(cls, fields: tuple):
        return fields.__add__(('created_at', 'updated_at'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="yaradılma tarixi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="dəyişdirilmə tarixi")

    class Meta:
        abstract = True


class MenuBaseItems(MyModel):
    title = models.CharField(max_length=128, verbose_name="Menu title")
    order = models.IntegerField(default=0, verbose_name="Menu order")
    url = models.CharField(default="", max_length=255, null=True, blank=True, verbose_name="Redirect url")

    # logs
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ("order",)
        verbose_name = "Əsas menu linki"
        verbose_name_plural = "Əsas menu linkləri"

    def __str__(self):
        return "%s" % self.title

    # return true if has child sub-menus
    def contain_dropdown(self):
        child_count = self.menusubitems_set.all().count()
        return True if child_count > 0 else False

    def get_childs(self):
        return self.menusubitems_set.all()


# Header menu sub-items model
class MenuSubItems(MyModel):
    title = models.CharField(max_length=128, verbose_name="Menu title")
    url = models.CharField(max_length=255, verbose_name="Redirect url")
    order = models.IntegerField(default=0, verbose_name="Menu order")
    base_header_item = models.ForeignKey(
        "MenuBaseItems",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Parent header menu",
    )
    parent_sub_item = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Parent menu",
    )

    # logs
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ("order",)
        verbose_name = "Köməkçi menu linki"
        verbose_name_plural = "Köməkçi menu linkləri"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # super(MenuSubItems, self).save(*args, **kwargs)
        if self.url.__len__() < 2:
            raise Exception("nil is not allowed")
        if self.url.startswith("/"):
            self.url = self.url[1:]
        elif self.url[::-1].startswith("/"):
            url_len = len(self.url)
            self.url = self.url[:url_len - 1]
        # self.url = (url[::-1] + "/")[::-1]
        super(MenuSubItems, self).save(*args, **kwargs)

    def has_own_child(self):
        count = MenuSubItems.objects.filter(parent_sub_item=self).count()
        return True if count > 0 else False

    def has_own_parent(self):
        return True if self.parent_sub_item else False

    def get_childs(self):
        return MenuSubItems.objects.filter(parent_sub_item=self)

    def get_absolute_url(self):
        return reverse(self.url)


class ContactInfo(MyModel):
    email = models.EmailField(max_length=128, verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Phone")

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


class Carousel(MyModel):
    pretitle = models.CharField(max_length=128, verbose_name="Ön başlıq")
    title = models.CharField(max_length=128, verbose_name="Başlıq")
    description = models.TextField(max_length=512, verbose_name="Açıqlama")
    image = models.ImageField(upload_to='carousel_images/', verbose_name="Karusel şəkli")
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[SmartResize(400, 400)],
                                     format='JPEG',
                                     options={'quality': 90})
    left_button_text = models.CharField(max_length=50, verbose_name="Soldakı düymə mətni")
    left_button_url = models.URLField(max_length=128, verbose_name="Soldakı düymə url-i")
    right_button_text = models.CharField(max_length=50, verbose_name="Sağdakı düymə mətni")
    right_button_url = models.URLField(max_length=128, verbose_name="Sağdakı düymə url-i")
    sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        verbose_name = "Karusel"
        verbose_name_plural = "Karusel"
        ordering = ['sort_order']

    def __str__(self):
        return self.title

        # before saving the instance we’re reducing the image

    def get_image(self):
        return get_image_html(self.image.url if self.image else None, self.title)

    image.short_description = "Carousel image"
    image.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.id and not self.image_thumbnail:
            self.image = optimise_image(self.image)
        if self.sort_order is None:
            try:
                last_item = type(self).objects.filter(sort_order__isnull=False).order_by('-sort_order').first()
                if last_item:
                    self.sort_order = last_item.sort_order + 1
            except type(self).DoesNotExist:
                pass

        super().save(*args, **kwargs)

    def optimize_image(self, image):
        return optimise_image(image)

    def delete(self, *args, **kwargs):
        # Delete the image file from disk when the model is deleted
        self.image.delete()
        super().delete(*args, **kwargs)


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


class VideoSection(MyModel):
    pretitle = models.CharField(max_length=100, verbose_name='Ön başlıq')
    title = models.CharField(max_length=200, verbose_name='Başlıq')
    video_source = models.URLField(verbose_name='Video mənbə kodu')
    image = models.ImageField(upload_to='video_section_image', verbose_name='Video cover')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[SmartResize(400, 400)],
                                     format='JPEG',
                                     options={'quality': 90})

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Delete the image file from disk when the model is deleted
        self.image.delete()
        super().delete(*args, **kwargs)

    def get_image(self):
        return get_image_html(self.image.url if self.image else None, self.title)

    def save(self, *args, **kwargs):
        if not self.id and not self.image_thumbnail:
            self.image = optimise_image(self.image)
        super().save(*args, **kwargs)


class WelcomeSection(MyModel):
    pretitle = models.CharField(max_length=100, verbose_name='Ön başlıq')
    title = models.CharField(max_length=200, verbose_name='Başlıq')
    description = models.TextField(verbose_name='Açıqlama')
    button_text = models.CharField(max_length=100, verbose_name='Düymə mətni')
    button_url = models.URLField(verbose_name='Düymə url-i')
    image = models.ImageField(upload_to='welcome_section_images', verbose_name='Image')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[SmartResize(400, 400)],
                                     format='JPEG',
                                     options={'quality': 90})

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Delete the image file from disk when the model is deleted
        self.image.delete()
        super().delete(*args, **kwargs)

    def get_image(self):
        return get_image_html(self.image.url if self.image else None, self.title)

    def save(self, *args, **kwargs):
        if not self.id and not self.image_thumbnail:
            self.image = optimise_image(self.image)
        super().save(*args, **kwargs)
