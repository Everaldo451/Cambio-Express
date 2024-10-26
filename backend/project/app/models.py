from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

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
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now())
	
	
	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	
	REQUIRED_FIELDS = ["username","password"]

	objects = UserManager()


class FeedBacks(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		verbose_name="user"
	)

	comment = models.CharField(max_length=500, null=True)
	stars = models.IntegerField(choices={i: i for i in range(1, 6)})



	

# Create your models here.
