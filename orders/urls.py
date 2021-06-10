from django.urls import path
from.views       import OrderitemView


urlpatterns = [
    path('/cart',OrderitemView.as_view()),
]