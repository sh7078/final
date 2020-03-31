from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User,Customer,Restaurant,Item,Menu,Restaurant1

class CustomerSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self, commit=True):
			user = save(commit=False)
			user.is_customer=True
			if commit:
				user.save()
			return user


class RestuarantSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model =User
		fields=['username','email','password']
		def save(self,commit=True):
			user=save(commit=False)
			user.is_restaurant=True
			if commit:
				user.save()
			return user


class Restuarant1SignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model =User
		fields=['username','email','password']
		def save(self,commit=True):
			user=save(commit=False)
			
			if commit:
				user.save()
			return user			

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields =['f_name','l_name','city','phone','address']


class RestuarantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields =['rname','info','location','r_logo','min_ord','status','approved']


class Restuarant1Form(forms.ModelForm):
	class Meta:
		model = Restaurant1
		fields =['rname','info','location','r_logo','min_ord','status','approved']




		
		

			




		
		


