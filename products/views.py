from django.views     import View
from django.http      import JsonResponse

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
        products = Product.objects.all()

        result = [{
            'title'     : product.title,
            'sub_title' : product.sub_title,
            'price'     : product.price,
            'calorie'   : product.calorie,
            'gram'      : product.gram,
            'taste'     : [taste.taste.taste for taste in product.tasteproduct_set.all()] ,
            'images'    : '' if product.productimage_set.all().first() == None else product.productimage_set.all().first().image_url
        } for product in products]

        return JsonResponse({'result' : result}, status=200)

        

