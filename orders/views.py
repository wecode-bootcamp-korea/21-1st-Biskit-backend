import json

from django.views    import View
from django.http     import JsonResponse
from django.db       import transaction

from .models         import DeliveryDate, Order, OrderItem, Status
from products.models import Product
from users.decorator import login_decorator

class CartView(View):
    @login_decorator
    def post(self, request):
        data          = json.loads(request.body)
        user          = request.user
        product       = data['product_id']
        quantity      = data['quantity']
        total_price   = data['total_price']
        date          = data['date']
        order_product = Product.objects.get(id=product)

        if Order.objects.filter(user=user, orderitem__product=product).exists():
            add_quantity = order_product.orderitem_set.get(product=product)
            add_quantity.quantity += quantity
            add_quantity.total_price += total_price
            add_quantity.save()

            return JsonResponse({'message' : 'SUCCESS'}, status=200)
    
        with transaction.atomic():
            order = Order.objects.create(
                user   = user,
                status = Status.objects.get(id=1)
            )
            order_item = OrderItem.objects.create(
                product     = Product.objects.get(id=product),
                quantity    = quantity,
                total_price = total_price,
                order       = order
            )
            DeliveryDate.objects.create(
                date       = date,
                order_item = order_item
            )

        return JsonResponse({'message' : 'SUCCESS'}, status=201)

    @login_decorator
    def get(self, request):
        user  = request.user
        carts = OrderItem.objects.filter(order__user=user)
        
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


        
