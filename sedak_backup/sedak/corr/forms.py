
from django import forms
    
from tempus_dominus.widgets import DatePicker
    
from .models import *
    
    
class CorrespondentCreateForm(forms.ModelForm):
    class Meta:
        model = Correspondent
        fields = ('kod', 'full_name', 'short_name', 'add_country', 'add_index', 'add_region','add_district', 'add_city_type', 'add_city', 'add_street_type', 'add_street', 'add_building', 'add_corps', 'add_office',)
    
        widgets = {
            'kod': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}) ,
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'add_country': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_index': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_region': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'add_district': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_city_type': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'add_city': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Назва населенного пункту'}), 
            'add_street_type': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'add_street': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Назва вулиці'}), 
            'add_building': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}), 
            'add_corps': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}), 
            'add_office': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}),
        }
    

class CorrespondentUpdateForm(forms.ModelForm):
    class Meta:
        model = Correspondent
        fields = ('kod', 'full_name', 'short_name', 'add_country', 'add_index', 'add_region','add_district', 'add_city_type', 'add_city', 'add_street_type', 'add_street', 'add_building', 'add_corps', 'add_office',)
    
        widgets = {
            'kod': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}) ,
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'add_country': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_index': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_region': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'add_district': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'add_city_type': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'add_city': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Назва населенного пункту'}), 
            'add_street_type': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'add_street': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Назва вулиці'}), 
            'add_building': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}), 
            'add_corps': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}), 
            'add_office': forms.TextInput(attrs={'class': 'form-control form-control-sm wid-75'}),
        }
    
    
class LetterTypeCreateForm(forms.ModelForm):
    class Meta:
        model = LetterType
        fields = ('title',)
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
        }
    

class LetterTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = LetterType
        fields = ('title',)
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
        }
    

class LetterSummaryCreateForm(forms.ModelForm):
    class Meta:
        model = LetterSummary
        fields = ('title',)
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
        }
    

class LetterSummaryUpdateForm(forms.ModelForm):
    class Meta:
        model = LetterSummary
        fields = ('title',)
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
        }
    

class InсorrCreateForm(forms.ModelForm):
    class Meta:
        model = Inсorr
        fields = ('incorr_date', 'incorr_num', 'correspondent', 'corr_datenum', 'debtor', 'letter_type', 'executed', 'letter_scan',)
    
        widgets = {
            'incorr_date': forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
            'incorr_num': forms.TextInput(attrs={'class': 'form-control form-control-sm'}) ,
            'correspondent': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'corr_datenum': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'debtor': forms.Select(attrs={'class': 'form-control form-control-sm'}), 
            'letter_type': forms.Select(attrs={'class': 'form-control form-control-sm'}), 
            'executed': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'letter_scan': forms.FileInput(),
        }
    
    
class InсorrUpdateForm(forms.ModelForm):
    class Meta:
        model = Inсorr
        fields = ('incorr_date', 'incorr_num', 'correspondent', 'corr_datenum', 'debtor', 'letter_type', 'executed', 'letter_scan',)
    
        widgets = {
            'incorr_date': forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
            'incorr_num': forms.TextInput(attrs={'class': 'form-control form-control-sm'}) ,
            'correspondent': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'corr_datenum': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            'debtor': forms.Select(attrs={'class': 'form-control form-control-sm'}), 
            'letter_type': forms.Select(attrs={'class': 'form-control form-control-sm'}), 
            'executed': forms.TextInput(attrs={'class': 'form-control form-control-sm'}), 
            # 'letter_scan': forms.FileInput(),
        }
    

class OutсorrCreateForm(forms.ModelForm):
    class Meta:
        model = Outсorr
        fields = ('outcorr_date', 'outcorr_num', 'correspondent', 'letter_type', 'letter_summary', 'debtor', 'letter_doc','letter_scan', 'check_scan', 'check_amount',)
    
        widgets = {
            'outcorr_date': forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
            'outcorr_num': forms.TextInput(attrs={'class': 'form-control form-control-sm'}) ,
            'correspondent': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'letter_type': forms.Select(attrs={'class': 'form-control form-control-sm'}), 
            'letter_summary': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'debtor': forms.Select(attrs={'class': 'form-control form-control-sm'}), 
            'check_amount': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'letter_doc': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
            'letter_scan': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
            'check_scan': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
        }
    
    
class OutсorrUpdateForm(forms.ModelForm):
    class Meta:
        model = Outсorr
        fields = ('outcorr_date', 'outcorr_num', 'correspondent', 'letter_type', 'letter_summary', 'debtor', 'letter_doc','letter_scan', 'check_scan', 'check_amount',)

        widgets = {
            'outcorr_date': forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
            'outcorr_num': forms.TextInput(attrs={'class': 'form-control form-control-sm'}) ,
            'correspondent': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'letter_type': forms.Select(attrs={'class': 'form-control form-control-sm'}), 
            'letter_summary': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'debtor': forms.Select(attrs={'class': 'form-control form-control-sm'}), 
            'check_amount': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'letter_doc': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
            'letter_scan': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
            'check_scan': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
        }
