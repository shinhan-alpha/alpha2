from django.urls import path
from . import views
urlpatterns = [
    path("/", views.PortfolioDetailView.as_view()),
    # path("/", views.PortfolioListView.as_view()),
]