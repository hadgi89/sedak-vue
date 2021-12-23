from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode




class Debtor(models.Model):
    CITY_TYPE = (
        ('місто', 'місто'),
        ('село міського типу', 'село міського типу'),
        ('село', 'село'),
    )
    STREET_TYPE = (
        ('бульвар', 'бульвар'),
        ('проспект', 'проспект'),
        ('вулиця', 'вулиця'),
        ('провулок', 'провулок'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,)
    kod = models.CharField(
        max_length=10,
        verbose_name='Ідентифікаційний код',)
    full_name = models.CharField(
        max_length=250, 
        verbose_name='Повне найменування',)
    short_name = models.CharField(
        max_length=150, 
        verbose_name='Скорочене найменування',)
    slug = models.SlugField(
        max_length=150, 
        verbose_name='Url', 
        unique=True,) 
    case_num = models.CharField(
        max_length=30, 
        verbose_name='Номер справи про банкрутство',)
    nomenclature_num = models.CharField(
        max_length=3, 
        verbose_name='Номенклатурний номер',
        blank=True,
        default='')
    add_country = models.CharField(
        max_length=50, 
        verbose_name='Країна', 
        blank=True,
        default='Україна')
    add_index = models.CharField(
        max_length=8,
        verbose_name='Поштовий індекс',
        blank=True,)
    add_region=models.CharField(
        max_length=50, 
        verbose_name='Область', 
        blank=True)
    add_district = models.CharField(
        max_length=50, 
        verbose_name='Район', 
        blank=True,)
    add_city_type = models.CharField(
        max_length=20, 
        choices=CITY_TYPE, 
        verbose_name='',
        blank=True,
        default='місто')
    add_city = models.CharField(
        max_length=50, 
        verbose_name='Населений пункт',
        blank=True,)
    add_street_type = models.CharField(
        max_length=20, 
        choices=STREET_TYPE, 
        verbose_name='',
        blank=True,
        default='вулиця')
    add_street = models.CharField(
        max_length=50, 
        verbose_name='Назва вулиці',
        blank=True,)
    add_building = models.CharField(
        max_length=10, 
        verbose_name='Номер будинку', 
        blank=True,
        default='',)
    add_corps = models.CharField(
        max_length=10, 
        verbose_name='Корпус', 
        blank=True,
        default='',)
    add_office = models.CharField(
        max_length=10, 
        verbose_name='Офіс', 
        blank=True,
        default='',)
    
    create_time = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата створення',)
    update_time = models.DateTimeField(
        auto_now=True, 
        verbose_name='Дата внесення змін',)
    
    class Meta:
        verbose_name = 'Боржник'
        verbose_name_plural = 'Боржники'
        ordering = ['-create_time']

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        # для получения slug по get_absolute_url из модели name(urls) должно быть 
        # = name из функции  get_absolute_url модели DEBTORS:
        return reverse('debtor-detail', kwargs={"slug": self.slug})
        
        # return reverse('debtor-detail', args=[str(self.slug)])
        # return reverse("_detail", kwargs={"pk": self.pk})

    # автозаполнение поля слаг на основе другого поля на уровне модели:
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.short_name))
        super(Debtor, self).save(*args, **kwargs)

