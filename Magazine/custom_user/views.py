from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout , authenticate
from django.contrib.auth.decorators import login_required
from custom_user.backends import AuthUserBackend
from custom_user.models import AuthUser, AuthUserManager
from custom_user.forms import AuthUserCreationForm, AuthUserAuthenticationForm

def index(request):
	return render(request , 'custom_user/index.html')

def signup(request):
	if request.method == 'POST':
		form = AuthUserCreationForm(request.POST)
		#print("form object created")
		if form.is_valid():
			form.save(commit=True)			
			return redirect('login')
		else:
			print form.errors
	else:
		form = AuthUserCreationForm()
	return render(request, 'custom_user/signup.html' , {'form': form})

def login(request):
	if request.method == 'POST':
		form = AuthUserAuthenticationForm(data=request.POST)
		if form.is_valid():
			user = authenticate(email=request.POST['email'] , password=request.POST['password'])
			if user is not None:
				#print("user present")
				django_login(request, user)
				return redirect('profile')
			else:
				print("user absent")
	else:
		form = AuthUserAuthenticationForm()
	return render(request, 'custom_user/login.html', {'form': form})
def logout(request):
	print("logout")
	print(request.user)
	django_logout(request)
	print("user logged out")
	return redirect('login')

@login_required
def profile(request):
	#print("profile")
	#print(request.user)
	return render(request, 'custom_user/profile.html')
