from rest_framework import status
from common.exceptions import CustomException


class CartDoesNotExistException(CustomException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Cart not found"
        self.default_code = "cart_not_found"


class CartItemDoesNotExistException(CustomException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Cart Item not found"
        self.default_code = "cart_item_not_found"


class CartAlreadyExistException(CustomException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Cart already exist"
        self.default_code = "cart_already_exist_not_found"


class CartCreationException(CustomException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Cart creation error"
        self.default_code = "cart_creation_error"
