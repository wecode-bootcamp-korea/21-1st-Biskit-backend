from django.db import models

class User(models.Model):
    name     = models.CharField(max_length=45)
    account  = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=200)
    mobile   = models.CharField(max_length=45)
    address  = models.CharField(max_length=200)
    email    = models.EmailField(max_length=80)

    class Meta:
        db_table = 'users'        