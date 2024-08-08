from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from time import timezone

class UserManager(BaseUserManager):
	
	def _create_user(self,email,username,password, is_staff, is_superuser, **extra_fields):

		now = timezone.now()
		email = self.normalize_email(email)

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
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)
	
	
	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	
	REQUIRED_FIELDS = ["username","password","email"]

	objects = UserManager()

	

# Create your models here.
