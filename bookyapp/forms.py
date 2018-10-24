from .models import Book,Ride
from django import forms
#......
class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class NewRideForm(forms.ModelForm):
    class Meta:
        model = Ride
        exclude = ['user','project']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
