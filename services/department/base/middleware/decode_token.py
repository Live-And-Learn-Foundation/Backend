import jwt
from django.utils.deprecation import MiddlewareMixin


class DecodeTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                decoded_token = jwt.decode(
                    token, options={"verify_signature": False})
                request.user_info = decoded_token
            except jwt.InvalidTokenError:
                pass

        return None
