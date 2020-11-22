from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth.forms import AuthenticationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    error_css_class = "error"
        
      
    #override
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        #Custom classok
        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['email'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'

        #Custom label
        self.fields['username'].label = ""
        self.fields['email'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""

        #Custom placeholder
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        
        
        
        #Help text off
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



class UserLoginForm(AuthenticationForm):
    error_css_class = "error"
    def __init__(self,*args,**kwargs):
        super(UserLoginForm, self).__init__(*args,**kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input','placeholder': 'Username','label':''}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input','placeholder': 'Password','label':''}
    ))