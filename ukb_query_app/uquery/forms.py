from django import forms
from django.forms import ModelForm
from . models import Field

#Create a venue form
class FieldForm(ModelForm):
    class Meta:
        model = Field
        fields = ('field_id','instance_id','title','encoding_id')
        labels = {
            'field_id': '',
            'instance_id': '',
            'title': '',
            'encoding_id': '',
            'version': '',
            
        }
        widgets ={
            'field_id': forms.TextInput(attrs={'class':'form-control','placeholder':'Field Number'}),
            'instance_id': forms.TextInput(attrs={'class':'form-control','placeholder':'Assessment Visit Number'}),
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Field Title'}),
            'encoding_id': forms.TextInput(attrs={'class':'form-control','placeholder':'Encoding Number'}),
            'version': forms.TextInput(attrs={'class':'form-control','placeholder':'Data File Version'}),
    
        }