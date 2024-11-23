from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.utils import timezone
import re

####MODEL VALIDATORS

def validate_cnpj(value:str):
	x = re.search(r"\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}", value)
	if not x.group():
		raise ValidationError(
			("%(value) não é um CNPJ válido"),
			params={"value":value},
		)

def validate_phone(value:str):
	x = re.search(r"\(\d{2}\)\s\d{5}-\d{4}", value)
	if not x.group():
		raise ValidationError(
			("%(value) não é um telefone válido"),
			params={"value":value}
		)

####MODELS

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
	money = models.FloatField(default=0)

	date_joined = models.DateTimeField(auto_now=True)
	
	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	
	REQUIRED_FIELDS = []

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

class Company(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		related_name="company",
	)

	name = models.CharField(max_length=100, null=False, blank=False)
	phone = models.CharField(unique=True, validators=[validate_phone], max_length=16, null=True, blank=True)
	CNPJ = models.CharField(unique=True, validators=[validate_cnpj], max_length=20, null=False, blank=False)

	def __str__(self):
		return self.name
	


class FeedBacks(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		verbose_name="user"
	)
	comment = models.CharField(max_length=500, null=True)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id


	

# Create your models here.
