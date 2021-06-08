from django.urls import path

from .views import ProductDetailDescriptionView, ProductDetailView

urlpatterns = [
    path('/detail', ProductDetailView.as_view()),
    path('/description', ProductDetailDescriptionView.as_view())
]