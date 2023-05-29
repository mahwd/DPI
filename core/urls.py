from django.urls import path
from core.views import PortfolioView, PortfolioDetailView, TeamView, TeamDetailView, AboutUsView, ContactFormView

urlpatterns = [
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<slug:slug>', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('team/', TeamView.as_view(), name='team'),
    path('team/<slug:slug>', TeamDetailView.as_view(), name='team_detail'),
    path('about/', AboutUsView.as_view(), name="about"),
    path('contact/', ContactFormView.as_view(), name="contact"),
]
