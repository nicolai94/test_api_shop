from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from config import settings
from constants import LOGIN_USER
from exceptions import NotAuthenticatedUser

User = get_user_model()


class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get('access_token')

        if not access_token:
            raise NotAuthenticatedUser

        try:
            token_key = LOGIN_USER.format(token=access_token, project_name=settings.PROJECT_NAME)
            user_id = cache.get(token_key)
            cache.close()

            if not user_id:
                raise NotAuthenticatedUser

            user = User.objects.get(pk=user_id)
            return user, None
        except User.DoesNotExist:
            raise NotAuthenticatedUser
        except Exception as e:
            raise NotAuthenticatedUser from e
