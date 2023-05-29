from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView
from core.views import BaseContext
from mail.forms import MailForm
from .models import Carousel, SectionInfo, Brand, ServiceIcon, MiniSwipe


class HomeView(BaseContext, FormView):
    template_name = 'home/index.html'
    form_class = MailForm

    @csrf_exempt
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context["carousels"] = Carousel.objects.all()
        context["brands"] = Brand.objects.filter(active=True).order_by("-sort_order")
        context["services"] = ServiceIcon.objects.filter(type__regex='mini')
        context["info_services"] = ServiceIcon.objects.filter(type__regex='middle')
        context["swipes"] = MiniSwipe.objects.filter(active=True)

        # - Sections
        context["welcome_section"] = SectionInfo.objects.filter(section__regex='welcome').last()
        context["video_section"] = SectionInfo.objects.filter(section__regex='video').last()
        context["service_section"] = SectionInfo.objects.filter(section__regex='service').last()
        context["info_section"] = SectionInfo.objects.filter(section__regex='info').last()
        context["testimonials_section"] = SectionInfo.objects.filter(section__regex='testimonials').last()
        context["projects_section"] = SectionInfo.objects.filter(section__regex='projects').last()
        context["ourteam_section"] = SectionInfo.objects.filter(section__regex='team').last()
        context["special_offer_section"] = SectionInfo.objects.filter(section__regex='special_offer').last()
        # = # Sections
        context['form'] = MailForm()

        return context

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        form = MailForm(request.POST)
        self.object = self.get_object()
        context = self.get_context_data(**kwargs)
        if form.is_valid():
            instance = form.save()
            mail_json = serializers.serialize('json', [instance, ])
            context["mailJson"] = mail_json
            print(mail_json)
            return self.render_to_response(context=context, status=200)
        else:
            # some form errors occured.
            return self.render_to_response(context=context, status=400)
