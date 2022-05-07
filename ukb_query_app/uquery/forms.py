from django import forms
from django.forms import IntegerField, ModelForm
from . models import Field

#Create a venue form
class FieldForm(ModelForm):
    class Meta:
        model = Field
        fields = ('field_num','instance_id')
        labels = {
            'field_num': '',
            'instance_id': '',
            
        }
        widgets ={
            'field_num': forms.TextInput(attrs={'class':'form-control','placeholder':'Field Number'}),
            'instance_id': forms.TextInput(attrs={'class':'form-control','placeholder':'Assessment Visit Number'}),

        }