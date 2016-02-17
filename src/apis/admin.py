from django.contrib import admin

# Register your models here.
from .models import Api
from .models import ChartVisualization
from .models import ChartType
from .models import DashBoard
from .models import Chart
# from .models import SignUp

# from .forms import SignUpForm
from .forms import DashBoardAdminForm

class DashBoardAdmin(admin.ModelAdmin):
	form = DashBoardAdminForm
	filter_horizontal = ['charts']
	
	def get_form(self, request, obj=None,**kwargs):
		form = super(DashBoardAdmin, self).get_form(request,obj, **kwargs)
		form.current_user = request.user
		return form

	# def get_queryset(self, request):
	# 	 qs = super(DashBoardAdmin, self).get_queryset(request)
	# 	 if request.user.is_superuser:
	# 		 return qs
	# 	 return qs.filter(user=request.user)

class ChartAdmin(admin.ModelAdmin):
	 def get_queryset(self, request):
		 qs = super(ChartAdmin, self).get_queryset(request)
		 if request.user.is_superuser:
			 return qs
		 return qs.filter(user=request.user)


class ApiAdmin(admin.ModelAdmin):
	list_display = ["name","uri"]
	# list_display_links =["uri"]
	# list_filter =["name"]
	list_editable = ["uri"]
	# search_fields = ["name","uri"]
	# class Meta:
	#   model = Api
	def get_queryset(self, request):
		 qs = super(ApiAdmin, self).get_queryset(request)
		 if request.user.is_superuser:
			 return qs
		 return qs.filter(user=request.user)

# class SignUpAdmin(admin.ModelAdmin):
#   list_display = ["email","full_name","updated"]
#   form = SignUpForm
#   class Meta:
#       model = SignUp
# class ChartInline(admin.TabularInline):
#   model = DashBoard.charts.through

	 #   qs = super(DashBoard, self).get_queryset(request)
		# return qs.filter(user=request.user)

	# class Meta:
	#   model = DashBoard
		# .objects.filter(tag__name="DataWipTable")


# class MyModelAdmin(admin.ModelAdmin):
#   def get_queryset(self, request):
#       qs = super(MyModelAdmin, self).get_queryset(request)
#       if request.user.is_superuser:
#           return qs
#       return qs.filter(author=request.user)

admin.site.register(Api,ApiAdmin)
# admin.site.register(SignUp,SignUpAdmin)
admin.site.register(ChartVisualization)
admin.site.register(ChartType)
admin.site.register(DashBoard,DashBoardAdmin)
admin.site.register(Chart,ChartAdmin)


