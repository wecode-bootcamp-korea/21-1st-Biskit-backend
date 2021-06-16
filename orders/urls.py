from django.urls import path
<<<<<<< HEAD

from .views     import CartDeleteView, CartView

urlpatterns = [
    path('', CartView.as_view()),
    path('/<int:product_id>', CartDeleteView.as_view())
=======
from .views      import OrderitemView

urlpatterns = [
    path('/cart',OrderitemView.as_view()),
>>>>>>> main
]