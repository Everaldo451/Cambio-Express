from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_digit(value:str):
	if not value.isdigit():
		raise ValidationError(
			"%(value)s must be only digits.",
			params={"value":value},
		)

def validate_len(value:str):
	if len(value)!=14:
		raise ValidationError(
			"%(value)s must be 14 characters.",
			params={"value":value},
		)

class Company(models.Model):

	user = models.OneToOneField(
		"users.User",
		on_delete=models.CASCADE,
		related_name="company",
	)
	name = models.CharField(max_length=100, null=False, blank=False)
	CNPJ = models.CharField(unique=True, validators=[validate_len, validate_digit], max_length=20, null=False, blank=False)

	def __str__(self):
		return f"{self.name}, CNPJ: {self.CNPJ}"