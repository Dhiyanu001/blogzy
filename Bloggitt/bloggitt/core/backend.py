from turtle import home
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class DomainRestrictedAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password) and email.endswith('@psgtech.ac.in'):
                return home
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
# from django.contrib.auth.backends import ModelBackend
# from django.core.exceptions import ValidationError

# ALLOWED_DOMAIN = 'psgtech.ac.in'

# class DomainEmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         # Perform email domain validation
#         if not username.endswith('@' + ALLOWED_DOMAIN):
#             raise ValidationError('Invalid email domain. Please use an email address from ' + ALLOWED_DOMAIN)
#         # Call the parent authenticate method with the validated username
#         return super().authenticate(request, username=username, password=password, **kwargs)


