import json

from django.views import View
from django.http  import JsonResponse

from .models import Product 

class ProductDetailView(View):

    def get(self, request):

            product = Product.objects.get(id=1)
            
            reviews      = product.review_set.all()
            tastes       = product.tasteproduct_set.all()
            images       = product.productimage_set.all()
            descriptions = product.description_set.all()
            
            detail_image_list = []
            taste_list        = []
            review_list       = []

            for image in images:
                detail_image_list.append(image.image_url)

            for taste in tastes:
                taste_list.append(taste.taste.taste)

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

            for review in reviews:
                
                review_info = {
                    'user'         : review.user.name,
                    'review_image' : review.image_url,
                    'content'      : review.content,
                    'created_at'   : review.created_at,
                    'star_rating'  : review.star_rating
                }

                review_list.append(review_info)

            return JsonResponse({'detail_result' : product_info, 'description_result' : description_info, 'review_detail' : review_list, 'message' : 'SUCCESS'}, status=200)
