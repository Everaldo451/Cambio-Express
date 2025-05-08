from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from .model_validators import validate_cnpj, validate_phone

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



class Company(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		related_name="company",
	)
	name = models.CharField(max_length=100, null=False, blank=False)
	CNPJ = models.CharField(unique=True, validators=[validate_cnpj], max_length=20, null=False, blank=False)

	def __str__(self):
		return f"{self.name}, CNPJ: {self.CNPJ}"
	


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


CODE_CHOICES = [
	("USD", "Dólar"),
	("BTC", "Bitcoin"),
	("EUR", "Euro")
]

class Offert(models.Model):

	company = models.OneToOneField(Company, on_delete=models.CASCADE, null=False)
	code = models.CharField(null=False, choices=CODE_CHOICES, max_length=10)
	min_value = models.FloatField()
	index_variable= models.CharField(max_length=100)  ####Variaveis como IPCA e Selic
	percent = models.FloatField() ###Juros

	def __str__(self):
		return self.id



class Transaction(models.Model):
	
	buyer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bought_offerts")
	seller = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="selled_offerts")
	offert = models.ForeignKey(
		Offert, 
		on_delete=models.PROTECT, 
		limit_choices_to={"company":seller}
	)
	value = models.FloatField()
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.id
	


class Account(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="accounts")
	code = models.CharField(null=False, choices=CODE_CHOICES, max_length=10)
	balance = models.FloatField(default=0)

# Create your models here.

	



	

# Create your models here.
