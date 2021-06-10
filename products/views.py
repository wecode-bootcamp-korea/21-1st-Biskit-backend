from django.views     import View
from django.http      import JsonResponse

from products.models import Product

class ProductList(View):

    def get(self, request):

        products = Product.objects.all()
        
        result = []

        for product in products:

            images     = product.productimage_set.all()
            image_list = [image.image_url for image in images]
            tastes     = product.tasteproduct_set.all()
            taste      = [taste.taste.taste for taste in tastes]

            product_info = {
                'title'     : product.title,
                'sub_title' : product.sub_title,
                'price'     : product.price,
                'calorie'   : product.calorie,
                'gram'      : product.gram,
                'taste'     : taste,
                'images'    : image_list
            }

            result.append(product_info)

        return JsonResponse({'message' : 'SUCCESS', 'result' : result}, status=200)