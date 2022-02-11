import re
from django import db
from rest_framework import fields, serializers
from .models import products

class dataSerializer(serializers.ModelSerializer):
 class Meta:
     model = products
     fields = ['id','name','href','imageSrc','imageAlt','price','color']