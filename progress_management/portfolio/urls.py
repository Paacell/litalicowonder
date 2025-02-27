from django.urls import path
from . import views
from .views import portfolio_list, add_portfolio

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path("add/", add_portfolio, name="add_portfolio"),    
    path('<int:project_id>/edit/', views.edit_portfolio, name='edit_portfolio'),
    path('<int:project_id>/delete/', views.delete_portfolio, name='delete_portfolio'),
    path('public/', views.public_portfolio_list, name='public_portfolio_list'),
]


# from django.urls import path
# from .views import portfolio_list, add_portfolio

# app_name = "portfolio"

# urlpatterns = [
#     path("", portfolio_list, name="portfolio_list"),
#     path("add/", add_portfolio, name="add_portfolio"),
# ]
