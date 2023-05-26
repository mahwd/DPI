from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView, ListView, DetailView
from mail.forms import MailForm
from .models import ContactInfo, SocialMediaIcon, Brand, Category, Project, TeamMember
from home.models import MenuItems, Carousel, InfoTag, \
    ServiceIcon, MiniSwipe, SectionInfo, ServicePlan
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.core import serializers


class BaseContext(View):
    def get_context_data(self, **kwargs):
        context = super(BaseContext, self).get_context_data(**kwargs)
        context["header_menu"] = MenuItems.objects.filter(parent__isnull=True)
        context["contact_info"] = ContactInfo.objects.last()
        context["socials"] = SocialMediaIcon.objects.all()
        context["carousels"] = Carousel.objects.all()
        context["brands"] = Brand.objects.all()
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
        context["services"] = ServiceIcon.objects.filter(type__regex='mini')
        context["info_services"] = ServiceIcon.objects.filter(type__regex='middle')
        context["tags"] = InfoTag.objects.filter(active=True)
        context["swipes"] = MiniSwipe.objects.filter(active=True)
        context["categories"] = Category.objects.filter(active=True)
        context["projects"] = Project.objects.filter(active=True)
        context["service_plans"] = ServicePlan.objects.filter(active=True)
        context["team"] = TeamMember.objects.filter(active=True)

        return context


class HomeView(BaseContext, TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        return super(HomeView, self).get_context_data(**kwargs)


class PortfolioView(BaseContext, ListView):
    template_name = 'portfolio/portfolio.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        try:
            cat = Category.objects.get(slug__exact=self.request.GET.get("category"))
            context["project_list"] = Project.objects.filter(category__slug=cat.slug)
            context["breadcrumps"] = [
                {"text": "Ana səhifə", "url": "/"},
                {"text": "Bütün proyektlər", "url": "/portfolio/"},
                {"text": cat.title, "url": ""}
            ]

        except:
            context["breadcrumps"] = [
                {"text": "Ana səhifə", "url": "/"},
                {"text": "Bütün proyektlər", "url": "#"}
            ]

        return context


class PortfolioDetailView(BaseContext, DetailView):
    template_name = 'portfolio/portfolio_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)
        try:
            category = kwargs.get('object').category
            breadcrumps = [
                {"text": "Ana səhifə", "url": "/"},
                {"text": "Bütün proyektlər", "url": f"/portfolio/"},
                {"text": category.title, "url": f"/portfolio/?category={category.slug}"}
            ]
            context["breadcrumps"] = breadcrumps
            return context
        except:
            return super(PortfolioDetailView, self).get_context_data(**kwargs)


class TeamView(BaseContext, ListView):
    template_name = 'team/team.html'
    model = TeamMember

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)
        context["breadcrumps"] = [
            {"text": "Ana səhifə", "url": "/"},
            {"text": "Komanda üzvləri", "url": "#"}
        ]
        return context


class TeamDetailView(BaseContext, DetailView):
    template_name = 'team/team_detail.html'
    model = TeamMember

    @csrf_exempt
    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['form'] = MailForm()
        member = self.get_object()
        context["breadcrumps"] = [
            {"text": "Ana səhifə", "url": "/"},
            {"text": "Bütün komanda üzvləri", "url": "/team/"},
            {"text": member.fullname, "url": ""}
        ]
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
