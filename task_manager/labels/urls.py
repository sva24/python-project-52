from django.urls import path

from .views import (
    LabelCreateView,
    LabelDeleteView,
    LabelListView,
    LabelUpdateView,
)

urlpatterns = [
    path("", LabelListView.as_view(), name="labels"),
    path("create/", LabelCreateView.as_view(), name="label_create"),
    path("<int:pk>/update/", LabelUpdateView.as_view(), name="label_update"),
    path("<int:pk>/delete/", LabelDeleteView.as_view(), name="label_delete"),
]
