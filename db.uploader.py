import django
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biskit.settings")

django.setup()
from users.models import *
from products.models import *
from orders.models import *


# with open('csv/days.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         Day.objects.create(
#             days = row['days']
#         )

# with open('csv/product_info2.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         Product.objects.create(
#             title = row['title'],
#             sub_title = row['sub_title'],
#             price = row['price'],
#             gram = row['gram'],
#             calorie = row['calorie'],
#             stock = row['stock'],
#             sell_count = row['sell_count']
#         )

# with open('csv/user_info.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         User.objects.create(
#             name     = row['name'],
#             account  = row['account'],
#             password = row['mobile'],
#             address  = row['address'],
#             mobile   = row['mobile'],
#             email    = row['email']
#         )

# with open('csv/tastes.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         Taste.objects.create(
#             name = row['name']
#         )

# with open('csv/taste_products.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         TasteProduct.objects.create(
#             product_id = row['product_id'],
#             taste_id = row['taste_id']
#         )

# with open('csv/status.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         Status.objects.create(
#             status = row['status']
#         )

# with open('csv/product_image2.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         ProductImage.objects.create(
#             product_id = row['product_id'],
#             image_url = row['image_url']
#         )

# with open('csv/description_info.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         Description.objects.create(
#             product_id = row['product_id'],
#             detail = row['detail'],
#             information = row['information'],
#             delivery = row['delivery'],
#             refund = row['refund']
#         )

# with open('csv/day_products.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         DayProduct.objects.create(
#             product_id = row['product_id'],
#             day_id = row['day_id']
#         )

# with open('csv/review.csv', newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         Review.objects.create(
#             image_url = row['image_url'],
#             content = row['content'],
#             created_at = row['created_at'],
#             star_rating = row['star_rating'],
#             product_id = row['product_id'],
#             user_id = row['user_id']
#         )
#update
with open('csv/review.csv', newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    pl=Review.objects.all()
    rowlist = []
    for row in data_reader:
        rowlist.append(row['created_at'])

    for i in range(len(pl)):
        a = pl[i]
        a.created_at = rowlist[i]
        a.save()

with open('csv/product_info2.csv', newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    pl=Product.objects.all()
    rowlist = []
    for row in data_reader:
        rowlist.append(row['created_at'])

    for i in range(len(pl)):
        a = pl[i]
        a.created_at = rowlist[i]
        a.save()