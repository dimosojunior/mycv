from DimosoApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):

    
    
    

    class Meta:
        model = Contact
        fields = [
			"email",
            
			"username",
			"phone",
			"place",
			"body"
			

        ]