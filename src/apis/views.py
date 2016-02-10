from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Api, DashBoard, Chart, ChartType

# from .forms import SignUpForm

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
