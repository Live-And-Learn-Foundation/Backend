import logging
from django.http import JsonResponse
from base.middleware.exception import CustomMiddlewareException


class ExceptionHandlingMiddleware:
    """Handle uncaught exceptions instead of raising a 500.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as exception:
            return self.process_exception(request, exception)
        return response

    def process_exception(self, request, exception):
        logging.error(f"An error occurred: {exception}", exc_info=True)
        if isinstance(exception, CustomMiddlewareException):
            return JsonResponse({'error': str(exception)})
        return JsonResponse({'error': 'An unexpected error occurred.'}, status=500)
