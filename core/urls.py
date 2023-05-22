from django.urls import path

from core.views import HomeView, PortfolioView, PortfolioDetailView, TeamView, TeamDetailView

urlpatterns = [
    path('', HomeView.as_view()),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<slug:slug>', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('team/', TeamView.as_view(), name='team'),
    path('team/<slug:slug>', TeamDetailView.as_view(), name='team_detail'),
]
