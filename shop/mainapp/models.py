from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=30)
    price=models.PositiveBigIntegerField(null=False)
    decs=models.TextField()
    pic=models.ImageField(upload_to="products/",null=False)
    stock=models.PositiveIntegerField(default=1)
