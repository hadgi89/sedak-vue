# импорт стандартных библиотек:
from django.shortcuts import get_object_or_404, render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
    
# импорт сторонних библиотек:
    
# импорт модулей текущего проекта:
from .models import *
from .forms import *
    
    
@login_required(login_url='signin')
def dbcorr_page(request):
    letter_type = LetterType.objects.all().order_by('title')[:5]
    letter_summary = LetterSummary.objects.all().order_by('title')[:5]
    сorrespondent = Correspondent.objects.all().order_by('short_name')[:5]
    
    content = {
        "сorrespondent":сorrespondent,
        "letter_type":letter_type, 
        "letter_summary":letter_summary,
        }
    return render(request, 'corr/db_corr.html', content)
    
    
class CorrespondentList(LoginRequiredMixin, ListView):
    login_url = 'signin'
    template_name = 'corr/сorrespondent_list.html'
    context_object_name = 'correspondent_list'
    paginate_by = 10
    allow_empty = True
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Кореспонденти'
        return context
    
    def get_queryset(self):
        return Correspondent.objects.filter(user__id=self.request.user.id)
    
    
class CorrespondentCreate(LoginRequiredMixin, CreateView):
    login_url = 'signin'
    form_class = CorrespondentCreateForm
    template_name = 'corr/correspondent_create.html'
    success_url = reverse_lazy ('correspondent-list')
    
    # Добавление текущего пользователя в связанное поле USER:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CorrespondentCreate, self).form_valid(form)
    

class CorrespondentUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'signin'
    model = Correspondent
    form_class = CorrespondentUpdateForm
    context_object_name = 'correspondent_update'
    template_name = 'corr/correspondent_update.html'
    
    
class CorrespondentDelete(LoginRequiredMixin, DeleteView):
    model = Correspondent
    template_name = 'corr/correspondent_delete.html'
    context_object_name = 'correspondent_delete'
    success_url = reverse_lazy('сorrespondent-list')
    
    
class LetterTypeList(LoginRequiredMixin, ListView):
    login_url = 'signin'
    template_name = 'corr/lettertype_list.html'
    context_object_name = 'lettertype_list'
    paginate_by = 10
    allow_empty = True
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тип кореспонденції'
        return context
    
    def get_queryset(self):
        return LetterType.objects.filter(user__id=self.request.user.id)
    
    
class LetterTypeCreate(LoginRequiredMixin, CreateView):
    login_url = 'signin'
    form_class = LetterTypeCreateForm
    template_name = 'corr/lettertype_create.html'
    success_url = reverse_lazy ('lettertype-list')
    
    # Добавление текущего пользователя в связанное поле USER:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LetterTypeCreate, self).form_valid(form)
    

class LetterTypeUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'signin'
    model = LetterType
    form_class = LetterTypeUpdateForm
    context_object_name = 'lettertype_update'
    template_name = 'corr/lettertype_update.html'
    
    
class LetterTypeDelete(LoginRequiredMixin, DeleteView):
    model = LetterType
    template_name = 'corr/lettertype_delete.html'
    context_object_name = 'lettertype_delete'
    success_url = reverse_lazy('lettertype-list')
    

class LetterSummaryList(LoginRequiredMixin, ListView):
    login_url = 'signin'
    template_name = 'corr/lettersummary_list.html'
    context_object_name = 'lettersummary_list'
    paginate_by = 10
    allow_empty = True
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Короткий зміст кореспонденції'
        return context
    
    def get_queryset(self):
        return LetterSummary.objects.filter(user__id=self.request.user.id)
    

class LetterSummaryCreate(LoginRequiredMixin, CreateView):
    login_url = 'signin'
    form_class = LetterSummaryCreateForm
    template_name = 'corr/lettersummary_create.html'
    success_url = reverse_lazy ('lettersummary-list')
    
    # Добавление текущего пользователя в связанное поле USER:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LetterSummaryCreate, self).form_valid(form)
    

class LetterSummaryUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'signin'
    model = LetterSummary
    form_class = LetterSummaryUpdateForm
    template_name = 'corr/lettersummary_update.html'
    context_object_name = 'lettersummary_update'
    

class LetterSummaryDelete(LoginRequiredMixin, DeleteView):
    model = LetterSummary
    template_name = 'corr/lettersummary_delete.html'
    context_object_name = 'lettersummary_delete'
    success_url = reverse_lazy('lettersummary-list')
    

class IncorrList(LoginRequiredMixin, ListView):
    login_url = 'signin'
    template_name = 'corr/incorr_list.html'
    context_object_name = 'incorr_list'
    paginate_by = 10
    allow_empty = True
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вхідна кореспонденція'
        return context
    
    def get_queryset(self):
        return Inсorr.objects.filter(user__id=self.request.user.id)
    
    
class IncorrCreate(LoginRequiredMixin, CreateView):
    login_url = 'signin'
    form_class = InсorrCreateForm
    template_name = 'corr/incorr_create.html'
    success_url = reverse_lazy ('incorr-list')
    
    # Добавление текущего пользователя в связанное поле USER:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IncorrCreate, self).form_valid(form)
    
    
class IncorrUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'signin'
    model = Inсorr
    form_class = InсorrUpdateForm
    template_name = 'corr/incorr_update.html'
    context_object_name = 'incorr_update'
    
    
class IncorrDelete(LoginRequiredMixin, DeleteView):
    model = Inсorr
    template_name = 'corr/incorr_delete.html'
    context_object_name = 'incorr_delete'
    success_url = reverse_lazy('incorr-list')
    

class OutcorrList(LoginRequiredMixin, ListView):
    login_url = 'signin'
    template_name = 'corr/outcorr_list.html'
    context_object_name = 'outcorr_list'
    paginate_by = 10
    allow_empty = True
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вихідна кореспонденція'
        return context
    
    def get_queryset(self):
        return Outсorr.objects.filter(user__id=self.request.user.id)
    
    
class OutcorrCreate(LoginRequiredMixin, CreateView):
    login_url = 'signin'
    form_class = OutсorrCreateForm
    template_name = 'corr/outcorr_create.html'
    success_url = reverse_lazy ('outcorr-list')
    
    # Добавление текущего пользователя в связанное поле USER:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OutcorrCreate, self).form_valid(form)
    
    
class OutcorrUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'signin'
    model = Outсorr
    form_class = OutсorrUpdateForm
    template_name = 'corr/outcorr_update.html'
    context_object_name = 'outcorr_update'
    
    
class OutcorrDelete(LoginRequiredMixin, DeleteView):
    model = Outсorr
    template_name = 'corr/outcorr_delete.html'
    context_object_name = 'outcorr_delete'
    success_url = reverse_lazy('outcorr-list')
