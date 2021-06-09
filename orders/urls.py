from django.urls import path
from.views       import OrderitemView


urlpatterns = [
    path('/ordersitem',OrderitemView.as_view()),
]