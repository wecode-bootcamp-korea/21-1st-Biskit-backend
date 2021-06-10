from django.urls import path

from products.views import ProductList
urlpatterns = [
    path('/products', ProductList.as_view())
]