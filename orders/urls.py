from django.urls import path

from .views     import CartDeleteView, CartView

urlpatterns = [
    path('', CartView.as_view()),
    path('/delete', CartDeleteView.as_view())
]