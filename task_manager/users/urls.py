from django.urls import path

from .views import SignUpView, UserDeleteView, UsersListView, UserUpdateView

urlpatterns = [
    path("", UsersListView.as_view(), name="users"),
    path("create/", SignUpView.as_view(), name="sign_up"),
    path("<int:pk>/update", UserUpdateView.as_view(), name="user_update"),
    path("<int:pk>/delete", UserDeleteView.as_view(), name="user_delete"),
]
