from products.models import Review
from django.urls import path

from .views      import ProductDetailView, ProductReviewVeiw

urlpatterns = [
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/review', ProductReviewVeiw.as_view())
]