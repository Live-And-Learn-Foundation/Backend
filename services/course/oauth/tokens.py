from datetime import datetime
from oauthlib.common import generate_signed_token
from django.utils import timezone
from jwcrypto import jws
import json
import pytz
utc = pytz.UTC


def signed_token_generator(private_pem, **kwargs):
    """
    :param private_pem:
    """
    def signed_token_generator(request):
        request.claims = kwargs
        refresh_token_instance = getattr(
            request, "refresh_token_instance", None)
        if request.scope is None and refresh_token_instance is not None:
            access_token = refresh_token_instance.access_token if refresh_token_instance is not None else None
            scope = access_token.scope if access_token is not None else None
            request.scope = scope
        request.claims.update(
            {
                "sub": str(request.user.id),
                "aud": request.client_id,
                "iat": timezone.now(),
            },
        )
        return generate_signed_token(private_pem, request)

    return signed_token_generator

class JWTAccessToken():
    def __init__(self, claims):
        self.scope = claims["scope"]
        self.client_id = claims["aud"]
        self.user_id = claims["sub"]
        unix_timestamp = int(claims.get("exp", None))
        self.expires = datetime.utcfromtimestamp(unix_timestamp)

    def allow_scopes(self, scopes):
        """
        Check if the token allows the provided scopes

        :param scopes: An iterable containing the scopes to check
        """
        if not scopes:
            return True

        if self.scope is None:
            return False

        provided_scopes = set(self.scope.split())
        resource_scopes = set(scopes)

        return resource_scopes.issubset(provided_scopes)
    
    def is_expired(self):
        """
        Check token expiration with timezone awareness
        """
        if not self.expires:
            return True

        return  timezone.now() >= utc.localize(self.expires)

    def is_valid(self, scopes=None):
        """
        Checks if the access token is valid.

        :param scopes: An iterable containing the scopes to check or None
        """
        return not self.is_expired() and self.allow_scopes(scopes)

    @property
    def scopes(self):
        """
        Returns a dictionary of allowed scope names (as keys) with their descriptions (as values)
        """
        # Don't move this import to global scope, because it it lazay object.
        from oauth2_provider.scopes import get_scopes_backend
        all_scopes = get_scopes_backend().get_all_scopes()
        token_scopes = self.scope.split()
        return {name: desc for name, desc in all_scopes.items() if name in token_scopes}
