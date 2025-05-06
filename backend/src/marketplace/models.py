from django.db import models
from api.models import Company
from authe.models import User

CODE_CHOICES = [
	("USD", "Dólar"),
	("BTC", "Bitcoin"),
	("EUR", "Euro")
]

class Offert(models.Model):

	company = models.OneToOneField(Company, on_delete=models.CASCADE, null=False)
	code = models.CharField(null=False, choices=CODE_CHOICES, max_length=10)
	min_value = models.FloatField()
	index_variable= models.CharField(max_length=100)  ####Variaveis como IPCA e Selic
	percent = models.FloatField() ###Juros

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
	value = models.FloatField()
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id
	

class Account(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="accounts")
	code = models.CharField(null=False, choices=CODE_CHOICES, max_length=10)
	balance = models.FloatField(default=0)

# Create your models here.
