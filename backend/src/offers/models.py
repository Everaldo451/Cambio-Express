from django.db import models

from backend.core.types.offers import CodeChoices, IndexChoices

class InvestmentOffer(models.Model):

	created_by = models.ForeignKey("users.User", on_delete=models.CASCADE, null=False)
	code = models.CharField(
		max_length=10,
		choices=[(tag.name, tag.value.title()) for tag in CodeChoices], 
	)
	index_variable= models.CharField(
		max_length=10,
		choices=[(tag.name, tag.value.title()) for tag in IndexChoices], 
	)
	min_value = models.DecimalField(max_digits=12, decimal_places=2)
	percent = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.code} ({self.index_variable}) - {self.percent}%"
