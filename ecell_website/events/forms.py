from django import forms
from django.forms import ModelForm
from .models import Friend_users

CHOICES = [('1', 'Male'), ('2', 'Female')]

class Friend_Form(ModelForm):
    class Meta:
        model = Friend_users
        fields = ('first_name','last_name','birthdate','gender','emailid','phone','address','pincode')
        widgets={
		#'gender':forms.RadioSelect(choices=CHOICES),
        }


