

from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("findings/", views.finding_list, name="finding_list"),
]


