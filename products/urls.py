from django.urls import path

from products.views import ProductList, ProductDetailView
urlpatterns = [
    path('/products', ProductList.as_view()),
    path('/<str:product_title>', ProductDetailView.as_view())
]