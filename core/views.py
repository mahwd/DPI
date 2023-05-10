from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import MenuBaseItems, ContactInfo, SocialMediaIcon, Carousel, Brand, SectionInfo, ServiceIcon, Tag, \
    MiniSwipe


class BaseContext(View):
    def get_context_data(self, **kwargs):
        context = super(BaseContext, self).get_context_data(**kwargs)
        context["header_menu"] = MenuBaseItems.objects.all()
        context["contact_info"] = ContactInfo.objects.last()
        context["socials"] = SocialMediaIcon.objects.all()
        context["carousels"] = Carousel.objects.all()
        context["brands"] = Brand.objects.all()
        # - Sections
        context["welcome_section"] = SectionInfo.objects.get(section__regex='welcome')
        context["video_section"] = SectionInfo.objects.get(section__regex='video')
        context["service_section"] = SectionInfo.objects.get(section__regex='service')
        context["info_section"] = SectionInfo.objects.get(section__regex='info')
        context["testimonials_section"] = SectionInfo.objects.get(section__regex='testimonials')
        context["projects_section"] = SectionInfo.objects.get(section__regex='projects')
        # = # Sections
        context["services"] = ServiceIcon.objects.filter(type__regex='mini')
        context["info_services"] = ServiceIcon.objects.filter(type__regex='middle')
        context["tags"] = Tag.objects.filter(active=True)
        context["swipes"] = MiniSwipe.objects.filter(active=True)
        return context


class HomeView(BaseContext, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return super(HomeView, self).get_context_data(**kwargs)
