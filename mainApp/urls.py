from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('save_random_users', views.save_random_users, name='save_random_users'),
    path('show_users', views.show_users, name='show_users')
]
