# импорт стандартных библиотек:
import uuid
import os
import datetime
from django.core import validators

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.core.files.storage import FileSystemStorage

from unidecode import unidecode

from main.models import Debtor
from account.models import CustomUser
    
    
def get_debtor_nomenclature(debtor):
        result = Debtor.objects.get(short_name=debtor)
        return result.nomenclature_num


def get_user_surname(user_id):
        result = CustomUser.objects.get(pk=user_id)
        return result.surname
    
    
def get_user_suffix(user_id):
        result = CustomUser.objects.get(pk=user_id)
        return "_".join([result.surname, str(result.pk)])
    

def incorr_directory(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4())[:13], ext)
    return '{0}/corr/in/{1}/{2}'.format(get_user_suffix(instance.user.id), instance.inncorr_date.strftime('%Y/%m'), filename)
    
    
def outcorr_directory(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4())[:13], ext)
    return '{0}/{1}/corr/out/pdf/{2}/{3}'.format(get_user_suffix(instance.user.id), get_debtor_nomenclature(instance.debtor), instance.outcorr_date.strftime('%Y/%m'), filename)
    
    
# fs = FileSystemStorage(location='/SEDAK/Листування/Вихідна')  сохранение не в медиа
# def outcorr_doc_directory(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (str(uuid.uuid4())[:8], ext)
#     return os.path.join('сезак/docx', filename)


def outcorr_doc_directory(instance, filename):
    def get_doc_type(doc_type):
        match doc_type:
            case "запит":
                return "запт"
            case "заява":
                return "заяв"
            case "лист":
                return "лист"
            case "апеляційна скарга":
                return "апск"
            case "касаційна скарга":
                return "касск"
    
    ext = filename.split('.')[-1]
    date_suffix = instance.outcorr_date.strftime("%Y.%m.%d")
    temp_filename = "_".join([date_suffix, get_doc_type(str(instance.letter_type).lower()), instance.correspondent])
    filename = "%s.%s" % (temp_filename, ext)
    return '{0}/{1}/corr/out/docx/{2}/{3}'.format(get_user_suffix(instance.user.id), get_debtor_nomenclature(instance.debtor), instance.outcorr_date.strftime('%Y'), filename)
    
    
def check_directory(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4())[:13], ext)
    return '{0}/{1}/corr/out/check/{2}/{3}'.format(get_user_suffix(instance.user.id), get_debtor_nomenclature(instance.debtor), instance.outcorr_date.strftime('%Y/%m'), filename)
    
    
class LetterType(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Найменування',
    )
    slug = models.SlugField(
        max_length=100, 
        verbose_name='Url', 
        unique=True,
    )
    
    class Meta:
        verbose_name = 'Тип кореспонденції'
        verbose_name_plural = 'Тип кореспонденції'
        ordering = ['title']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(LetterType, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('lettertype-update', kwargs={"slug": self.slug})
    
    
class LetterSummary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=150,
        verbose_name='Найменування',
    )
    slug = models.SlugField(
        max_length=150, 
        verbose_name='Url', 
        unique=True,
    )
    
    class Meta:
        verbose_name = 'Короткий зміст кореспонденції'
        verbose_name_plural = 'Короткий зміст кореспонденції'
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(LetterSummary, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('lettersummary-update', kwargs={"slug": self.slug})
    
    
class Correspondent(models.Model):
    
    TOWN = 'м.'
    URBAN_VILLAGE = 'смт.'
    VILLAGE = 'с.'
    CITY_TYPE_CHOICES = (
        (TOWN, 'місто'),
        (URBAN_VILLAGE,'село міського типу'),
        (VILLAGE,'село'),
    )
    
    BOULEVARD = 'бул.'
    AVENUE = 'пр.'
    STREET = 'вул.'
    LANE = 'пров.'
    STREET_TYPE_CHOICES = (
        (BOULEVARD, 'бульвар'),
        (AVENUE, 'проспект'),
        (STREET, 'вулиця'),
        (LANE, 'провулок'),
    )
    
    # CITY_TYPE = (
    #     ('місто', 'м.'),
    #     ('село міського типу', 'смт.'),
    #     ('село', 'с.'),
    # )
    # STREET_TYPE = (
    #     ('бульвар', 'бул.'),
    #     ('проспект', 'пр.'),
    #     ('вулиця', 'вул.'),
    #     ('провулок', 'пров.'),
    # )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    kod = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Ідентифікаційний код',
    )
    full_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name='Повне найменування',
    )
    short_name = models.CharField(
        max_length=150, 
        verbose_name='Скорочене найменування',
    )
    add_country = models.CharField(
        max_length=50, 
        verbose_name='Країна', 
        blank=True,
        default='Україна'
    )
    add_index = models.CharField(
        max_length=8,
        verbose_name='Поштовий індекс',
        blank=True,
    )
    add_region=models.CharField(
        max_length=50, 
        verbose_name='Область', 
        blank=True
    )
    add_district = models.CharField(
        max_length=50, 
        verbose_name='Район', 
        blank=True,
    )
    add_city_type = models.CharField(
        max_length=20, 
        choices=CITY_TYPE_CHOICES, 
        verbose_name='',
        blank=True,
        default='місто'
    )
    add_city = models.CharField(
        max_length=50, 
        verbose_name='Населений пункт',
        blank=True,
    )
    add_street_type = models.CharField(
        max_length=20, 
        choices=STREET_TYPE_CHOICES, 
        verbose_name='',
        blank=True,
        default='вулиця'
    )
    add_street = models.CharField(
        max_length=50, 
        verbose_name='Назва вулиці',
        blank=True,
    )
    add_building = models.CharField(
        max_length=10, 
        verbose_name='Номер будинку', 
        blank=True,
        default='',
    )
    add_corps = models.CharField(
        max_length=10, 
        verbose_name='Корпус', 
        blank=True,
        default='',
    )
    add_office = models.CharField(
        max_length=10, 
        verbose_name='Офіс', 
        blank=True,
        default='',
    )
    create_time = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата створення',
    )
    update_time = models.DateTimeField(
        auto_now=True, 
        verbose_name='Дата внесення змін',
    )
    slug = models.SlugField(
        max_length=150, 
        verbose_name='Url', 
        unique=True,
    )
    
    class Meta:
        verbose_name = 'Кореспондент'
        verbose_name_plural = 'Кореспонденти'
        ordering = ['short_name']
    
    def __str__(self):
        return self.short_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.short_name))
        super(Correspondent, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('сorrespondent-update', kwargs={"slug": self.slug})
    
    
class Outсorr(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    outcorr_date = models.DateField(
        auto_now=False, 
        auto_now_add=False,
        verbose_name='Дата реєстрації',
    )
    outcorr_num = models.CharField(
        max_length=50, 
        verbose_name='Реєстраційний номер',
    )
    correspondent = models.CharField(
        max_length=150,
        verbose_name='Кореспондент',
    )
    letter_type = models.ForeignKey(
        LetterType, 
        on_delete=models.RESTRICT,
        verbose_name='Тип листа',
    )
    letter_summary = models.ForeignKey(
        LetterSummary, 
        on_delete=models.RESTRICT,
        verbose_name='Короткий зміст листа',
    )
    debtor = models.ForeignKey(
        'main.Debtor', 
        on_delete=models.RESTRICT,
        verbose_name='Боржник',
    )
    
    letter_doc = models.FileField(
        upload_to=outcorr_doc_directory, 
        # storage=fs,
        blank=True,
        verbose_name='doc листа',
        validators=[FileExtensionValidator(['docx', 'doc'])],
    )
    
    letter_scan = models.FileField(
        upload_to=outcorr_directory, 
        blank=True,
        verbose_name='Скан листа',
        validators=[FileExtensionValidator(['pdf'])],
    )
    check_scan = models.FileField(
        upload_to=check_directory, 
        blank=True,
        verbose_name='Скан чека про відправку',
        validators=[FileExtensionValidator(['pdf'])],
    )
    check_amount = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Сума чека про відправку',
    )
    slug = models.SlugField(
        max_length=50, 
        verbose_name='Url', 
        unique=True,
    ) 
    create_time = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата створення',
    )
    update_time = models.DateTimeField(
        auto_now=True, 
        verbose_name='Дата внесення змін',
    )
    
    class Meta:
        verbose_name = 'Вихідний лист'
        verbose_name_plural = 'Вихідна кореспонденція'
        ordering = ['-create_time']
    
    def __str__(self):
        return self.outcorr_num
    
    def save(self, *args, **kwargs):
        slug = self.outcorr_num.replace('/', '_')
        self.slug = slugify(unidecode(slug))
        # self.slug = slugify(unidecode(self.incorr_num))
        super(Outсorr, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('outcorr-update', kwargs={"slug": self.slug})
    
    
class Inсorr(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    incorr_date = models.DateField(
        auto_now=False, 
        auto_now_add=False,
        verbose_name='Дата реєстрації',
    )
    incorr_num = models.CharField(
        max_length=50, 
        verbose_name='Реєстраційний номер',
    )
    correspondent = models.CharField(
        max_length=150,
        verbose_name='Кореспондент',
    )
    corr_datenum = models.CharField(
        max_length=50, 
        verbose_name='Дата та номер вхідного листа',
    )
    debtor = models.ForeignKey(
        'main.Debtor', 
        on_delete=models.RESTRICT,
        verbose_name='Боржник',
    )
    letter_type = models.ForeignKey(
        LetterType, 
        on_delete=models.RESTRICT,
        verbose_name='Тип листа',
    )
    executed = models.CharField(
        max_length=50,
        verbose_name='Відмітка про виконання',
        blank=True,
        default='-',
    )
    letter_scan = models.FileField(
        upload_to=incorr_directory, 
        blank=True,
    )
    slug = models.SlugField(
        max_length=50, 
        verbose_name='Url', 
        unique=True,
    ) 
    create_time = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата створення',
    )
    update_time = models.DateTimeField(
        auto_now=True, 
        verbose_name='Дата внесення змін',
    )
    
    class Meta:
        verbose_name = 'Вхідний лист'
        verbose_name_plural = 'Вхідна кореспонденція'
        ordering = ['-incorr_num']
    
    def __str__(self):
        return self.incorr_num
    
    def save(self, *args, **kwargs):
        slug = self.incorr_num.replace('/', '_')
        self.slug = slugify(unidecode(slug))
        # self.slug = slugify(unidecode(self.incorr_num))
        super(Inсorr, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('incorr-update', kwargs={"slug": self.slug})


