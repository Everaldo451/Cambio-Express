from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_cnpj(value:str):
	x = re.search(r"\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}", value)
	if not x.group():
		raise ValidationError(
			("%(value) não é um CNPJ válido"),
			params={"value":value},
		)

def validate_phone(value:str):
	x = re.search(r"\(\d{2}\)\s\d{5}-\d{4}", value)
	if not x.group():
		raise ValidationError(
			("%(value) não é um telefone válido"),
			params={"value":value}
		)
	

class Company(models.Model):

	user = models.OneToOneField(
		"users.User",
		on_delete=models.CASCADE,
		related_name="company",
	)
	name = models.CharField(max_length=100, null=False, blank=False)
	CNPJ = models.CharField(unique=True, validators=[validate_cnpj], max_length=20, null=False, blank=False)

	def __str__(self):
		return f"{self.name}, CNPJ: {self.CNPJ}"