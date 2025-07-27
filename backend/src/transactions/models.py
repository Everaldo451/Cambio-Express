from django.db import models

class Transaction(models.Model):
	
	buyer = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="bought_offers")
	investment_offer = models.ForeignKey("offers.InvestmentOffer", on_delete=models.PROTECT)
	value = models.FloatField()
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id

