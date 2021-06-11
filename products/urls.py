from products.models import Review
from django.urls import path

from .views      import ProductDetailView, ProductReviewVeiw

urlpatterns = [
    path('/<str:product_title>', ProductDetailView.as_view()),
    path('/<str:product_title>/review', ProductReviewVeiw.as_view())
]