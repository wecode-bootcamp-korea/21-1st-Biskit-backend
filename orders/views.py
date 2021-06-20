import json

from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction
from django.db.models import F, Q
from json.decoder     import JSONDecodeError

from .models         import DeliveryDate, Order, OrderItem, Status
from users.models    import User 
from products.models import Product
from users.decorator import login_decorator

class CartView(View):
    @login_decorator
    def post(self, request):
        data        = json.loads(request.body)
        date        = data.get('date', '')
        product     = Product.objects.get(id=data['product_id'])
        quantity    = int(data.get('quantity', 1))
        total_price = int(data.get('total_price'))
        user   = User.objects.get(id=request.user.id)
        status = Status.objects.get(id=1)
        
        if OrderItem.objects.filter(Q(order__status=status)&Q(order__user=user)&Q(product_id=product.id)).exists():
            user_cart = OrderItem.objects.filter(order__status=status, order__user=user, product_id=product)
            for cart in user_cart:
                cart.quantity = quantity
                cart.total_price = total_price
                cart.save()
            return JsonResponse({"message" : "SUCCESS"}, status=200)

        with transaction.atomic():
            order = Order.objects.create(
                user   = request.user,
                status = Status.objects.get(id=1)
                )
            order_item = OrderItem.objects.create(
                quantity    = quantity,
                total_price = total_price,
                product     = product,
                order       = order
                )
            DeliveryDate.objects.create(
                date       = date,
                order_item = order_item
                )

        return JsonResponse({"message" : "SUCCESS"},status=201)

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
            'date'          : None if cart.deliverydate_set.first() is None else cart.deliverydate_set.first().date,
            'product_id'    : cart.product.id
        } for cart in carts]

        return JsonResponse({'result' : cart_info}, status=200)

# class CartDeleteView(View):
#     @login_decorator
#     def delete(self, request, product_id):
#         user    = request.user
#         product = Product.objects.get(id=product_id)

#         Order.objects.filter(user=user, orderitem__product=product).delete()

#         return JsonResponse({'message' : 'SUCCESS'}, status=200)


class CartDeleteView(View):
    @login_decorator
    def post(self, request):
        # try:
        user     = request.user
        data     = json.loads(request.body)
        selected = data.get('selecteditemid')
        
        for product_id in selected:
            product = Product.objects.get(id=product_id)
            Order.objects.filter(user=user, orderitem__product_id=product.id).delete()
        
        return JsonResponse({'message' : 'SUCCESS'}, status=200)
        # except JSONDecodeError:
        #     return JsonResponse({'message' : '안와요ㅜㅜ'}, status=400)


'''
class CartDeleteView(View):
    @login_decorator
    def post(self, request):
        user    = request.user
        data = json.loads(request.body) 

        if type(data) == int:
            product = Product.objects.get(id=data)
            Order.objects.filter(user=user, orderitem__product_id=product.id).delete()
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        
        for product_id in data:
            product = Product.objects.filter(id=product_id)
                if len(product) != 0:
                    Order.objects.filter(user=user, orderitem__product_id=product[0].id).delete()
        
        return JsonResponse({'message' : 'SUCCESS'}, status=200)
'''