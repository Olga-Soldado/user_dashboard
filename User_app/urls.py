from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('signin', views.signin),
    path('login', views.login ),
    path('registration', views.registration),
    path('register', views.register),
    path('admin_dashboard', views.admin_dashboard),
    path('user_dashboard', views.user_dashboard),
    path('user_edit', views.user_edit),
    path('edit_info', views.edit_info),
    path('edit_password', views.edit_password),
    path('admin_edit/<int:id>', views.admin_edit),
    path('admin_edit_info/<int:id>', views.admin_edit_info),
    path('admin_edit_password/<int:id>', views.admin_edit_password),
    path('delete/<int:id>', views.delete),
    path('add', views.add),
    path('admin_add', views.admin_add),
    path('show/<int:id>', views.show),
    path('message/<int:id>', views.message),
    path('logout', views.logout),
]