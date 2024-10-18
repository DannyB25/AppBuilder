from django import forms #imports forms module from Django, which provides necessary classes and methods to create forms
from .models import HappyPlace #imports HappyPlace model from models.py

class HappyPlaceForm(forms.ModelForm): #defines a new form class, which is a subclass of forms.ModelForm
    class Meta: #provides metadata to form, like which model the form is associated with and which fields to include in form
        model = HappyPlace #specifies the form is linked to HappyPlace model
        fields = '__all__' #lists fields from HappyPlace model to include in form, which users can input or edit
        labels = {
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'location': 'Location',
            'comments': 'Comments',
        }
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name Here'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name Here'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Happy Place Here'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Comments'}),
        }
