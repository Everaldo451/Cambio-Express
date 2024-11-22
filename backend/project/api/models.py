from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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
	
	def _create_user(self,email,full_name,password, is_staff, is_superuser, **extra_fields):

		now = timezone.now()
		email = self.normalize_email(email)

		print(email)

		user = self.model(full_name=full_name, email=email, is_staff=is_staff, is_superuser=is_superuser, last_login=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_user(self,email,full_name,password, **extra_fields):

		return self._create_user(email,full_name,password,False,False, **extra_fields)
	
	def create_superuser(self,email,full_name,password, **extra_fields):

		return self._create_user(email,full_name,password,True,True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
	
	full_name = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField(max_length=254,unique=True,null=False)
	money = models.FloatField(default=0)

	date_joined = models.DateTimeField(auto_now=True)
	
	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	
	REQUIRED_FIELDS = ["email","password"]

	objects = UserManager()

	def __str__(self):
		username = None

		if self.company is None:
			username = self.full_name.split()[0]
		else:
			username = self.company.name

		return username

class Company(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		related_name="company",
	)

	name = models.CharField(max_length=100)
	phone = models.CharField(unique=True, validators=[validate_phone], max_length=16)
	CNPJ = models.CharField(unique=True, validators=[validate_cnpj], max_length=20)

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
