from django.urls import path
from .views import main_page, game_detail, update_task_status, add_feedback

app_name = 'plans'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('plans/<int:game_id>/', game_detail, name='game_detail'),
    path('update_task_status/<int:task_id>/<str:new_status>/', update_task_status, name='update_task_status'),
    path('<int:game_id>/add_feedback/', add_feedback, name='add_feedback'),
]
