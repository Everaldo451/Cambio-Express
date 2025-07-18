from django.db import DatabaseError, models
from rest_framework import status

def get_all_obj_exception_handler(model:models.Model, error:Exception):
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


def get_all_obj(model:models.Model):
	data = {}
	try:
		obj = model.objects.all()
		data = {
			"error": False,
			"message": f"All {model.__name__} fetched successfully.",
			"obj": obj,
			"status": status.HTTP_200_OK
        }
	except Exception as error:
		data = get_all_obj_exception_handler(model, error)
	return data