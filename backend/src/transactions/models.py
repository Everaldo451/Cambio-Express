from django.db import models

class Transaction(models.Model):
	
	created_by = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="bought_offers")
	investment_offer = models.ForeignKey("offers.InvestmentOffer", on_delete=models.PROTECT)
	value = models.DecimalField(max_digits=12, decimal_places=2)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id

