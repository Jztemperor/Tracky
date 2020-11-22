from django.forms import ModelForm
from users.models import Profile
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class WeightForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['weight','height']
    
    def __init__(self, *args, **kwargs):
        super(WeightForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'anyad'

        self.fields['weight'].widget.attrs['placeholder'] = 'Your Weight'
        self.fields['height'].widget.attrs['placeholder'] = 'Your Height'
        
       
    
       

