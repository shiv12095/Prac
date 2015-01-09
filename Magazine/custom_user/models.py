from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
# Create your models here.

class AuthUserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, date_of_birth, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(email=self.normalize_email(email),
							date_of_birth = date_of_birth,
							first_name = first_name,
							last_name = last_name )
		user.is_active = True
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(email=email, password=password , first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
		user.is_staff = True
		user.is_active = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class AuthUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(verbose_name='email address' , unique=True, max_length=255)
	first_name = models.CharField(max_length=30, null=False, blank=False)
	last_name = models.CharField(max_length=30, null=False, blank=False)
	gender = models.CharField(max_length=1, null=False, blank=False)
	date_of_birth = models.DateField(null=True, default=None)
	date_joined = models.DateField(null=True, default=None)
	is_active = models.BooleanField(default=True, null=False)
	is_staff = models.BooleanField(default=True, null=False)

	objects = AuthUserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name' , 'last_name' , 'date_of_birth', 'gender']

	def get_full_name(self):
		fullname = self.first_name + " " + self.last_name
		return fullname

	def get_short_name(self):
		return self.first_name	

	def __unicode__(self):
		return self.email	

