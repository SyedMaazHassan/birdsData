from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth
# Create your models here.


class bird_orders(models.Model):
    id = models.IntegerField(primary_key = True)
    scientific_name = models.CharField(max_length = 255, blank = True, default = "NULL", unique = True)
    brief_description = models.CharField(max_length = 255, blank = True, default = "NULL", null = True)
    order_image = models.ImageField(upload_to = "photos", blank = True, default = "NULL", null = True)


class bird_families(models.Model):
    id = models.IntegerField(primary_key = True)
    scientific_name = models.CharField(max_length = 255, blank = True, default = "NULL", unique = True)
    brief_description = models.CharField(max_length = 255, blank = True, default = "NULL", null = True)
    bird_orders = models.ForeignKey(bird_orders, on_delete = models.CASCADE)
    
class birds_bill_shapes(models.Model):
    id = models.CharField(primary_key = True, max_length = 3)
    bill_shape = models.CharField(max_length = 25, null = True, default = "NULL")
    bill_example = models.ImageField(upload_to = "photos", blank = True, null = True)

class birds_body_shapes(models.Model):
    id = models.CharField(primary_key = True, max_length = 3)
    body_shape = models.CharField(max_length = 25, null = True, default = "NULL")
    body_example = models.ImageField(upload_to = "photos", blank = True, null = True)
    
class birds_wing_shapes(models.Model):
    id = models.CharField(primary_key = True, max_length = 3)
    wing_shape = models.CharField(max_length = 25, null = True, default = "NULL")
    wing_example = models.ImageField(upload_to = "photos", blank = True, null = True)
    
class conservation_status(models.Model):
    id = models.IntegerField(primary_key = True)
    conservation_category = models.CharField(max_length = 10, null = True, default = "NULL")
    conservation_state = models.CharField(max_length = 25, null = True, default = "NULL")

class birds(models.Model):
    id = models.IntegerField(primary_key = True)
    scientific_name = models.CharField(max_length = 100, blank = True, default = "NULL", null = True, unique = True)
    common_name = models.CharField(max_length = 255, blank = True, default = "NULL", null = True)
    family = models.ForeignKey(bird_families, on_delete = models.CASCADE, null = True, blank = True)
    conservation_status = models.ForeignKey(conservation_status, on_delete = models.CASCADE, null = True, blank = True)
    wing = models.ForeignKey(birds_wing_shapes, on_delete = models.CASCADE, null = True, blank = True)
    body = models.ForeignKey(birds_body_shapes, on_delete = models.CASCADE, null = True, blank = True)
    bill = models.ForeignKey(birds_bill_shapes, on_delete = models.CASCADE, null = True, blank = True)
    description = models.TextField(null = True, blank = True)

class sighting(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bird = models.ForeignKey(birds, on_delete = models.CASCADE)
    date_time = models.DateTimeField(default = datetime.now())
    location = models.CharField(max_length = 255)
    comments = models.TextField(null = True, blank = True)

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver