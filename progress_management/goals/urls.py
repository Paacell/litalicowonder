# from django.urls import path
# from .views import goal_list, edit_goal

# app_name = "goals"

# urlpatterns = [
#     path("", goal_list, name="goal_list"),
#     path("edit/", edit_goal, name="edit_goal"),
# ]

from .views import my_goals
from django.urls import path
from . import views

app_name = "goals"

urlpatterns = [
    path("", views.my_goals, name="my_goals"),
    path("students/", views.student_list, name="student_list"),  # 生徒一覧
    path("students/<int:student_id>/goals/", views.student_goal_list, name="student_goal_list"),  # 生徒ごとの目標一覧
    path("goal/edit/<int:goal_id>/", views.goal_edit, name="goal_edit"),  # 目標の編集
    path("goal/create/", views.goal_edit, name="goal_create"),  # 目標の作成
]
