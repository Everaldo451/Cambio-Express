from django.db import models

from backend.core.types.offers import CodeChoices

class Account(models.Model):

	created_by = models.ForeignKey("users.User", on_delete=models.CASCADE, null=False, related_name="accounts")
	code = models.CharField(
		max_length=10,
		choices=[(tag.name, tag.value.title()) for tag in CodeChoices], 
	)
	balance = models.FloatField(default=0)

	class Meta:
		constraints = [
            models.UniqueConstraint(fields=["created_by", "code"], name="unique_code_per_user")
        ]
