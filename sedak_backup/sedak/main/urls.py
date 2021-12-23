from django.urls import path
from django.urls.conf import include

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('debtor/', Debtor_List.as_view(), name='debtor-list'),
    path('debtor/create/', Debtor_Create.as_view(), name='debtor-create'),
    
    # для получения slug по get_absolute_url из модели name(urls) должно быть 
    # = name из функции get_absolute_url модели DEBTORS:
    
    path('debtor/<str:slug>/', Debtor_Detail.as_view(), name='debtor-detail'),
    path('debtor/<str:slug>/update/', Debtor_Update.as_view(), name='debtor-update'),
    
    
    # path('debtor/<str:slug>/', include([
    #     path('', Debtor_Detail.as_view(), name='debtor-detail'), 
    #     path('update/', Debtor_Update.as_view(), name='debtor-update'),
    # ]))
    
    # path('debtor/<str:slug>/edit/', Debtor_Update.as_view(), name='debtor_update'),
    
    
    # path('projects/', projects, name='projects'),
]
