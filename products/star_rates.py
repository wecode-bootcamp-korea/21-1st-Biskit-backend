from .models import Product

def star_rates(product):    
    product = Product.objects.get(title=product)
    reviews = product.review_set.all()
    
    count = 0
        
    for review in reviews: 
        count += review.star_rating
    
    count = count/len(reviews)

    return {'star' : count, 'count' : len(reviews)}