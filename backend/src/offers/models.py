from django.db import models

CODE_CHOICES = [
	("USD", "Dólar"),
	("BTC", "Bitcoin"),
	("EUR", "Euro")
]

class InvestmentOffer(models.Model):

	created_by = models.OneToOneField("users.User", on_delete=models.CASCADE, null=False)
	code = models.CharField(null=False, choices=CODE_CHOICES, max_length=10)
	min_value = models.FloatField()
	index_variable= models.CharField(max_length=100)  ####Variaveis como IPCA e Selic
	percent = models.FloatField() ###Juros

	def __str__(self):
		return self.id
