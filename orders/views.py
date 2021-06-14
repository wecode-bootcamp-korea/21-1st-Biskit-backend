import json

from django.views     import View
from django.http      import JsonResponse, request
from django.db        import transaction
from django.db.models import F


from .models          import Status, Order, OrderItem
from users.decorators import login_decorator
from products.models  import Product, ProductImage



class OrderitemView(View):
    @login_decorator
    def post(self,request):
        try:
            data      = json.loads(request.body)
            user      = request.user
            product   = Product.objects.get(title=data['title'])
            product   = Product.objects.get(price=data['price'])
            status    = Status.objects.get(status=data['status'])
            quantity  = int(data['quantity'])

            order = Order.objects.create(
                product = product,
                status  = status,
            )
            OrderItem.objects.create(
                product     = product,
                total_price = quantity*product.price,
                user        = user,
                order       = order
            )
            
            return JsonResponse({'message':'SUCCESS'},status=201)
        except KeyError:
            return JsonResponse ({'message':'KEY_ERROR'},status=400)
    
    @login_decorator 
    def get(self,request):
        try:
           cart_list=OrderItem.objects.all()
           reslut=[]
           for usercart in cart_list:
               image =ProductImage.objects.filter(product_id=usercart.product.id)
               for url in image:
                   image=[ ]
                   img_info={
                   'img':url.image_url}
                   image.append(img_info)
               info={
                   'title':usercart.product.title,
                   'price':usercart.product.price,
                   'total_price':usercart.total_price,
                   'image':image
               }
               reslut.append(info)
 
           return JsonResponse({'message':reslut},status=200)

        except AttributeError:
            return JsonResponse({'message':'SEVER ERROR'},status=500)

    


        

        


        

   