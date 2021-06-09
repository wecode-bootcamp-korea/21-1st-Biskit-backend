from django.urls import path

from .views import ProductDetailView

urlpatterns = [
    path('/<str:product_title>/detail', ProductDetailView.as_view())
]