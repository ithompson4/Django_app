from django import forms
from django.forms import ModelForm
from .models import Snake
from .models import Scientist 

class SnakeForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    color = forms.CharField(
        label='Color or Pattern',
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Snake
        fields = ['name', 'description', 'color', 'prey', 'region', 'venomous']
        form_classes = {'class': 'form-control'}
        widgets = {
            'description': forms.TextInput(attrs=form_classes),
            'prey': forms.TextInput(attrs=form_classes),
            'region': forms.TextInput(attrs=form_classes),
            'venomous': forms.TextInput(attrs=form_classes)
        }
        
class LoginForm(forms.ModelForm):
    email = forms.CharField(
        label='Email',
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Scientist
        fields =['email','password']
        form_classes = {'class': 'form-control'}
        widgets = {
            'password': forms.PasswordInput(attrs=form_classes)
        } 
        
class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        label='First Name',
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Last Name',
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Scientist
        fields =['first_name','last_name','email','password'] 
        form_classes = {'class': 'form-control'}
        widgets = {
            'email': forms.TextInput(attrs=form_classes),
            'password': forms.PasswordInput(attrs=form_classes)
        }         
        

