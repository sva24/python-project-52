from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from .users.models import CustomUser
from django.core.exceptions import PermissionDenied


class LoginCheckMixin(LoginRequiredMixin):
    def get_login_message(self):
        return _('You are not logged in! Please sign in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.get_login_message())
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class PermissionCheckMixin:
    def get_permission_message(self):
        return _('You do not have permission to change another user.')

    def dispatch(self, request, *args, **kwargs):
        user_to_edit = get_object_or_404(CustomUser, pk=kwargs.get('pk'))

        if request.user != user_to_edit:
            messages.error(request, self.get_permission_message())
            return redirect('users')

        return super().dispatch(request, *args, **kwargs)


class TemplateContextMixin:
    page_title = ""
    submit_button_text = ""

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['submit_button_text'] = self.submit_button_text
        return context
