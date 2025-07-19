from django.db import DatabaseError, models
from rest_framework import status

def get_n_last_obj_exception_handler(model:models.Model, error:Exception):
	if isinstance(error, DatabaseError):
		return {
			"message": "Database connection error.",
			"status": status.HTTP_502_BAD_GATEWAY
        }
	return {
		"message": "Internal server error.",
		"status": status.HTTP_500_INTERNAL_SERVER_ERROR
    }


def get_n_last_obj(model:models.Model, n:int):
	return model.objects.order_by("-id")[:n]