from django.db import DatabaseError, models
from rest_framework import status

def get_obj_by_id_exception_handler(model:models.Model, error:Exception):
	if isinstance(error, model.DoesNotExist):
		return {
			"error": True,
			"message": f"{model.__name__} not found.",
			"status": status.HTTP_404_NOT_FOUND
        }
	elif isinstance(error, DatabaseError):
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


def get_obj_by_id(model:models.Model, id:int):
	data = {}
	try:
		obj = model.objects.get(id=id)
		data = {
			"error": False,
			"message": f"{model.__name__} fetched successfully.",
			"obj": obj,
			"status": status.HTTP_200_OK
        }
	except Exception as error:
		data = get_obj_by_id_exception_handler(model, error)
	return data