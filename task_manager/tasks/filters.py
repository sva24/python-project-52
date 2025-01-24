import django_filters
from .models import Task, Label, Status
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_("Status"))
    executor = django_filters.ModelChoiceFilter(
        queryset=get_user_model().objects.all(),
        label=_("Executor"))
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all(),
                                              label=_("Label"))
    self_tasks = django_filters.BooleanFilter(method='filter_self_tasks',
                                              widget=forms.CheckboxInput,
                                              label=_("Only my tasks"))

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(created_by=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'self_tasks']

