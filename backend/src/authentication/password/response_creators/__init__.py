from abc import ABC, abstractmethod
from django.http import HttpRequest
from authentication.services.jwt_service import JWTService
from authentication.registers import Register

class ResponseCreator(ABC):

    def __init__(self, jwt_service:JWTService, register:Register):
        self.jwt_service = jwt_service
        self.register = register

    @abstractmethod
    def create_response(self, request:HttpRequest, data:dict):
        raise NotImplementedError


