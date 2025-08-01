from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError

from backend.core.types.user import UserTypes

class UserManager(BaseUserManager):
	
	def _create_user(self,email, password, **extra_fields):

		if not email:
			raise ValidationError("Email will not blank")
		elif not password:
			raise ValidationError("Password will not blank")

		email = self.normalize_email(email)

		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user
	
	def create_user(self, email, password, **extra_fields):

		return self._create_user(email, password, **extra_fields)
	
	def create_superuser(self, email, password, **extra_fields):

		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_active", True)
		extra_fields.setdefault("is_superuser", True)

		return self._create_user(email, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
	
	username = None
	email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
	user_type = models.TextField(
		choices=[(item.value, item.name.title()) for item in UserTypes], 
		default=UserTypes.STANDARD.value,
	)
	date_joined = models.DateTimeField(auto_now=True)

	AUTHENTICATION_CHOICES = [
		('password', "Password"),
		('oauth', 'OAuth')
	]
	authentication_type = models.CharField(max_length=50, null=False, blank=False, choices=AUTHENTICATION_CHOICES, default="password")
	
	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	
	REQUIRED_FIELDS = ["authentication_type"]

	objects = UserManager()

	def __str__(self):
		username = ""

		if not hasattr(self,"company"):
			if self.first_name:
				username = self.first_name
			else:
				username = self.email
		else:
			username = self.company.name

		return username