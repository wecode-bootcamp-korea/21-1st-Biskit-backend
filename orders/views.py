import json

from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction
from django.db.models import F

from .models         import DeliveryDate, Order, OrderItem, Status
from products.models import Product
from users.decorator import login_decorator

class CartView(View):
    @login_decorator
    def get(self, request):
        user  = request.user
        carts = OrderItem.objects.filter(order__user=user).annotate(date=F('deliverydate__date')).order_by('date')
        
        cart_info = [{
            'product_title' : cart.product.title,
            'product_image' : cart.product.productimage_set.first().image_url,
            'product_price' : cart.product.price,
            'quantity'      : cart.quantity,
            'total_price'   : cart.total_price,
            'date'          : cart.deliverydate_set.first().date
        } for cart in carts]

        return JsonResponse({'result' : cart_info}, status=200)

class CartDeleteView(View):
    @login_decorator
    def delete(self, request, product_id):
        user    = request.user
        product = Product.objects.get(id=product_id)

        Order.objects.filter(user=user, orderitem__product=product).delete()

        return JsonResponse({'message' : 'SUCCESS'}, status=200)


        
