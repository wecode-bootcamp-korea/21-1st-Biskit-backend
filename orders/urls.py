from django.urls import path

from .views     import CartDeleteView, CartView, DeleteView

urlpatterns = [
    path('', CartView.as_view()),
    path('/delete', DeleteView.as_view()),
    path('/<int:product_id>', CartDeleteView.as_view())
]