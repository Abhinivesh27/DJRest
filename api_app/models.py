from django.db import models


class products(models.Model):

    name = models.CharField(max_length=20, default="Mutta parota")
    href = models.CharField(default="/",max_length=100)
    imageSrc = models.CharField(max_length=200,default="https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg")
    imageAlt = models.CharField(max_length=100,default="loading...")
    price = models.CharField(max_length=3,default="௹27")
    color = models.CharField(max_length=10,default="white")

    def __str__(self):
        return self.name