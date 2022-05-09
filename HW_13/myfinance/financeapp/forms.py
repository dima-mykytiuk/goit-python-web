from django import forms
from .models import Category


class OutcomeForm(forms.Form):
    sum = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'special'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'category_select'}))
    
    
class IncomeForm(forms.Form):
    sum = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'special'}))
    
    
class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'category_name'}))


class DateSliceForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'dateslice'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'dateslice'}))