from rest_framework.exceptions import APIException
from rest_framework.views import status

# class NonUptableKeyError(Exception):
#     ...

class NonUptableKeyError(APIException):
      status_code = status.HTTP_401_UNAUTHORIZED
