# импорт стандартных библиотек:
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
    
# импорт сторонних библиотек:
    
# импорт модулей текущего проекта:
from .models import *
    
    
class LetterTypeAdminForm(forms.ModelForm):
    class Meta:
        model = LetterType
        fields = '__all__'
    
    
class LetterSummaryAdminForm(forms.ModelForm):
    class Meta:
        model = LetterSummary
        fields = '__all__'
    
    
class CorrespondentAdminForm(forms.ModelForm):
    class Meta:
        model = Correspondent
        fields = '__all__'
    
    
class IncorrAdminForm(forms.ModelForm):
    class Meta:
        model = Inсorr
        fields = '__all__'
    
    
class OutcorrAdminForm(forms.ModelForm):
    class Meta:
        model = Outсorr
        fields = '__all__'
    
    
class LetterTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} 
    form = LetterTypeAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',) 
    search_fields = ('title',)
    list_filter = ('title',)
    fields = ('user', 'title', 'slug',)

class LetterSummaryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} 
    form = LetterSummaryAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',) 
    search_fields = ('title',)
    list_filter = ('title',)
    fields = ('user', 'title', 'slug',)
    
    
class CorrespondentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("short_name",)} 
    form = CorrespondentAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'kod', 'short_name')
    list_display_links = ('id', 'short_name',) 
    search_fields = ('short_name',)
    list_filter = ('short_name',)
    readonly_fields = ('create_time', 'update_time')
    fields = ('user', 'kod', 'full_name', 'short_name', 'add_country', 'add_index', 'add_region', 'add_district', 'add_city_type', 'add_city', 'add_street_type', 'add_street', 'add_building', 'add_corps', 'add_office', 'slug', 'create_time', 'update_time',)
    

class IncorrAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("incorr_num",)}  # автозаполнения поля слаг на основе короткого названия
    form = IncorrAdminForm
    save_as = True  # сохранение объекта как нового
    save_on_top = True  # набор кнопок сверхуб, чтобы не листать вниз
    # отображение полей модели в админке:
    list_display = ('id', 'incorr_date', 'incorr_num', 'correspondent', 'debtor', 'letter_type',)
    list_display_links = ('id', 'incorr_num',) 
    search_fields = ('incorr_num',)
    list_filter = ('incorr_num',)
    readonly_fields = ('create_time', 'update_time')  # поля только для чтения
    # Отображение полей внутри записи:
    fields = ('user', 'incorr_date', 'incorr_num', 'correspondent', 'corr_date', 'corr_datenum', 'corr_num', 'debtor', 'letter_type', 'executed', 'doc_scan', 'slug', 'create_time', 'update_time',)
    
    
class OutcorrAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('outcorr_date', 'outcorr_num',)} 
    form = OutcorrAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'outcorr_date', 'outcorr_num', 'correspondent', 'letter_type', 'debtor',)
    list_display_links = ('id', 'outcorr_num',) 
    search_fields = ('outcorr_num',)
    list_filter = ('outcorr_num',)
    readonly_fields = ('create_time', 'update_time',)
    fields = ('user', 'outcorr_date', 'outcorr_num', 'correspondent', 'letter_type', 'letter_summary', 'debtor', 'letter_scan', 'check_scan', 'check_amount', 'slug', 'create_time', 'update_time',)
    
    
admin.site.register(LetterType, LetterTypeAdmin)
admin.site.register(LetterSummary, LetterSummaryAdmin)
admin.site.register(Correspondent, CorrespondentAdmin)
admin.site.register(Inсorr, IncorrAdmin)
admin.site.register(Outсorr, OutcorrAdmin)
