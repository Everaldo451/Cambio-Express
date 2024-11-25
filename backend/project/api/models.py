from django.db import models
from authe.models import User
from .model_validators import validate_cnpj, validate_phone


class Company(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		related_name="company",
	)

	name = models.CharField(max_length=100, null=False, blank=False)
	phone = models.CharField(unique=True, validators=[validate_phone], max_length=16, null=True, blank=True)
	CNPJ = models.CharField(unique=True, validators=[validate_cnpj], max_length=20, null=False, blank=False)

	def __str__(self):
		return f"{self.name}, CNPJ: {self.CNPJ}"
	


class FeedBacks(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		verbose_name="user"
	)
	comment = models.CharField(max_length=500, null=True)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id


	

# Create your models here.
