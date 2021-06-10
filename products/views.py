from django.views import View
from django.http  import JsonResponse

from .models import Product
from .star_rates import star_rates

class ProductDetailView(View):

    def get(self, request, product_title):
            
        order = request.GET.get('sort')

        product = Product.objects.get(title=product_title)
        
        tastes       = product.tasteproduct_set.all()
        images       = product.productimage_set.all()
        descriptions = product.description_set.all()
        
        if order == None:
            reviews = product.review_set.all()
        else:
            reviews = product.review_set.order_by(order) # -star_rating, -created_at
 
        product_info = {
            'title'            : product.title,
            'sub_title'        : product.sub_title,
            'price'            : product.price,
            'gram'             : product.gram,
            'calorie'          : product.calorie,
            'detail_image'     : [image.image_url for image in images],
            'taste'            : [taste.taste.taste for taste in tastes],
            'description_info' : [{
                                    'detail'      : description.detail,
                                    'information' : description.information,
                                    'delivery'    : description.delivery,
                                    'refund'      : description.refund
                                } for description in descriptions],
            'review_info'      : [{
                                'user'         : review.user.name,
                                'review_image' : review.image_url,
                                'content'      : review.content,
                                'created_at'   : review.created_at,
                                'star_rating'  : review.star_rating
                                } for review in reviews]
        }

        return JsonResponse({'detail_result' : product_info, 'detail_rate' : star_rates(product_title)}, status=200)