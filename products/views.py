import math

from django.views     import View
from django.http      import JsonResponse
from django.db.models import F, Avg, Count, Q

from products.models  import Product

class ProductDetailView(View):
    def get(self, request, product_id):
        product     = Product.objects.get(id=product_id)
        description = product.description_set.first()
        
        product_info = {
            'title'        : product.title,
            'sub_title'    : product.sub_title,
            'price'        : int(product.price),
            'gram'         : product.gram,
            'calorie'      : product.calorie,
            'detail_image' : [image.image_url for image in product.productimage_set.all()],
            'taste'        : product.tasteproduct_set.first().taste.name,
            'detail'       : description.detail,
            'information'  : description.information,
            'delivery'     : description.delivery,
            'refund'       : description.refund
        }

        return JsonResponse({'result' : product_info}, status=200)

class ProductReviewVeiw(View):
    def get(self, request, product_id):
        order     = request.GET.get('sort', 'id')
        page      = int(request.GET.get('page', 1))
        per_page  = int(request.GET.get('per_page', 0))
        product   = Product.objects.get(id=product_id)
        PAGE_SIZE = 10

        reviews = product.review_set.order_by(order)

        review_info = [{'user'         : review.user.account,
                        'review_image' : review.image_url,
                        'content'      : review.content,
                        'created_at'   : review.created_at,
                        'star_rating'  : review.star_rating
                        } for review in reviews]

        product_rate = product.review_set.aggregate(avg=Avg('star_rating'),count=Count('star_rating'))

        if per_page != 0:
            review_info = []
            products    = Product.objects.order_by('-created_at')[:4]
            for product in products:
                review = product.review_set.first()
                review_info.append({
                    'title'        : product.title,
                    'image'        : product.productimage_set.first().image_url,
                    'user'         : review.user.account,
                    'review_image' : review.image_url,
                    'content'      : review.content,
                    'created_at'   : review.created_at,
                    'star_rating'  : review.star_rating
                })

            return JsonResponse({'result' : review_info}, status=200)

        limit     = PAGE_SIZE * page
        offset    = limit - PAGE_SIZE

        if review_info[offset:limit] == []:
            return JsonResponse({'result' : review_info[0:9], 'product_rate' : product_rate}, status=200)

        return JsonResponse({'result' : review_info[offset:limit-1], 'product_rate' : product_rate}, status=200)
         
class ProductList(View):
    def get(self, request):
        sort     = request.GET.get('sort', '-created_at')
        day      = request.GET.get('day')
        taste    = request.GET.get('taste')
        page     = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 0))
        PER_PAGE = 20
        
        products = Product.objects.annotate(
            rating=Avg('review__star_rating'), day=F('dayproduct__day'), taste=F('tasteproduct__taste')).order_by(sort)

        if day != None:
            products = products.filter(day=day).order_by(sort)
        if taste != None:
            products = products.filter(taste=taste).order_by(sort)
        
        objects_count = products.count()
        pages         = math.ceil(objects_count/PER_PAGE)

        if page <= 0 or page > pages:
            return JsonResponse({'message' : 'PAGE_NOT_FOUND'}, status=404)

        if per_page == 1:
            PER_PAGE = 6
        
        if per_page == 2:
            PER_PAGE = 3
            products = products[:3]
            
        started  = (page - 1) * PER_PAGE
        ended    = started + PER_PAGE
        products = products[started:ended]

        result = [{
            'id'        : product.id,
            'rating'    : round(product.rating,1),
            'title'     : product.title,
            'sub_title' : product.sub_title,
            'price'     : str(int(product.price)),
            'calorie'   : product.calorie,
            'gram'      : str(int(product.gram)),
            'taste'     : product.tasteproduct_set.first().taste.name,
            'images'    : product.productimage_set.first().image_url,
            'reviews'   : product.review_set.aggregate(count=Count('star_rating'))['count']
        } for product in products]

        result.append({
            'count'    : objects_count,
            'page'     : page,
            'per_page' : PER_PAGE,
            'pages'    : pages,
            'elements' : products.count()
        })

        return JsonResponse({'result' : result}, status=200)
    
class SearchView(View):
    def get(self,request):
        search_word = request.GET.get('search_word', None)
        products    = Product.objects.order_by('-created_at')
        
        if search_word: 
            products = Product.objects.filter(Q(title__icontains=search_word) | Q(sub_title__icontains=search_word))

        result =[{
            'id'           : product.id,
            'title'        : product.title,
            'sub_title'    : product.sub_title,
            'price'        : product.price,
            'detail_image' : product.productimage_set.first().image_url,
            'taste'        : product.tasteproduct_set.first().taste.name,
            'calorie'      : product.calorie,
            'gram'         : product.gram,
            'review'       : product.review_set.first().content,
            'star_rating'  : product.review_set.aggregate(average=Avg('star_rating'))['average']
         }for product in products]
         
        return JsonResponse({'result' : result}, status=200)