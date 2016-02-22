from django import forms
from datetime import date
from django.db.models import Q
from django.contrib.auth.models import User

from .models import Api, Chart, DashBoard
# from .models import SignUp
# from .models import Chart,ChartByUser

# class SignUpForm(forms.ModelForm):
# 	"""docstring for SignUP"""
# 	class Meta:
# 		model = SignUp
# 		fields = ['full_name','email']

# class ChartByUserAdminForm(forms.ModelForm):
# 	class Meta:
# 		model = ChartByUser

# 	def __init__(self, *args, **kwargs):
# 		super(ChartByUserAdminForm, self).__init__(*args, **kwargs)
# 		# if 'user_charts' in self.initial:
# 		#     self.fields['chart'].queryset = Chart.objects.filter(Q(pk__in=self.initial['user_charts']) | Q(event_date__gte=date.today()))
# 		# else:
# 		self.fields['chart'].queryset = Chart.objects.filter(user='pk')

class ApiAdminForm(forms.ModelForm):
	class Meta:
		model = Api
		fields = '__all__'
		exclude = []

	def __init__(self,*args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(ApiAdminForm, self).__init__(*args, **kwargs)

		meta = getattr(self, 'Meta', None)
		exclude = getattr(meta, 'exclude', [])

		if (not  self.current_user_is_superuser):					
			exclude.append('user',)

class ChartAdminForm(forms.ModelForm):
	class Meta:
		model = Chart
		fields = '__all__'
		exclude = []

	def __init__(self,*args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(ChartAdminForm, self).__init__(*args, **kwargs)

		meta = getattr(self, 'Meta', None)
		exclude = getattr(meta, 'exclude', [])

		if (not self.current_user_is_superuser):					
			exclude.append('user',)

		if self.user:
			self.fields['apis'].queryset = Api.objects.filter(user=User.objects.filter(pk = self.user.id))
		else:
			user = self.current_user
			self.fields['apis'].queryset = Api.objects.filter(user=User.objects.filter(pk = user.id))

class DashBoardAdminForm(forms.ModelForm):
	class Meta:	
		model = DashBoard
		fields = '__all__'
		exclude = []

	# def get_form(self, request, obj=None, **kwargs):
	# 	self.exclude = ['user',]
	# 	# if self.current_user.is_superuser:
	# 	return form

	def __init__(self,*args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(DashBoardAdminForm, self).__init__(*args, **kwargs)
		# form =  super(DashBoardAdminForm, self).get_form(request,obj, **kwargs)
		# super(form, self).__init__(*args, **kwargs)
		# del self.fields['name']
		meta = getattr(self, 'Meta', None)
		exclude = getattr(meta, 'exclude', [])

		if (not  self.current_user_is_superuser):					
			exclude.append('user',)

		# exclude.append('user',)
		# for user in exclude:
		# 	if user in self.fields:
		# 		# self.exclude.pop('user')
		# 		del self.fields[user]

				# if not self.is_superuser=='True':	

		if 'charts' in self.initial:
			self.fields['charts'].queryset = Chart.objects.filter(Q(pk__in=self.initial['charts']))
		else:
			if self.user:
				self.fields['charts'].queryset = Chart.objects.filter(user=User.objects.filter(pk = self.user.id))
				# self.exclude.append('user',)
				# self.exclude = ['user',]
			else:
				user = self.current_user
				# superu = self.is_superuser
				# exclude.append('user',)

				self.fields['charts'].queryset = Chart.objects.filter(user=User.objects.filter(pk = user.id))
				# # if not superu:
				# if  current_user_is_superuser== true:					
				# 	exclude.append('user',)
				# self.exclude = ['user',]
				# if not  user.is_staff:
				# 	del self.fields['user']
