from django.urls import path
from . import views
urlpatterns = [
    path("/<int:stock_id>/cart", views.CartListView.as_view()),
    path("/cart/<int:pk>", views.CartDeleteView.as_view()),
    path("/cart", views.CartCreateView.as_view()),
    path("/<int:pk>", views.StockDetailView.as_view()),
    path("/", views.StockListView.as_view()),
    path("/balance", views.BalanceListView.as_view())
]