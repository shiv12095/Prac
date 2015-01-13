from django import forms
from subscriptions.models import MagazineSubscription
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class MagazineSubscriptionForm(forms.ModelForm):
	year = date.today().year
	MAGAZINE_CHOICES = (('People\'s Demococracy' ,'People\'s Democracy'), ('India Today' , 'India Today'))
	PAYMENT_MODE_CHOICES = (('cash','Cash'), ('credit card','Credit Card'), ('net banking' , 'Net Banking'), ('cheque' , 'Cheque'))

	STATE_CHOICES = (
		('AP' ,'Andhra Pradesh'),('AR' ,'Arunachal Pradesh'),('AS' ,'Assam'),
		('BR' ,'Bihar'),('CT' ,'Chhattisgarh'),('GA' ,'Goa'),('GJ' ,'Gujrat'),('HR' ,'Haryana'),
		('HP' ,'Himachal Pradesh'),('JK' ,'Jammu and Kashmir'),('JH' ,'Jharkhand'),
		('KA' ,'Karnataka'),('KL' ,'Kerala'),('MP' ,'Madhya Pradesh'),('MH' ,'Maharashtra'),
		('MN' ,'Manipur'),('ML' ,'Meghalaya'),('MZ' ,'Mizoram'),('OR' ,'Odisha'),('PB' ,'Punjab'),
		('RJ' ,'Rajasthan'),('SK' ,'Sikkim'),('TN' ,'Tamil Nadu'),('TG' ,'Telangana'),
		('TR' ,'Tripura'),('UP' ,'Uttar Pradesh'),('UT' ,'Uttrakhand'),('WB' ,'West Bengal'),
		('AN' ,'Andaman and Nicobar Islands'),('CN' ,'Chandigarh'),('DN' ,'Dadra and Nagar Haveli'),
		('DD' ,'Daman and Diu'),('LD' ,'Lakshadweep'),('DL' ,'National Capital Territory of India'),
		('PY' ,'Puducherry'))

	magazine_name = forms.ChoiceField(label="Magazine", choices=MAGAZINE_CHOICES)
	subscriber_name = forms.CharField(label="Subscriber Name", max_length=30, required=True)
	subscriber_mobile_number = forms.IntegerField(label="Subscriber Mobile Number", required=True)
	amount = forms.IntegerField(label="Amount paid", required=True)
	mode_of_payment = forms.ChoiceField(label="Mode of Payment", choices=PAYMENT_MODE_CHOICES, initial='cash', required=True)
	subscription_start_date = forms.DateField(label="Subscription start date", widget=SelectDateWidget(years=range(year,year+5,+1)))
	subscription_end_date = forms.DateField(label="Subscription end date", widget=SelectDateWidget(years=range(year,year+5,+1)))
	subscriber_address = forms.CharField(label="Subscriber Address", max_length=255, required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols':40}))
	subscriber_state = forms.ChoiceField(label="State", choices=STATE_CHOICES)
	subscriber_pincode = forms.IntegerField(label="Pincode")

	class Meta:
		model = MagazineSubscription
		exclude = ('user_id', 'subscription_id', 'cancelled')

	def clean_amount(self):
		#print("clean_amount")
		if self.cleaned_data.get("amount") < 0:
			raise forms.ValidationError("Invalid Amount Entered")
		else:
			return self.cleaned_data.get("amount")

	def clean_subscriber_pincode(self):
		#print("clean_pincode")
		if self.cleaned_data.get("subscriber_pincode") < 100000 or self.cleaned_data.get("subscriber_pincode") > 999999 : #India uses 6 digit pincodes
			raise forms.ValidationError("Invalid Indian Pincode")
		else:
			return self.cleaned_data.get("subscriber_pincode")

	def clean_subscriber_mobile_number(self):
		#print("clean_subscriber_mobile_number")
		#print(self.cleaned_data.get("subscriber_mobile_number")/1000000000)
		if self.cleaned_data.get("subscriber_mobile_number")/1000000000 < 1:	#Assuming 10 digit mobile numbers
			raise forms.ValidationError("Invalid Mobile Number")
		else:
			return self.cleaned_data.get("subscriber_mobile_number")

	def clean_subscription_end_date(self):
		#print("clean_subscription_end_date")
		if self.cleaned_data.get("subscription_start_date") < date.today():
			raise forms.ValidationError("Invalid Subscription Start Date")
		elif self.cleaned_data.get("subscription_start_date") > self.cleaned_data.get("subscription_end_date"):
			raise forms.ValidationError("Invalid Subscription Dates")
		else:
			return self.cleaned_data.get("subscription_end_date")

class ExpiringMagazineSubscriptionForm(forms.Form):
	MAGAZINE_CHOICES = (('People\'s Demococracy' ,'People\'s Democracy'), ('India Today' , 'India Today'))

	magazine_name = forms.ChoiceField(label="Magazine", choices=MAGAZINE_CHOICES)
	subscription_end_date = forms.DateField(label="Subscription end date", widget=SelectDateWidget)

	class Meta:
		fields = ['magazine_name' , 'subscription_end_date']