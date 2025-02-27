from django.urls import path
from .views import goal_list, edit_goal

app_name = "goals"

urlpatterns = [
    path("", goal_list, name="goal_list"),
    path("edit/", edit_goal, name="edit_goal"),
]
