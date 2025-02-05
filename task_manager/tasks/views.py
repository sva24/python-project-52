from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from task_manager.mixins import (
    LoginCheckMixin,
    TaskOwnerCheckMixin,
    TemplateContextMixin,
)

from .filters import TaskFilter
from .models import Task

# Create your views here.


class TaskListView(FilterView):
    model = Task
    template_name = "show_tasks.html"
    context_object_name = "tasks"
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.all()


class TaskCreateView(
    LoginCheckMixin, SuccessMessageMixin, TemplateContextMixin, CreateView
):
    model = Task
    fields = ["name", "description", "status", "executor", "labels"]
    template_name = "create_task.html"
    success_url = reverse_lazy("tasks")
    page_title = _("Create task")
    submit_button_text = _("Create")
    success_message = _("Task successfully created")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdateView(
    LoginCheckMixin, SuccessMessageMixin, TemplateContextMixin, UpdateView
):
    model = Task
    fields = ["name", "description", "status", "executor", "labels"]
    template_name = "create_task.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully updated")
    page_title = _("Update task")
    submit_button_text = _("Update")


class TaskDeleteView(
    LoginCheckMixin,
    SuccessMessageMixin,
    TaskOwnerCheckMixin,
    TemplateContextMixin,
    DeleteView,
):
    model = Task
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("tasks")
    page_title = _("Delete task")
    success_message = _("Task successfully deleted")
    owner_field = "created_by"


class TaskDetailView(LoginCheckMixin, DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"
