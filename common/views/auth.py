import logging
import uuid

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from common.serializers.auth import UserLoginSerializer
from config import settings
from constants import LOGIN_USER
from exceptions import UserDoesNotExistException, DoesNotExistAccessTokenException

logger = logging.getLogger("main")


@extend_schema(request=UserLoginSerializer, summary="Логин", tags=["Аутентификация & Авторизация"])
@api_view(["POST"])
def user_login(request: Request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")

        user = None
        if "@" in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist as e:
                logger.info(f"User not found {e}")
                raise UserDoesNotExistException

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token = str(uuid.uuid4().hex)
            response = Response({"token": token}, status=status.HTTP_200_OK)
            if request.data.get("remember_me"):
                expire = 3600 * 24 * 30
                response.set_cookie("remember_me", "on")
            else:
                expire = 3600
                response.delete_cookie("remember_me")

            response.set_cookie("access_token", token, secure=True, expires=expire, httponly=True)

            cache.set(
                key=LOGIN_USER.format(token=token, project_name=settings.PROJECT_NAME), value=user.pk, timeout=expire
            )

            return response

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@extend_schema(summary="Логаут", tags=["Аутентификация & Авторизация"])
@api_view(["POST"])
def user_logout(request: Request):
    if request.method == "POST":
        try:
            access_token = request.COOKIES.get("access_token")
            if not access_token:
                logger.info("Does not exist access token")
                raise DoesNotExistAccessTokenException

            response = Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
            response.delete_cookie(key=access_token)
            cache.delete(LOGIN_USER.format(token=access_token, project_name=settings.PROJECT_NAME))

            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
