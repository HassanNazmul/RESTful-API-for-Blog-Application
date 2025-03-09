from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from django.contrib.auth import get_user_model
from ..services.email_service import EmailService


# Rate limiting for password reset attempts
class PasswordResetRateThrottle(UserRateThrottle):
    rate = '3/hour'


# Handles password reset request initiation
class PasswordResetRequestView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    throttle_classes = [PasswordResetRateThrottle]

    def post(self, request):
        # Extract and validate email
        email = request.data.get('email')
        if not email:
            return Response(
                {'error': 'Email is required.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validate email format using Django's validator
        try:
            EmailValidator()(email)
        except DjangoValidationError:
            return Response(
                {'error': 'Invalid email format.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Find user and send reset email
            User = get_user_model()
            user = User.objects.get(email=email)
            email_sent = EmailService.send_password_reset_email(user, email)
            
            if not email_sent:
                return Response(
                    {'error': 'Failed to send password reset email.'}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
                
            return Response(
                {'message': 'Password reset email has been sent if the email exists in our system.'}, 
                status=status.HTTP_200_OK
            )
            
        except User.DoesNotExist:
            # Return same message to prevent email enumeration
            return Response(
                {'message': 'Password reset email has been sent if the email exists in our system.'}, 
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {'error': 'An unexpected error occurred.'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# Handles password reset confirmation and update
class PasswordResetConfirmView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    throttle_classes = [PasswordResetRateThrottle]

    def post(self, request):
        # Extract required fields from request
        uid = request.data.get('uid')
        token = request.data.get('token')
        password = request.data.get('password')

        # Validate presence of all required fields
        if not all([uid, token, password]):
            return Response(
                {'error': 'All fields (uid, token, password) are required.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Decode user ID and validate user existence
            uid = force_str(urlsafe_base64_decode(uid))
            User = get_user_model()
            user = User.objects.get(pk=uid)

            # Verify token validity
            if not default_token_generator.check_token(user, token):
                return Response(
                    {'error': 'Invalid or expired reset token.'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Validate password strength using Django's validator
            try:
                validate_password(password, user)
            except DjangoValidationError as e:
                return Response(
                    {'error': list(e.messages)}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Update password and save user
            user.set_password(password)
            user.save()

            return Response(
                {'message': 'Password has been reset successfully.'}, 
                status=status.HTTP_200_OK
            )

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response(
                {'error': 'Invalid reset link.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            return Response(
                {'error': 'An unexpected error occurred while resetting password.'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )