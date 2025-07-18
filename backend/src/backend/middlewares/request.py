import logging
from decouple import config

print(__name__)
logger = logging.getLogger(__name__)


def LogRequest(get_response):

    def middleware(request):

        endpoint:str = request.get_full_path()
        admin_url = config("DJANGO_ADMIN_URL", 'admin/')

        if admin_url and endpoint.startswith("/"+admin_url):
            return get_response(request)
        
        method = request.method
        endpoint = request.get_full_path()

        user = request.user
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
        
    