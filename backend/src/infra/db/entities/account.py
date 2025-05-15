from django.db import models
from . import User
from .offert import CODE_CHOICES


class Account(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="accounts")
	code = models.CharField(null=False, choices=CODE_CHOICES, max_length=10)
	balance = models.FloatField(default=0)