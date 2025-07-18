from rest_framework import status
from rest_framework.response import Response

from . import ResponseCreator
import logging

class CommonUserResponseCreator(ResponseCreator):

    def create_response(self, request, data):
        register_data = self.register.register_user({**data})
        if register_data["error"] == True:
            logging.debug(f"Response with error: {register_data["message"]}")
            return Response({"message": register_data["message"]}, status=register_data["status"])
        
        logging.debug(f"Response with status 201. User registed sucessful.")
        user = register_data["obj"]
        return self.jwt_service.generate_response(request, user, status.HTTP_201_CREATED)