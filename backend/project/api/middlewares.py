from django.http import HttpResponse, HttpRequest
import logging
import os

print(__name__)
logger = logging.getLogger(__name__)


def LogRequest(get_response):

    def middleware(request):

        endpoint:str = request.get_full_path()

        if endpoint.startswith("/"+os.environ.get("DJANGO_ADMIN_URL")):
            return get_response(request)
        
        method = request.method
        endpoint = request.get_full_path()


        user = request.user
        print(user)
        username = "anonymous"

        if user.is_authenticated:
            if user.is_superuser: 
                return get_response(request)
            username = user.username
        
        response = get_response(request)
        status = response.status_code

        extra = {
            "username":username, 
            "status": status, 
            "method": method,
            "endpoint": endpoint,
        }

        logger.info("Request:", extra=extra)

        return response

    return middleware
        
    