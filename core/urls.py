from django.urls import path

from core.views import HomeView, PortfolioView, PortfolioDetailView

urlpatterns = [
    path('', HomeView.as_view()),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<slug:slug>', PortfolioDetailView.as_view(), name='portfolio_detail'),
]
