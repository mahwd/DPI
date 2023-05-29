from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from mail.forms import MailForm
from .forms import ContactForm
from .models import ContactInfo, SocialMediaIcon, Category, Project, TeamMember, ContactUsPageData
from home.models import MenuItems, Carousel, InfoTag, \
    ServiceIcon, MiniSwipe, SectionInfo, ServicePlan, Brand
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.core import serializers


class BaseContext(View):
    def get_context_data(self, **kwargs):
        context = super(BaseContext, self).get_context_data(**kwargs)
        context["header_menu"] = MenuItems.objects.filter(parent__isnull=True)
        context["contact_info"] = ContactInfo.objects.last()
        context["socials"] = SocialMediaIcon.objects.all()

        context["categories"] = Category.objects.filter(active=True)
        context["projects"] = Project.objects.filter(active=True)
        context["service_plans"] = ServicePlan.objects.filter(active=True)
        context["team"] = TeamMember.objects.filter(active=True)

        return context


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


class AboutUsView(BaseContext, TemplateView):
    template_name = 'pages/aboutus.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        page = ContactUsPageData.objects.filter(active=True).last()
        context["page"] = page or None
        context["accordion_items"] = page.accordion_items.all() if page else []
        context["swipers"] = page.swipers.all() if page else []
        context["brands"] = Brand.objects.filter(active=True).order_by("-sort_order")
        context["breadcrumps"] = [
            {"text": "Ana səhifə", "url": "/"},
            {"text": "Haqqımızda", "url": "#"},
        ]
        return context


class ContactUsView(BaseContext, TemplateView):
    template_name = 'pages/contact.html'


class ContactFormView(BaseContext, FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
