from rest_framework.exceptions import APIException


class CustomException(APIException):
    def __init__(self, status_code, detail, default_code):
        self.status_code = status_code
        self.detail = detail
        self.default_code = default_code
