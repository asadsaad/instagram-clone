from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class RegistrationForm(UserCreationForm):
		password1=forms.CharField(label="Password1",widget=forms.PasswordInput(attrs={}))
		password2=forms.CharField(label="Password2",widget=forms.PasswordInput(attrs={}))
		username=forms.CharField(label="Username",widget=forms.TextInput(attrs={}))

		class Meta:
			model=User
			fields=('username',
			'email',
			'first_name',
			'last_name',
			'password1',
			'password2',)

class ChangeForm(UserChangeForm):
	# password=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'hidden'}))
	class Meta:
			model=User
			fields=('username',
			'email',
			'first_name',
			'last_name',
			'password',	)		