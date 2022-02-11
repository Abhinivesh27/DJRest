from django.urls import path
from django.urls import path
from .views import GenericView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('data/', GenericView.as_view()),
    path('data/<int:id>/', GenericView.as_view()),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'), 
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
    