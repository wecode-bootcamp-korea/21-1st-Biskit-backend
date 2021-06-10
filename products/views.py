from django.views     import View
from django.http      import JsonResponse

from products.models  import Product

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
            'images'    : product.productimage_set.all().first().image_url
        } for product in products]

        return JsonResponse({'result' : result}, status=200)