from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    LogoutView,
    UserProfileView,
    UserDetailView,
    PasswordResetRequestView,
    PasswordResetConfirmView
)

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('auth/password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('auth/password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    
    # User management endpoints
    path('users/me/', UserProfileView.as_view(), name='user_profile'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]