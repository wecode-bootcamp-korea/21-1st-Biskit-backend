import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from users.models    import User
from products.models import Product, ProductImage

from .models         import Status, Order, OrderItem

class OrderitemView(View):
    def post(self,request):
        try:
            data      = json.loads(request.body)
            product = Product.objects.get(title=data['title'])
            user      = User.objects.get(name = data['name'])
            status    = Status.objects.get(status=data['status'])
            quantity  = int(data['quantity'])
            img       = ProductImage.objects.get(id = product.id)
            
            if  quantity > product.stock:
                return JsonResponse({'경고':'최대수량{0}넘기셨습니다.'.format(quantity)},status=400)

            order = Order.objects.create(
                product = product,
                status  = status,
            )
           
            OrderItem.objects.create(
                product     = img.Product.title,
                total_price = quantity*product.price,
                user        = user,
                order       = order
            )

            return JsonResponse({'message':'SUCCESS'},status=201)
                
        except KeyError:
            return JsonResponse ({'message':'KEY_ERROR'},status=400)