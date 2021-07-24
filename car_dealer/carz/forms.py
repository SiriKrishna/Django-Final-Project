#from django.forms import ModelForm
from carz.models import Car,User,Rolereq
from django import forms
#from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class CarForm(forms.ModelForm):
	class Meta:
		model = Car
		fields = ["carname","carprice","carmodel","purchased_year","carfuel","carseats","carkms","carimg"]
		widgets = {
		"carname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Car Name",
			}),
		"carprice":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Car Price",
			}),
		"carmodel":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select Model",
			}),
		"purchased_year":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Manufactured Year",
			}),
        "carfuel":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select Fuel",
			}), 
        "carseats":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter No.of Seats",
		
			}),
        "carkms":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter No.of KMS driven",
			
			}),
		"carimg":forms.FileInput(attrs={
			
			
			}),		          
		}
class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		}

class Rltype(forms.ModelForm):
	class Meta:
		model = Rolereq
		fields = ["uname","rltype","pfe"]
		widgets = {
		"rltype":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Rlupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","role"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Pfupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","age","mobilenumber","uimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Email",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Age",
			}),
		"mobilenumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Mobile Number",
			}),
		}

class Chgepwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Old Password"
		}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Password",
		}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["old_password","new_password1","new_password2"]		