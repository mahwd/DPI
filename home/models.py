from django.db import models
from core.models import MyModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize
from core.custom.custom_tools import get_image_html


class MenuItems(MyModel):
    title = models.CharField(max_length=128, verbose_name="Menu title")
    url = models.CharField(default="", max_length=255, null=True, blank=True, verbose_name="Redirect url")
    sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Parent menu",
    )

    class Meta:
        ordering = ['sort_order']
        verbose_name = "Header menu linki"
        verbose_name_plural = "Header menu linkləri"

    def __str__(self):
        return self.title

    # return true if has child sub-menus
    def contain_dropdown(self):
        child_count = MenuItems.objects.filter(parent_id=self.id).count()
        return True if child_count > 0 else False

    def get_children(self):
        return MenuItems.objects.filter(parent_id=self.id)

    def save(self, *args, **kwargs):
        if self.sort_order is None:
            try:
                last_item = type(self).objects.filter(sort_order__isnull=False).order_by('-sort_order').first()
                if last_item:
                    self.sort_order = last_item.sort_order + 1
            except type(self).DoesNotExist:
                pass

        super().save(*args, **kwargs)


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
    left_button_url = models.CharField(max_length=128, verbose_name="Soldakı düymə url-i")
    right_button_text = models.CharField(max_length=50, verbose_name="Sağdakı düymə mətni")
    right_button_url = models.CharField(max_length=128, verbose_name="Sağdakı düymə url-i")
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


class InfoTag(MyModel):
    # type_options = [
    #     ("info", "Info tag"),
    #     ("skill_diagram", "Skill tag"),
    #     ("project_tag", "Project tag"),
    # ]
    # type = models.CharField(max_length=128, choices=type_options, verbose_name="Teq tipi")
    title = models.CharField(max_length=255, verbose_name="Teq")
    # Info section tag fields
    url = models.CharField(max_length=255, verbose_name="URL")  # null=True, blank=True,
    sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    # Skill diagram tag fields
    # percentage = fields.IntegerRangeField(min_value=1, max_value=100, verbose_name="Faiz")

    class Meta:
        verbose_name = "İnfo Teq"
        verbose_name_plural = "İnfo Teqlər"
        ordering = ['sort_order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.sort_order is None:
            try:
                last_item = type(self).objects.filter(sort_order__isnull=False).order_by('-sort_order').first()
                if last_item:
                    self.sort_order = last_item.sort_order + 1
            except type(self).DoesNotExist:
                pass
        super().save(*args, **kwargs)


class ServiceIcon(MyModel):
    service_types = [
        ("mini", "Kiçik"),
        ("middle", "Orta"),
    ]

    title = models.CharField(max_length=128, verbose_name="Servis adı")
    url = models.CharField(max_length=255, verbose_name="Servis URL-i")
    type = models.CharField(max_length=64, choices=service_types, verbose_name="Servis tipi")
    # optional fields
    icon = models.CharField(null=True, blank=True, max_length=128, verbose_name="Servis ikon klası")
    image = models.ImageField(null=True, blank=True, upload_to='section_images', verbose_name='Servis şəkli')
    description = models.TextField(null=True, blank=True, verbose_name='Servis açıqlaması')

    class Meta:
        verbose_name = "Servis ikonu"
        verbose_name_plural = "Servis ikonları"

    def __str__(self):
        return self.title

    def get_image(self):
        return get_image_html(self.image.url if self.image else None, self.title)


class MiniSwipe(MyModel):
    idiom = models.TextField(verbose_name='Mətn')
    author = models.CharField(max_length=100, verbose_name='Müəllif')
    author_profession = models.CharField(max_length=100, verbose_name='Vəzifə')
    author_image = models.ImageField(null=True, blank=True, upload_to='swiper_auther_images', verbose_name='Şəkil')

    # section_info = models.ForeignKey('SectionInfo', on_delete=models.CASCADE, related_name="swipers", verbose_name="Bölmə")

    class Meta:
        verbose_name = "Mini Swiper"
        verbose_name_plural = "Swipers"

    def __str__(self):
        return "%s - %s" % (self.author, self.idiom[50:])

    def get_image(self):
        return get_image_html(self.author_image.url if self.author_image else None, self.author)


class SectionInfo(MyModel):
    sections = [
        ('welcome', "Welcome section"),
        ('video', "Video section"),
        ('service', "Services section"),
        ('info', "Info section"),
        ('testimonials', "Testimonials section"),
        ('projects', "Projects section"),
        ('team', "Our team section"),
        ('special_offer', " Offer section"),
        # ('what-we-can-do', "What we can do section"),
        # ('faq', "FREQUENTLY ASKED"),
    ]

    # required fields
    section = models.CharField(choices=sections, max_length=255, verbose_name="Section seçin")

    # optional fields
    pretitle = models.CharField(null=True, blank=True, max_length=100, verbose_name='Ön başlıq')
    title = models.CharField(null=True, blank=True, max_length=200, verbose_name='Başlıq')
    description = models.TextField(null=True, blank=True, verbose_name='Açıqlama')
    button_text = models.CharField(null=True, blank=True, max_length=100, verbose_name='Düymə mətni')
    button_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='Düymə url-i')
    secondary_button_text = models.CharField(null=True, blank=True, max_length=100, verbose_name='Əlavə düymə mətni')
    secondary_button_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='Əlavə düymə url-i')
    video_source = models.TextField(null=True, blank=True, verbose_name='Video mənbə kodu')
    image = models.ImageField(null=True, blank=True, upload_to='section_images', verbose_name='Şəkil')
    image2 = models.ImageField(null=True, blank=True, upload_to='section_images', verbose_name='Əlavə şəkil ')

    class Meta:
        verbose_name = "Section Information"
        verbose_name_plural = "Section Information"

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Delete the image file from disk when the model is deleted
        self.image.delete() if self.image else None
        self.image2.delete() if self.image2 else None
        super().delete(*args, **kwargs)

    def get_image(self):
        return get_image_html(self.image.url if self.image else None, self.title)


class ServicePlan(MyModel):
    title = models.CharField(max_length=255, verbose_name='Planın adı')
    description = models.CharField(max_length=255, verbose_name='Planın açıqlaması')
    price = models.CharField(max_length=255, verbose_name='Planın qiyməti')
    currency = models.CharField(max_length=255, verbose_name='Plan qiymətinin valyutası')

    class Meta:
        verbose_name = "Servis paketi"
        verbose_name_plural = "Servis paketləri"

    def __str__(self):
        return self.title
