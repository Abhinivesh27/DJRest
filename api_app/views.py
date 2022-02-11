from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import products
from .serializers import dataSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status, generics , mixins
from rest_framework.views import APIView 

#Generic API view 
class GenericView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = dataSerializer
    queryset = products.objects.all()
    lookup_field = 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)
#Class based API Views
# class DatViewClass(APIView):

#     def get(self, request):
#         data = db_data.objects.all()
#         serializer = dataSerializer(data, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = dataSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # Class based API view 
# class data_details(APIView):
    
#     def get_object(self, id):
#         try:
#             return db_data.objects.get(id=id)
#         except db_data.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND) 

#     def get(self, request, id):
#         data = self.get_object(id)
#         serializer = dataSerializer(data)
#         return Response(serializer.data)

#     def put(self, request, id):
#         data = self.get_object(id)
#         serializer = dataSerializer(data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         data = self.get_object(id)
#         data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 
 
# #Function based API view
# @csrf_exempt 
# def data_view(request):

#     if request.method == 'GET':
#         data_input = db_data.objects.all()
#         serializer = dataSerializer(data_input, many=True)
#         return JsonResponse(serializer.data, safe = False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = dataSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

