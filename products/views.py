import math

from django.views     import View
from django.http      import JsonResponse
from django.db.models import F, Q, Avg

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
 
class ProductList(View):
    def get(self, request):
        sort     = request.GET.get('sort', 'id')
        day      = request.GET.get('day')
        taste    = request.GET.get('taste')
        page     = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 20))
        
        products = Product.objects.annotate(
            rating=Avg('review__star_rating'), day=F('dayproduct__day'), taste=F('tasteproduct__taste')).filter(
                Q(day=day)|Q(taste=taste)).order_by(sort)
        
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
            'title'     : product.title,
            'sub_title' : product.sub_title,
            'price'     : product.price,
            'calorie'   : product.calorie,
            'gram'      : product.gram,
            'taste'     : [taste.taste.name for taste in product.tasteproduct_set.all()],
            'images'    : '' if product.productimage_set.all().first() == None else product.productimage_set.all().first().image_url
        } for product in products]

        return JsonResponse(result, status=200)