
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("findings/", views.finding_list, name="finding_list"),
    path("findings/new/", views.finding_create, name="finding_create"),
    path("findings/<int:pk>/edit/", views.finding_edit, name="finding_edit"),

]



