import re
from django import db
from rest_framework import fields, serializers
from .models import db_data

class dataSerializer(serializers.ModelSerializer):
 class Meta:
     model = db_data
     fields = ['id','name','age','course']