from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from mail.forms import MailForm
from django.http import JsonResponse


# Create your views here.

@csrf_exempt
def send_mail(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            instance = form.save()
            mail_json = serializers.serialize('json', [instance, ])
            print(mail_json)
            return JsonResponse({"instance": mail_json}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
