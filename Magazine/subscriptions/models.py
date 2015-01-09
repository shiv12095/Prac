from django.db import models
from custom_user.models import AuthUser

class MagazineSubscription(models.Model):
	magazine_name = models.CharField(max_length=30, blank=False, null=False)
	subscriber_name = models.CharField(max_length=30, blank=False, null=False)
	subscriber_mobile_number = models.CharField(max_length=15, blank=False, null=False)
	amount = models.PositiveIntegerField(blank=False, null=False)
	mode_of_payment = models.CharField(max_length=30, blank=False, null=False)
	subscription_start_date = models.DateField(null=True, default=None)
	subscription_end_date = models.DateField(null=True, default=None)
	subscriber_address = models.CharField(max_length=255, blank=False, null=False)
	subscriber_pincode = models.PositiveIntegerField(blank=False, null=False)
	subscriber_state = models.CharField(max_length=30, blank=False, null=False)
	subscription_id = models.CharField(max_length=30, blank=False, null=False, unique=True)
	user_id = models.ForeignKey(AuthUser)