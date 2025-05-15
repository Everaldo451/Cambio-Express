from django.db import models
from . import User


class FeedBack(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		verbose_name="user"
	)
	comment = models.CharField(max_length=500, null=True)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id