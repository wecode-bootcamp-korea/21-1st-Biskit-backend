# import json

# from django.views import View
# from django.http  import JsonResponse

# from users.decorators import login_decorator
# from .models import Order, OrderItem

# class CartView(View):
#     @login_decorator
#     def post(self, request):
#         data = json.loads(request.body)
#         user = request.user

#         cart = Order.objects.get()