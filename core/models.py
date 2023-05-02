from django.db import models


class MyModel(models.Model):

    @classmethod
    def get_fields(cls, fields: tuple):
        return fields.__add__(('created_at', 'updated_at'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="yaradılma tarixi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="dəyişdirilmə tarixi")

    class Meta:
        abstract = True


1


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
