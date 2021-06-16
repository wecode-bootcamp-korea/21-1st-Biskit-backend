from django.urls import path

from .views     import CartDeleteView, CartView

urlpatterns = [
    path('', CartView.as_view()),
    path('/<int:product_id>', CartDeleteView.as_view())
]