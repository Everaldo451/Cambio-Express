from django.db import models
from django.core.exceptions import ValidationError

def validate_gte_0(value):
	if value<0:
		raise ValidationError(
			"%(value)s must be greater than or equal 0.",
			params={"value":value},
		)

class InvestmentOffer(models.Model):

	created_by = models.ForeignKey("users.Company", on_delete=models.CASCADE, null=False)
	monetary_index = models.ForeignKey("finances.MonetaryIndex", on_delete=models.DO_NOTHING)
	min_value = models.DecimalField(max_digits=12, decimal_places=2, validators=[validate_gte_0])
	percent = models.DecimalField(max_digits=5, decimal_places=2, validators=[validate_gte_0])
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.code} ({self.index_variable}) - {self.percent}%"
