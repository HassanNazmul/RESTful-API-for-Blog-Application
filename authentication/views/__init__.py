from .auth_views import RegisterView, CustomTokenObtainPairView, LogoutView
from .user_views import UserProfileView, UserDetailView
from .password_views import PasswordResetRequestView, PasswordResetConfirmView
from .auth_views import CustomTokenObtainPairView, LogoutView

__all__ = [
    'RegisterView',
    'CustomTokenObtainPairView',
    'LogoutView',
    'UserProfileView',
    'UserDetailView',
    'PasswordResetRequestView',
    'PasswordResetConfirmView',
]