import json

from django.views     import View
from django.http      import JsonResponse, request
from django.db        import transaction

from .models          import Status, Order, OrderItem
from users.decorators import login_decorator
from products.models  import Product



class OrderitemView(View):
    @login_decorator
    def post(self,request):
        try:
            data      = json.loads(request.body)
            user      = request.user
            product   = Product.objects.get(title=data['title'])
            status    = Status.objects.get(status=data['status'])
            quantity  = int(data['quantity'])
            total_price = int(data['total'])

            if  quantity > product.stock:
                return JsonResponse({'message':'The maximum quantity is {}.'.format(product.stock)},status=400)

            order = Order.objects.create(
                product = product,
                status  = status,
            )
            OrderItem.objects.create(
                product     = product,
                total_price = total_price,
                user        = user,
                order       = order
            )
            
            return JsonResponse({'message':'SUCCESS'},status=201)
        except KeyError:
            return JsonResponse ({'message':'KEY_ERROR'},status=400)
    
    @login_decorator 
    def get(self,request):
           cart_list=OrderItem.objects.filter(user_id=request.user.id)
           reslut=[]
           for usercart in cart_list:
               image_url=[]
               image =usercart.product.productimage_set.all()
               for url in image:
                   img_info={
                   'img':url.image_url}     
                   image_url.append(img_info)
               info={
                   'title':usercart.product.title,
                   'price':usercart.product.price,
                   'image':image_url
               }
               reslut.append(info)
 
           return JsonResponse({'message':reslut},status=200)