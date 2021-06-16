import json

from django.views     import View
from django.http      import JsonResponse, request
from django.db.models import Q
from django.db        import transaction 

from .models          import Status, Order, OrderItem, DeliveryDate
from users.models     import User 
from users.decorators import login_decorator
from products.models  import Product

class OrderitemView(View):
    @login_decorator
    def post(self,request):
        data        = json.loads(request.body)
        date        = data['date']
        product     = Product.objects.get(id=data['id'])
        quantity    = int(data['qunantity'])
        total_price = int(data['total_price'])

        user   = User.objects.get(id=request.user.id)
        status = Status.objects.get(id=1)
        
        if OrderItem.objects.filter(Q(order__status=status)&Q(order__user=user)&Q(product_id=product.id)).exists():
            user_cart = OrderItem.objects.filter(order__status=status, order__user=user, product_id=product)
            for cart in user_cart:
                cart.quantity += quantity
                cart.save()
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=200)
    
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
    
        delivey = DeliveryDate.objects.create(
            date       = date,
            order_item = order_item
            )
        with transaction.transaction.atomic():
            order.save()
            order_item.save()
            delivey.save()

        return JsonResponse({"MESSAGE":"SUCCESS"},status=201)
        
        
        





    
    # @login_decorator 
    # def get(self,request):
    #        cart_list=OrderItem.objects.filter(user_id=request.user.id)
    #        reslut=[]
    #        for usercart in cart_list:
    #            image_url=[]
    #            image =usercart.product.productimage_set.all()
    #            for url in image:
    #                img_info={
    #                'img':url.image_url}     
    #                image_url.append(img_info)
    #            info={
    #                'title':usercart.product.title,
    #                'price':usercart.product.price,
    #                'image':image_url
    #            }
    #            reslut.append(info)
 
    #        return JsonResponse({'message':reslut},status=200)