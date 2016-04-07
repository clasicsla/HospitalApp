from django.forms import ModelForm
from django import forms
from .models import Users

class UserForm(ModelForm):
	birth_date = forms.DateField(widget=forms.SelectDateWidget(years = (1990,1991)))
	class Meta:
		model = Users
		fields = ['name', 'birth_date', 'age', 'address']#, 'address'