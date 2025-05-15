from django.db import models
from . import User, Company, Offert


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