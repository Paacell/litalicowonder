from django.urls import path
from . import views
from .views import progress_list, add_progress

app_name = 'progress'

urlpatterns = [
    path('', views.progress_list, name='progress_list'),
    path('add/', add_progress, name='add_progress'),
    path('<int:progress_id>/edit/', views.edit_progress, name='edit_progress'),
    path('<int:progress_id>/delete/', views.delete_progress, name='delete_progress'),
]

# from django.urls import path
# from . import views

# app_name = 'progress'

# urlpatterns = [
#     path('game/<int:game_id>/', views.progress_list, name='progress_list'),
#     path('game/<int:game_id>/add/', views.add_progress, name='add_progress'),
#     path('<int:progress_id>/edit/', views.edit_progress, name='edit_progress'),
#     path('<int:progress_id>/delete/', views.delete_progress, name='delete_progress'),
# ]
