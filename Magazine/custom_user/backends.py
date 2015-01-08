from django.conf import settings
from django.contrib.auth.models import check_password
from custom_user.models import AuthUser, AuthUserManager

class AuthUserBackend(object):
	def authenticate(self, email=None, password=None):
		#print("In AuthUserBackend")
		try:
			user = AuthUser.objects.get(email=email)
			if user.check_password(password):
				#print("the user is: :")
				#print(user)
				return user
		except AuthUser.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			user = AuthUser.objects.get(pk=user_id)
			return user
		except AuthUser.DoesNotExist:
			return None
