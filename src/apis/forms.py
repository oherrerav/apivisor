from django import forms
from datetime import date
from django.db.models import Q
from django.contrib.auth.models import User

from .models import Event, EventDate
from .models import Chart, DashBoard
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
class DashBoardAdminForm(forms.ModelForm):
	class Meta:
		model = DashBoard
		fields = '__all__'

	def __init__(self,*args, **kwargs):
		super(DashBoardAdminForm, self).__init__(*args, **kwargs)
		user = self.current_user
		if 'charts' in self.initial:
			self.fields['charts'].queryset = Chart.objects.filter(Q(pk__in=self.initial['charts']))
		else:
			self.fields['charts'].queryset = Chart.objects.filter(user=User.objects.filter(pk = user.id))

class EventAdminForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(EventAdminForm, self).__init__(*args, **kwargs)
		if 'event_dates' in self.initial:
			self.fields['event_dates'].queryset = EventDate.objects.filter(Q(pk__in=self.initial['event_dates']) | Q(event_date__gte=date.today()))
		else:
			self.fields['event_dates'].queryset = EventDate.objects.all()
