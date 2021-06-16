from django.urls import path

from products.views import ProductList, ProductDetailView, ProductReviewVeiw

urlpatterns = [
    path('', ProductList.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/review', ProductReviewVeiw.as_view())
]