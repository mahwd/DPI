from .models import Mail
from django import forms
import datetime


class MailForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Adınız", "id": "name"}))
    email = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Elektron poçt ünvanınız", "id": "email"}))
    message = forms.CharField(label='',
                              widget=forms.Textarea(attrs={"placeholder": "Mesajınız", "id": "message"}))

    # email_to = forms.CharField(label='', widget=forms.TextInput(attrs={"type": "hidden"}))

    # def __init__(self, *args, **kwargs):
    #     super(MailForm, self).__init__(*args, **kwargs)
    #
    #     for name in self.fields.keys():
    #         self.fields[name].widget.attrs.update({
    #             'id': name,
    #             'placeholder': self.fields[name].label
    #         })

    class Meta:
        model = Mail
        fields = ["name", "email", "message", "email_to"]
