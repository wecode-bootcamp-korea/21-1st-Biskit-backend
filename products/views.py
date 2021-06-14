import math

from django.views     import View
from django.http      import JsonResponse
from django.db.models import F, Avg, Count

from products.models  import Product

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

        review_info.append(product.review_set.aggregate(avg=Avg('star_rating'),count=Count('star_rating')))

        return JsonResponse({'result' : review_info}, status=200)
         
class ProductList(View):
    def get(self, request):
        sort     = request.GET.get('sort', 'id')
        day      = request.GET.get('day')
        taste    = request.GET.get('taste')
        page     = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 20))
        
        products = Product.objects.annotate(
            rating=Avg('review__star_rating'), day=F('dayproduct__day'), taste=F('tasteproduct__taste')).order_by(sort)

        if day != None:
            products = products.filter(day=day).order_by(sort)
        if taste != None:
            products = products.filter(taste=taste).order_by(sort)
        
        objects_count = products.count()
        
        if page > 0 and per_page > 0:
            started  = (page - 1) * per_page
            ended    = started + per_page
            products = products[started:ended]

        result = {
            'count'    : objects_count,
            'page'     : page,
            'per_page' : per_page,
            'pages'    : math.ceil(objects_count/per_page),
            'elements' : products.count()
        }
        
        result['result'] = [{
            'id'        : product.id,
            'title'     : product.title,
            'sub_title' : product.sub_title,
            'price'     : product.price,
            'calorie'   : product.calorie,
            'gram'      : product.gram,
            'taste'     : [taste.taste.name for taste in product.tasteproduct_set.all()],
            'images'    : '' if product.productimage_set.all().first() == None else product.productimage_set.all().first().image_url
        } for product in products]

        return JsonResponse(result, status=200)