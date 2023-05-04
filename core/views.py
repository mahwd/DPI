from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import MenuBaseItems, ContactInfo, SocialMediaIcon, Carousel, Brand, WelcomeSection


class BaseContext(View):
    def get_context_data(self, **kwargs):
        context = super(BaseContext, self).get_context_data(**kwargs)
        context["header_menu"] = MenuBaseItems.objects.all()
        context["contact_info"] = ContactInfo.objects.last()
        context["socials"] = SocialMediaIcon.objects.all()
        context["carousels"] = Carousel.objects.all()
        context["brands"] = Brand.objects.all()
        context["welcome_section"] = WelcomeSection.objects.all()
        return context


class HomeView(BaseContext, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return super(HomeView, self).get_context_data(**kwargs)
