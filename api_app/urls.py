from django.urls import path
from django.urls import path
from .views import DatViewClass, data_details, GenericView

urlpatterns = [
    path('data/', GenericView.as_view()),
    path('details/<int:id>/', GenericView.as_view()),
]