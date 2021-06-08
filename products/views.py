import json

from django.views import View
from django.http  import JsonResponse

from .models import Product

class ProductDetailView(View):

    def get(self, request):

            products  = Product.objects.all()
            
            product_detail_list = []
            
            for product in products:
                images            = product.productimage_set.all()
                detail_image_list = []

                for image in images:
                    detail_image_list.append(image.image_url)

                product_info = {
                    'title' : product.title,
                    'sub_title' : product.sub_title,
                    'price' : product.price,
                    'gram' : product.gram,
                    'calorie' : product.calorie,
                    'detail_image' : detail_image_list
                }

                product_detail_list.append(product_info)

            return JsonResponse({'result' : product_detail_list, 'message' : 'SUCCESS'}, status=200)

            

            
class ProductDetailDescriptionView(View):

    def get(self, request):

            products = Product.objects.all()
            
            description_list = []
            
            for product in products:
                descriptions = product.description_set.all()

                for description in descriptions:
                    
                    description_info = {
                        'detail' : description.detail,
                        'information' : description.information,
                        'delivery' : description.delivery,
                        'refund' : description.refund
                    }

                    description_list.append(description_info)
            
            return JsonResponse({'result' : description_list, 'message' : 'SUCCESS'}, status=200)

