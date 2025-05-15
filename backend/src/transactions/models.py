from django.db import models

class Transaction(models.Model):
	
	buyer = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="bought_offerts")
	seller = models.ForeignKey("companies.Company", on_delete=models.PROTECT, related_name="selled_offerts")
	offert = models.ForeignKey(
		"offerts.Offert", 
		on_delete=models.PROTECT, 
		limit_choices_to={"company":seller}
	)
	value = models.FloatField()
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id

