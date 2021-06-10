from django.views import View
from django.http  import JsonResponse

from .models     import Product
from .star_rates import star_rates

class ProductDetailView(View):
    def get(self, request, product_title):
        product = Product.objects.get(title=product_title)
        
        tastes       = product.tasteproduct_set.all()
        images       = product.productimage_set.all()
        descriptions = product.description_set.all()
        
        product_info = {
            'title'            : product.title,
            'sub_title'        : product.sub_title,
            'price'            : product.price,
            'gram'             : product.gram,
            'calorie'          : product.calorie,
            'detail_image'     : [image.image_url for image in images],
            'taste'            : [taste.taste.name for taste in tastes],
            'description_info' : [{
                                    'detail'      : description.detail,
                                    'information' : description.information,
                                    'delivery'    : description.delivery,
                                    'refund'      : description.refund
                                } for description in descriptions]
        }

        return JsonResponse({'result' : product_info}, status=200)

class ProductReviewVeiw(View):
    def get(self, request, product_title):
        order = request.GET.get('sort')

        product = Product.objects.get(title=product_title)

        if order == None:
            reviews = product.review_set.all()
        else:
            reviews = product.review_set.order_by(order) # -star_rating-별점높은순, -created_at-최신순

        review_info = [{'user'         : review.user.name,
                        'review_image' : review.image_url,
                        'content'      : review.content,
                        'created_at'   : review.created_at,
                        'star_rating'  : review.star_rating
                        } for review in reviews]

        return JsonResponse({'result' : review_info, 'rates' : star_rates(product_title)}, status=200)