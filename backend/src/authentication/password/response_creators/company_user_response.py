from rest_framework import status
from rest_framework.response import Response

from companies.models import Company
from . import ResponseCreator
import logging

class CompanyUserResponseCreator(ResponseCreator):
	
    def company_exists(self, data):
        return Company.objects.filter(
			CNPJ=data.get("CNPJ")
		).exists()


    def create_response(self, request, data):
        data.pop("is_company")
        logging.debug("Verifying if company already exists.")
        if self.company_exists(data):
            logging.debug("Response 409. Company already exists.")
            return Response({"message":"Company already exists."}, status=status.HTTP_409_CONFLICT)
        
        register_data = self.register.register_user({**data})
        if register_data["error"] == True:
            logging.debug(f"Response with error: {register_data["message"]}")
            return Response({"message": register_data["message"]}, status=register_data["status"])
        
        company:Company = register_data["obj"]
        return self.jwt_service.generate_response(request, company.user, status.HTTP_201_CREATED)