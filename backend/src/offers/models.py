from django.db import models
from django.core.exceptions import ValidationError

from backend.core.types.offers import CodeChoices, IndexChoices

def validate_gte_0(value):
	if value<0:
		raise ValidationError(
			"%(value)s must be greater than or equal 0.",
			params={"value":value},
		)

class InvestmentOffer(models.Model):

	created_by = models.ForeignKey("companies.Company", on_delete=models.CASCADE, null=False)
	code = models.CharField(
		max_length=10,
		choices=[(tag.name, tag.value.title()) for tag in CodeChoices], 
	)
	index_variable= models.CharField(
		max_length=10,
		choices=[(tag.name, tag.value.title()) for tag in IndexChoices], 
	)
	min_value = models.DecimalField(max_digits=12, decimal_places=2, validators=[validate_gte_0])
	percent = models.DecimalField(max_digits=5, decimal_places=2, validators=[validate_gte_0])

	def __str__(self):
		return f"{self.code} ({self.index_variable}) - {self.percent}%"
