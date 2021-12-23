# импорт стандартных библиотек:
from django.urls import path
from django.urls.conf import include
    
# импорт сторонних библиотек:
    
# импорт модулей текущего проекта:
from .views import *
    
    
urlpatterns = [
    path('in/', include([
        path('', IncorrList.as_view(), name='incorr-list'),
        path('create/', IncorrCreate.as_view(), name='incorr-create'),
        path('<str:slug>/', IncorrUpdate.as_view(), name='incorr-update'),
        path('<str:slug>/delete/', IncorrDelete.as_view(), name='incorr-delete'),
    ])),
    
    path('out/', include([
        path('', OutcorrList.as_view(), name='outcorr-list'),
        path('create/', OutcorrCreate.as_view(), name='outcorr-create'),
        path('<str:slug>/', OutcorrUpdate.as_view(), name='outcorr-update'),
        path('<str:slug>/delete/', OutcorrDelete.as_view(), name='outcorr-delete'),
    ])),

    path('db/', include([
        path('', dbcorr_page, name='dbcorr-page'),
        path('correspondent/', CorrespondentList.as_view(), name='сorrespondent-list'),
        path('correspondent/create/', CorrespondentCreate.as_view(), name='correspondent-create'),
        path('correspondent/<str:slug>/detail/', CorrespondentUpdate.as_view(), name='сorrespondent-update'),
        path('correspondent/<str:slug>/delete/', CorrespondentDelete.as_view(), name='сorrespondent-delete'),
        
        path('lettertype/', LetterTypeList.as_view(), name='lettertype-list'),
        path('lettertype/create/', LetterTypeCreate.as_view(), name='lettertype-create'),
        path('lettertype/<str:slug>/detail/', LetterTypeUpdate.as_view(), name='lettertype-update'),
        path('lettertype/<str:slug>/delete/', LetterTypeDelete.as_view(), name='lettertype-delete'),

        path('lettersummary/', LetterSummaryList.as_view(), name='lettersummary-list'),
        path('lettersummary/create/', LetterSummaryCreate.as_view(), name='lettersummary-create'),
        path('lettersummary/<str:slug>/detail/', LetterSummaryUpdate.as_view(), name='lettersummary-update'),
        path('lettersummary/<str:slug>/delete/', LetterSummaryDelete.as_view(), name='lettersummary-delete'),
    ])),
]

