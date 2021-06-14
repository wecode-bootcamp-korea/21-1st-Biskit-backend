from django.views          import View
from django.http           import JsonResponse
from django.db.models      import Avg, Count

from .models               import Product

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
        order   = request.GET.get('sort')
        page    = int(request.GET.get('page', 1))
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

        product_rate = product.review_set.aggregate(avg=Avg('star_rating'),count=Count('star_rating'))

        PAGE_SIZE = 10
        limit     = PAGE_SIZE * page
        offset    = limit - PAGE_SIZE

        if review_info[offset:limit] == []:
            return JsonResponse({'result' : review_info[0:9], 'product_rate' : product_rate}, status=200)

        return JsonResponse({'result' : review_info[offset:limit-1], 'product_rate' : product_rate}, status=200)