from rest_framework import status

from common.exceptions import CustomException


class NotAuthenticatedUser(CustomException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Not authenticated"
        self.default_code = "user_not_authenticated"


class DoesNotExistAccessTokenException(CustomException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Does not exist access token"
        self.default_code = "does_not_have_token"


class UserDoesNotExistException(CustomException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "User not found"
        self.default_code = "user_not_found"
