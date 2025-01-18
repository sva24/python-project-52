from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from task_manager.mixins import LoginCheckMixin, TemplateContextMixin, TaskOwnerCheckMixin
from .models import Task
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _


# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'show_tasks.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        queryset = Task.objects.all()

        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status__id=status_filter)

        executor_filter = self.request.GET.get('executor')
        if executor_filter:
            queryset = queryset.filter(executor__id=executor_filter)

        if self.request.GET.get('self_tasks'):
            queryset = queryset.filter(created_by=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['users'] = get_user_model().objects.all()
        return context


class TaskCreateView(LoginCheckMixin,
                     TemplateContextMixin,
                     CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor']
    template_name = 'create_task.html'
    success_url = reverse_lazy('tasks')
    page_title = _("Create task")
    submit_button_text = _("Create")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginCheckMixin,
                     TemplateContextMixin,
                     UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor']
    template_name = 'create_task.html'
    success_url = reverse_lazy('tasks')
    page_title = _("Update task")
    submit_button_text = _("Update")


class TaskDeleteView(LoginCheckMixin,
                     TaskOwnerCheckMixin,
                     TemplateContextMixin,
                     DeleteView):
    model = Task
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('tasks')
    page_title = _("Delete task")
    success_message = _("Task successfully deleted")
    owner_field = 'created_by'


class TaskDetailView(LoginCheckMixin,
                     DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
