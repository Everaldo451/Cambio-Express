from django.db import models

class Account(models.Model):

	created_by = models.ForeignKey("users.User", on_delete=models.CASCADE, null=False, related_name="accounts")
	currency = models.ForeignKey("finances.Currency", on_delete=models.DO_NOTHING)
	balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['created_by', 'currency'], name='unique_currency_per_user')
		]
