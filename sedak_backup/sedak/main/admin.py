from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class DebtorAdminForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = '__all__'

class DebtorAdmin(admin.ModelAdmin):
    # автозаполнения поля слаг на основе короткого названия:
    prepopulated_fields = {"slug": ("short_name",)} 
    form = DebtorAdminForm
    
    # сохранение объекта как нового:
    save_as = True
    
    # набор кнопок сверхуб, чтобы не листать вниз:
    save_on_top = True
    
    # отображение полей модели в админке:
    list_display = ('id', 'short_name', 'case_num', 'create_time',)  
    list_display_links = ('id', 'short_name',) 
    search_fields = ('short_name',)
    list_filter = ('nomenclature_num', 'short_name',)
    # поля только для чтения:
    readonly_fields = ('create_time', 'update_time')
    
    # Отображение полей внутри записи:
    fields = ('user', 'kod', 'full_name', 'short_name', 'slug', 'case_num', 'nomenclature_num', 'add_country', 'add_index', 'add_region', 'add_district', 'add_city_type', 'add_city', 'add_street_type', 'add_street', 'add_building', 'add_office', 'create_time', 'update_time',)

admin.site.register(Debtor,DebtorAdmin)
