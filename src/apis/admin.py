from django.contrib import admin

# Register your models here.
from .models import Api
from .forms import SignUpForm
from .models import SignUp

class ApiModelAdmin(admin.ModelAdmin):
	list_display = ["name","uri"]
	# list_display_links =["uri"]
	# list_filter =["name"]
	list_editable = ["uri"]
	search_fields = ["name","uri"]
	class Meta:
		model = Api

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["email","full_name","updated"]
	form = SignUpForm
	class Meta:
		model = SignUp


admin.site.register(Api,ApiModelAdmin)
admin.site.register(SignUp,SignUpAdmin)