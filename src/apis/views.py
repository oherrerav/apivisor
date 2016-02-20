from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Api, DashBoard, Chart, ChartType
from django.core import serializers

from .forms import ApiAdminForm, ChartAdminForm, DashBoardAdminForm

# Create your views here.
def home(request):
	title = 'Welcome'
	# if request.user.is_authenticated():
	# 	title = "My user is: %s " %(request.user)
	# add a from
	# form = SignUpForm(request.POST or None)
	apis = Api.objects.filter(user=request.user)
	chartTypes = ChartType.objects.filter()
	charts = Chart.objects.filter(user=request.user)
	dashboards = DashBoard.objects.filter(user=request.user)

	

	# dashboards = DashBoard
	context = {
	'apis': apis,
	'dashboards': dashboards,
	'chartTypes': chartTypes,
	'charts': charts
	 }
	# context = {
	#    "title": title,
	#    "form": form	} 


	# if form.is_valid():
	# 	form.save()
	# 	# instance = form.save(commit=False)
	# 	# instance.save()
	# 	# from_email = settings.EMAIL_HOST_USER,
	# 	send_mail('Subject here', 'Here is the message. 2.','oherrerav@gmail.com', 
 #    ['oherrerav@gmail.com'], fail_silently=False)
	# 	context = {"title":"Thank you"}

	return render(request,"home.html",context)
	# return HttpResponse("<h1>Hello!Home</h1>")

# def api_home(request):
# 	return HttpResponse("<h1>Hello!</h1>")
def settings(request):
# add a from
	form = None
	model = None
	context = {}
	action = request.GET.get('action')
	if action == "postChart":
		form = ChartAdminForm(request.POST or None, user=request.user)
		context = {
	   "form": form	} 
	elif  action == "getChart": 
		model = serializers.serialize( 'python',
			   							Chart.objects.filter(user=request.user), 
			   							fields=('name', 'chartType', 'apis', 'size', 'status'),
			   							use_natural_foreign_keys=True 
			   						)
		# model = Chart.objects.filter(user=request.user)
		context = {'model': model}
	elif action == "postApi":
		form = ApiAdminForm(request.POST or None)
		context = {
	   "form": form	} 
	elif action == "postDashBoard":
		form = DashBoardAdminForm(request.POST or None, user=request.user)
		context = {
	   "form": form	} 

		# instance = form.save(commit=False)
	# 	# instance.save()
	# 	# from_email = settings.EMAIL_HOST_USER,
	# 	send_mail('Subject here', 'Here is the message. 2.','oherrerav@gmail.com', 
 #    ['oherrerav@gmail.com'], fail_silently=False)
	# 	context = {"title":"Thank you"}

	return render(request,"settings.html",context)
	# return HttpResponse("<h1>Hello!Home</h1>")

# def api_home(request):
# 	return HttpResponse("<h1>Hello!</h1>")
