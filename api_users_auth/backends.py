from django.contrib.auth.models import ModelBackend
from .models import CustomUser


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=kwargs['email'])
        except CustomUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
