from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, PasswordResetRequestView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
     path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
]
