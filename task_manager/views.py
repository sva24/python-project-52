from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def index(request):
    return render(
        request,
        "greeting.html",
    )


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        message = _("You are logged in")
        messages.success(self.request, message)
        return super().form_valid(form)


class LogoutUserView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        message = _("You are logged out")
        messages.info(request, message)
        return super().dispatch(request, *args, **kwargs)
