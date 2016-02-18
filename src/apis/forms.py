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
		exclude = ['user',]

class ChartAdminForm(forms.ModelForm):
	class Meta:
		model = Chart
		fields = '__all__'
		exclude = ['user',]

	def __init__(self,*args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(ChartAdminForm, self).__init__(*args, **kwargs)
		if self.user:
			self.fields['apis'].queryset = Api.objects.filter(user=User.objects.filter(pk = self.user.id))
		else:
			user = self.current_user
			self.fields['apis'].queryset = Api.objects.filter(user=User.objects.filter(pk = user.id))

class DashBoardAdminForm(forms.ModelForm):
	class Meta:	
		model = DashBoard
		fields = '__all__'
		exclude = ['user',]

	def __init__(self,*args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(DashBoardAdminForm, self).__init__(*args, **kwargs)
		if 'charts' in self.initial:
			self.fields['charts'].queryset = Chart.objects.filter(Q(pk__in=self.initial['charts']))
		else:
			if self.user:
				self.fields['charts'].queryset = Chart.objects.filter(user=User.objects.filter(pk = self.user.id))
			else:
				user = self.current_user
				self.fields['charts'].queryset = Chart.objects.filter(user=User.objects.filter(pk = user.id))