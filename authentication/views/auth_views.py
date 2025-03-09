from django.apps import apps
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import UserSerializer, CustomTokenObtainPairSerializer

# Handles new user registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

# Extends TokenObtainPairView to include additional claims in JWT tokens
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Handles user logout by blacklisting their refresh token
class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            # Get and validate refresh token
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Blacklist the token to prevent reuse
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(
                {"message": "Successfully logged out"}, 
                status=status.HTTP_200_OK
            )
        except (TypeError, ValueError):
            return Response(
                {"error": "Invalid refresh token"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            return Response(
                {"error": "An error occurred during logout"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )