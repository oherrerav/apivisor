from django.http import HttpResponse
from django.shortcuts import render

from .forms import SignUpForm

# Create your views here.
def home(request):
	title = 'Welcome'
	# if request.user.is_authenticated():
	# 	title = "My user is: %s " %(request.user)
	# add a from
	form = SignUpForm(request.POST or None)

	context = {
	   "title": title,
	   "form": form	} 


	if form.is_valid():
		form.save()
		# instance = form.save(commit=False)
		# instance.save()
		context = {"title":"Thank you"}

	return render(request,"home.html",context)
	# return HttpResponse("<h1>Hello!Home</h1>")

# def api_home(request):
# 	return HttpResponse("<h1>Hello!</h1>")
