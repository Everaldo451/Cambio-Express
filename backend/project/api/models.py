from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, GroupManager
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
	
	def _create_user(self,email,username,password, is_staff, is_superuser, **extra_fields):

		now = timezone.now()
		email = self.normalize_email(email)

		print(email)

		user = self.model(username=username, email=email, is_staff=is_staff, is_superuser=is_superuser, last_login=now, date_joined=now)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_user(self,email,username,password, **extra_fields):

		return self._create_user(email,username,password,False,False, **extra_fields)
	
	def create_superuser(self,email,username,password, **extra_fields):

		return self._create_user(email,username,password,True,True, **extra_fields)


class User(AbstractBaseUser):
	
	username = models.CharField(max_length=100,unique=True,null=False)
	email = models.EmailField(max_length=254,unique=True,null=False)
	money = models.FloatField(default=0)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_company = models.BooleanField(default=False)

	date_joined = models.DateTimeField(default=timezone.now())
	
	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	
	REQUIRED_FIELDS = ["username","password"]

	objects = UserManager()


class Company(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
	)
	name = models.CharField(max_length=100)
	phone = models.CharField(unique=True, validators=[validate_phone], max_length=16)
	CNPJ = models.CharField(unique=True, validators=[validate_cnpj], max_length=20)

class FeedBacks(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		verbose_name="user"
	)
	comment = models.CharField(max_length=500, null=True)
	stars = models.IntegerField(choices={i: i for i in range(1, 6)})



	

# Create your models here.
