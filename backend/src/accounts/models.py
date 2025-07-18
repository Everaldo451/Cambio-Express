from django.db import models
from offerts.models import CODE_CHOICES

class Account(models.Model):

	user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=False, related_name="accounts")
	code = models.CharField(null=False, choices=CODE_CHOICES, max_length=10)
	balance = models.FloatField(default=0)

	class Meta:
		constraints = [
            models.UniqueConstraint(fields=["user", "code"], name="unique_code_per_user")
        ]
