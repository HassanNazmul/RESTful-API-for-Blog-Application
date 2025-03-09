from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings

class EmailService:
    @staticmethod
    def send_password_reset_email(user, email):
        # Generate token and uid for password reset
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        
        # Get reset URL from settings with fallback
        reset_base_url = getattr(
            settings, 
            'PASSWORD_RESET_URL', 
            'http://localhost:3000/reset-password'
        )
        reset_url = f"{reset_base_url.rstrip('/')}/{uid}/{token}/"
        
        # Send email
        try:
            send_mail(
                'Password Reset Request',
                f'Click the following link to reset your password: {reset_url}\n\n'
                'This link will expire in 24 hours.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return True
        except Exception:
            return False