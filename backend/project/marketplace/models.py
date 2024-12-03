from django.db import models
from api.models import Company
from authe.models import User
from datetime import datetime, timedelta

class Offert(models.Model):

	company = models.OneToOneField(Company, on_delete=models.CASCADE, null=False)
	coin = models.CharField(null=False, choices={
		"USD": "Dólar",
		"BTC": "Bitcoin",
		"EUR": "Euro"
	}, max_length=10)
	value = models.FloatField()
	index_variable= models.CharField(max_length=100)  ####Variaveis como IPCA e Selic
	fees = models.FloatField() ###Juros

	def __str__(self):
		return self.id



class Transaction(models.Model):
	
	buyer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bought_offerts")
	seller = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="selled_offerts")

	offert = models.ForeignKey(
		Offert, 
		on_delete=models.PROTECT, 
		limit_choices_to={"company":seller}
	)

	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id

# Create your models here.
