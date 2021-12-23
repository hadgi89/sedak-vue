from django.shortcuts import get_object_or_404, render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Debtor
from .forms import DebtorCreateForm, DebtorUpdateForm


@login_required(login_url='signin')
def index(request):
    return render(request, 'main/index.html')  # путь к шаблону ГЛАВНАЯ


@login_required(login_url='signin')
def projects(request):
    return render(request, 'main/projects.html')  # путь к шаблону ПРОЕКТЫ


class Debtor_List(LoginRequiredMixin, ListView):
    login_url = 'signin'
    template_name = 'main/debtor_list.html'
    context_object_name = 'debtor_list'
    paginate_by = 10
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Боржники'
        return context

    def get_queryset(self):
        # Выбор данных из таблицы ДОЛЖНИКИ для текущего пользователя:
        return Debtor.objects.filter(user__id=self.request.user.id)


class Debtor_Create(LoginRequiredMixin, CreateView):
    login_url = 'signin'
    form_class = DebtorCreateForm
    template_name = 'main/debtor_create.html'
    success_url = reverse_lazy ('debtor-list')

    # Добавление текущего пользователя в связанное поле USER:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Debtor_Create, self).form_valid(form)

class Debtor_Detail(LoginRequiredMixin, DetailView):
    login_url = 'signin'
    model = Debtor 
    template_name = 'main/debtor_detail.html'
    context_object_name = 'debtor_detail'


class Debtor_Update(LoginRequiredMixin, UpdateView):
    login_url = 'signin'
    model = Debtor
    form_class = DebtorUpdateForm
    context_object_name = 'debtor_update'
    template_name = 'main/debtor_update.html'
    
    def get_success_url(self):
        return reverse('debtor-detail', kwargs={'slug': self.object.slug})

