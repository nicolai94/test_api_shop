from rest_framework import status
from common.exceptions import CustomException


class ProductDoesNotExistException(CustomException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Product not found"
        self.default_code = "product_not_found"


class CategoryDoesNotExistException(CustomException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Category not found"
        self.default_code = "category_not_found"
