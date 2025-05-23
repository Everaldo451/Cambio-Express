from django.db import DatabaseError, models
from rest_framework import status

def get_n_last_obj_exception_handler(model:models.Model, error:Exception):
	if isinstance(error, DatabaseError):
		return {
			"error": True,
			"message": "Database connection error.",
			"status": status.HTTP_502_BAD_GATEWAY
        }
	return {
		"error": True,
		"message": "Internal server error.",
		"status": status.HTTP_500_INTERNAL_SERVER_ERROR
    }


def get_n_last_obj(model:models.Model, n:int):
	data = {}
	try:
		obj = model.objects.order_by("-id")[:n]
		data = {
			"error": False,
			"message": f"Last {n} {model.__name__} fetched successfully.",
			"obj": obj,
			"status": status.HTTP_200_OK
        }
	except Exception as error:
		data = get_n_last_obj_exception_handler(model, error)
	return data