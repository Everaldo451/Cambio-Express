from abc import abstractmethod, ABC
from django.http import HttpRequest

class Register[T](ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def register_exception_handler(self, error:Exception):
        raise NotImplementedError
    
    @abstractmethod
    def create_user(self, user_data:dict) -> T:
        raise NotImplementedError
    
    @abstractmethod
    def register_user(self, user_data:dict):
        raise NotImplementedError