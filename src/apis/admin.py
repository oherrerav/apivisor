from django.contrib import admin

# Register your models here.
from .models import Api
from .models import ChartVisualization
from .models import ChartType
from .models import Chart
from .models import DashBoard
# from .models import SignUp

# from .forms import SignUpForm

class ApiModelAdmin(admin.ModelAdmin):
	list_display = ["name","uri"]
	# list_display_links =["uri"]
	# list_filter =["name"]
	list_editable = ["uri"]
	search_fields = ["name","uri"]
	class Meta:
		model = Api

# class SignUpAdmin(admin.ModelAdmin):
# 	list_display = ["email","full_name","updated"]
# 	form = SignUpForm
# 	class Meta:
# 		model = SignUp


admin.site.register(Api,ApiModelAdmin)
# admin.site.register(SignUp,SignUpAdmin)
admin.site.register(ChartVisualization)
admin.site.register(ChartType)
admin.site.register(Chart)
admin.site.register(DashBoard)