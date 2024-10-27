from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
import requests


class CustomJWTAuthentication(BaseAuthentication):
    def __init__(self):
        # Set this to your Auth Service's JWKS endpoint
        self.jwks_url = settings.JWKS_URL
        self.jwk = self.fetch_jwk()

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            token = auth_header.split()[1]
            decoded = jwt.decode(
                token,
                self.jwk,
                algorithms=['RS256'],
                # Turn this on/off based on needs
                options={"verify_aud": False}
            )
            # Retrieve or create a user from the decoded token info
            user = decoded
            return (user, None)
        except jwt.InvalidTokenError as e:
            raise AuthenticationFailed(f"Invalid token: {str(e)}")

    def fetch_jwk(self):
        response = requests.get(self.jwks_url)
        jwks = response.json()
        # Here you would select the key you need based on 'kid'
        # We're assuming a single key pair for simplicity
        return jwt.algorithms.RSAAlgorithm.from_jwk(jwks['keys'][0])
