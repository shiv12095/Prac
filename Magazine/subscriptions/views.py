from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from subscriptions.forms import MagazineSubscriptionForm
from subscriptions.models import MagazineSubscription
from datetime import date, timedelta

@login_required
def index(request):
	return render(request, 'subscriptions/index.html')

@login_required
def view(request, subscription_id):
	#print("view")
	#print subscription_id
	context_dict={}	
	try:
		subscription = MagazineSubscription.objects.get(subscription_id=subscription_id)
		context_dict["subscription"] = subscription
		context_dict["subscription_expiring"] = subscription_expiring(subscription)
		#print("subscription found")
	except MagazineSubscription.DoesNotExist:
		return redirect('index')
	return render(request, 'subscriptions/view.html', context_dict)

def subscription_expiring(subscription):
	expiry_date = date.today() + timedelta(days=8)	#1 week notice before expiry
	print expiry_date
	if subscription.subscription_end_date < expiry_date:
		#print("expiring")
		return "expiring"
	elif subscription.subscription_end_date < date.today():
		#print("expiring")
		return "expired"
	else:
		#print("valid")
		return "valid"

@login_required
def expiring(request):
	expiry_date = date.today() + timedelta(days=8)	#1 week notice before expiry
	try:
		expiring_subscriptions = MagazineSubscription.objects.filter(subscription_end_date__lt=expiry_date)
		#print expiring_subscriptions
		return render(request, 'subscriptions/expiring.html', {'expiring_subscriptions':expiring_subscriptions})
	except MagazineSubscription.DoesNotExist:
		return render(request, 'subscriptions/expiring.html')

@login_required
def new(request):
	if(request.method=='POST'):
		form = MagazineSubscriptionForm(request.POST)
		if form.is_valid():
			user = request.user
			subscription = form.save(commit=False)
			subscription.user_id = user
			subscription_id = generate_subscription_id(request)
			subscription.subscriber_address = get_address(request)
			subscription.subscription_id = subscription_id
			subscription.subscriber_state = request.POST["subscriber_state"]
			subscription.subscriber_pincode = request.POST["subscriber_pincode"]
			subscription.save()
			return redirect(view, subscription_id=subscription_id)
		else:
			print form.errors
	else:
		form = MagazineSubscriptionForm()
	return render(request, 'subscriptions/new.html' , {'form': form})

def get_address(request):
	address = request.POST["subscriber_address"] + " " + request.POST["subscriber_address_1"] + " " + request.POST["subscriber_address_2"] + " " + get_state(request) + " " + request.POST["subscriber_pincode"]
	return address

def generate_subscription_id(request):
	state_code = request.POST["subscriber_state"]
	#print("generate_subscription_id")
	#print state_code
	count = MagazineSubscription.objects.filter(subscriber_state=state_code).count() + 1
	#print count
	subscription_id = state_code + str(count)
	return subscription_id

def get_state(request):
	STATE_CHOICES = {
		'AP':'Andhra Pradesh','AR':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CT':'Chhattisgarh',
		'GA':'Goa','GJ':'Gujrat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand',
		'KA':'Karnataka','KL':'Kerala','MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya',
		'MZ':'Mizoram','OR':'Odisha','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim','TN':'Tamil Nadu','TG':'Telangana',
		'TR':'Tripura','UP':'Uttar Pradesh','UT':'Uttrakhand','WB':'West Bengal','AN':'Andaman and Nicobar Islands',
		'CN':'Chandigarh','DN':'Dadra and Nagar Haveli','DD': 'Daman and Diu','LD':'Lakshadweep',
		'DL':'National Capital Territory of India','PY':'Puducherry'
	}
	return STATE_CHOICES[request.POST["subscriber_state"]]