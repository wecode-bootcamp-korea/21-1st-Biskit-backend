import json

from djnago.views import View
from django.http  import JsonResponse

from .models      import DeliveryDate, Order, OrderItem, Status

class CartView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        product = data['product_id']
        quantity = data['quantity']
        total_price = data['total_price']
        date = data['date']

        zzz = Order.objects.create(
            user = user,
            status = Status.objects.get(id=1)
        )

        hhh = OrderItem.objects.create(
            product = product,
            quantity = quantity,
            total_price = total_price,
            order = zzz
        )
        
        DeliveryDate.objects.create(
            date = date,
            order_item = hhh
        )

        return JsonResponse({'message' : 'SUCCESS'}, status=200)