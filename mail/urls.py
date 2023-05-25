from django.urls import path
from .views import send_mail

urlpatterns = [
    path('sendmail/', send_mail, name="sendmail")
]
