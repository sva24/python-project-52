from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import LoginCheckMixin, PermissionCheckMixin, DeleteProtectedObjectMixin
from django.utils.translation import gettext_lazy as _


# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UsersListView(ListView):
    model = get_user_model()
    template_name = 'show_users.html'

    def get_queryset(self):
        return self.model.objects.filter(is_superuser=False)


class UserUpdateView(LoginCheckMixin,
                     PermissionCheckMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'update.html'
    success_url = reverse_lazy('users')
    success_message = _("User was updated successfully")


class UserDeleteView(LoginCheckMixin,
                     PermissionCheckMixin,
                     SuccessMessageMixin,
                     DeleteProtectedObjectMixin,
                     DeleteView):
    model = get_user_model()
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
    protected_error_message = _('Cannot delete user because it is in use')
    protect_redirect = 'users'
