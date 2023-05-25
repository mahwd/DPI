from django.db import models
from django.core.mail import send_mail
from core.models import MyModel


class Mail(MyModel):
    name = models.CharField(max_length=100, verbose_name="Ad və soyad")
    email = models.CharField(max_length=100, verbose_name="Email")
    message = models.TextField(max_length=300, verbose_name="Mesaj mətni")
    email_sent = models.BooleanField(default=False, verbose_name="Is email sent?")
    email_to = models.EmailField(verbose_name="Email to")

    def save(self, *args, **kwargs):
        # send mail
        if not self.email_sent:
            try:
                is_sent = send_mail(
                    f"{self.name} sizinlə əlaqə saxlamaq istəyir.",
                    self.message,
                    "lazure.net@gmail.com",
                    [self.email_to],
                    fail_silently=False,
                )
                if is_sent == 1:
                    self.email_sent = True
                super(Mail, self).save(*args, **kwargs)
            except Exception:
                print(Exception)
        else:
            super(Mail, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
