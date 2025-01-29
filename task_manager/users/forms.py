from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
        )


class CustomUserChangeForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if (
            username
            and self._meta.model.objects.filter(username=username)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise forms.ValidationError(
                self.instance.unique_error_message(
                    self._meta.model, ["username"]
                )
            )
        return username
