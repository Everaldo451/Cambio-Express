from django.db import models

# Create your models here.

class Client(models.Model):

	user = models.OneToOneField(
		"users.User",
		on_delete=models.CASCADE,
		related_name="client",
	)
	first_name = models.CharField(max_length=50, null=False, blank=False)
	last_name = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
