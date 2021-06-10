from django.db import models

class Product(models.Model):
    title      = models.CharField(max_length=45)
    sub_title  = models.CharField(max_length=100)
    price      = models.DecimalField(max_digits=8, decimal_places=2)
    gram       = models.DecimalField(max_digits=6, decimal_places=1)
    calorie    = models.DecimalField(max_digits=6, decimal_places=1)
    stock      = models.IntegerField()
    sell_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'

class Category(models.Model):
    name    = models.CharField(max_length=45)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Description(models.Model):
    detail      = models.URLField()
    information = models.URLField()
    delivery    = models.URLField()
    refund      = models.URLField()
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'descriptions'

class ProductImage(models.Model):
    image_url = models.URLField()
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'

class Day(models.Model):
    days = models.IntegerField()

    class Meta:
        db_table = 'days'

class DayProduct(models.Model):
    day     = models.ForeignKey(Day, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'day_products'

class Taste(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'tastes'

class TasteProduct(models.Model):
    taste   = models.ForeignKey(Taste, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'taste_products'

class Like(models.Model):
    dip     = models.BooleanField(default=False)
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'

class Review(models.Model):
    image_url   = models.URLField()
    content     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    star_rating = models.DecimalField(max_digits=2, decimal_places=1)
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta():
        db_table = 'reviews'