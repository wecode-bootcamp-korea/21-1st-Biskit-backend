import csv
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biskit.settings")

import django

django.setup()

from users.models import *

CSV_PATH = 'csv/user_info.csv'
with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        User.objects.create(
            name     = row['name'],
            account  = row['account'],
            password = row['mobile'],
            address  = row['address'],
            mobile   = row['mobile'],
            email    = row['email']
        )
        