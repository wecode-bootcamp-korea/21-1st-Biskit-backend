import json

from django.views import View
from django.http  import JsonResponse

from users.models    import User
from products.models import Product
from .models         import Status, Order, OrderItem

class OrderitemView(View):
    def post(self,request):
        try:
            data      = json.loads(request.body)
            cart_plus = Product.objects.get(title=data['title'])
            user      = User.objects.get(name = data['name'])
            status    = Status.objects.get(status=data['status'])
            quantity  = data['quantity']

            order = Order.objects.create(
                product = cart_plus,
                status  = status
            )
            OrderItem.objects.create(
                product     = cart_plus,
                total_price = quantity*cart_plus.price,
                user        = user,
                order       = order
            )
            return JsonResponse({'메시지':'데이터가 성공적으로 이동했습니다.'},status=201)
             
        except KeyError:
            return JsonResponse ({'메시지':'테이터가 잘못되었습니다.'},status=400)