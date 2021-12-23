
from django import forms

from .models import Debtor



class DebtorCreateForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = ('kod', 'full_name', 'short_name', 'case_num', 'nomenclature_num', 'add_country', 'add_index', 'add_region','add_district', 'add_city_type', 'add_city', 'add_street_type', 'add_street', 'add_building', 'add_corps', 'add_office')

        widgets = {
            'kod': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}) ,
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'case_num': forms.TextInput(attrs={'class': 'form-control'}), 
            'nomenclature_num': forms.TextInput(attrs={'class': 'form-control'}), 
            'add_country': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_index': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_region': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'add_district': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_city': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Назва населенного пункту'}), 
            'add_street': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Назва вулиці'}), 
            'add_building': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}), 
            'add_corps': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}), 
            'add_office': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}),
        }


class DebtorUpdateForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = ('kod', 'full_name', 'short_name', 'case_num', 'nomenclature_num', 'add_country', 'add_index', 'add_region','add_district', 'add_city_type', 'add_city', 'add_street_type', 'add_street', 'add_building', 'add_corps', 'add_office')

        widgets = {
            'kod': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}) ,
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'case_num': forms.TextInput(attrs={'class': 'form-control'}), 
            'nomenclature_num': forms.TextInput(attrs={'class': 'form-control'}), 
            'add_country': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_index': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_region': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'add_district': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_city': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_street': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_building': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}), 
            'add_corps': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}), 
            'add_office': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}),
        }
