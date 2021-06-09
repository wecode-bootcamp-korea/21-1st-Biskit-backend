import json

from django.views import View
from django.http  import JsonResponse

from .models import Product 

class ProductDetailView(View):

    def get(self, request, product_title):

            product = Product.objects.get(title=product_title)
            
            tastes       = product.tasteproduct_set.all()
            images       = product.productimage_set.all()
            descriptions = product.description_set.all()
    
            product_info     = {}
            description_info = {}
            
            detail_image_list = [image.image_url for image in images]

            taste_list        = [taste.taste.taste for taste in tastes]

            product_info = {
                'title'        : product.title,
                'sub_title'    : product.sub_title,
                'price'        : product.price,
                'gram'         : product.gram,
                'calorie'      : product.calorie,
                'detail_image' : detail_image_list,
                'taste'        : taste_list
            }

            for description in descriptions:
                
                description_info = {
                    'detail'      : description.detail,
                    'information' : description.information,
                    'delivery'    : description.delivery,
                    'refund'      : description.refund
                }

            return JsonResponse({'detail_result' : product_info, 'description_result' : description_info, 'message' : 'SUCCESS'}, status=200)
