from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from custom_user.models import AuthUser, AuthUserManager
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class AuthUserCreationForm(forms.ModelForm):
	year = date.today().year
	GENDER_CHOICES=(('M','Male'),('F','Female'))

	first_name = forms.CharField(label="First name", max_length=30, required=True)
	last_name = forms.CharField(label="Last name", max_length=30, required=True)
	gender = forms.ChoiceField(label="Gender", widget=forms.RadioSelect, choices=GENDER_CHOICES, initial='M')
	date_of_birth = forms.DateField(label="Date of Birth", widget=SelectDateWidget(years=range(year-18,year-80,-1)))
#	date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y',))
	email = forms.EmailField(label="Email Id", max_length=255, required=True)
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = AuthUser
		fields = ('first_name','last_name', 'gender' ,'date_of_birth', 'email')

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		#print("verifying passwords")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		user = super(AuthUserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			#print("saving user")
			user.save()
		return user

class AuthUserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = AuthUser
		fields = ('email' , 'first_name' , 'last_name' , 'date_of_birth' , 'is_active')

	def clean_password(self):
		return self.initial["password"]

class AuthUserAuthenticationForm(forms.Form):
	email = forms.EmailField(label="Email Id", max_length=255, required=True)
	password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

	class Meta:
		fields = ['email' , 'password']
	
	def clean_email(self):
		print(self)
		try:
			user = AuthUser.objects.get(email=self.cleaned_data.get("email"))
		except AuthUser.DoesNotExist:
			raise forms.ValidationError("Invalid Email Id or Password")
		return self.cleaned_data.get("email")
