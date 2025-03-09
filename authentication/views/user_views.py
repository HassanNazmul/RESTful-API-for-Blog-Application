from django.contrib.auth.models import User
from rest_framework import generics, permissions

from ..serializers import UserProfileSerializer

# Handles user profile operations - both retrieval and updates
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        # Returns the currently authenticated user's profile
        return self.request.user

# Handles read-only access to user details by their ID
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)