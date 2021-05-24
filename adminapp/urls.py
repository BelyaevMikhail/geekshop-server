from django.urls import path

from adminapp.views import index, admin_users_read, admin_users_create

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', admin_users_read, name='admin_users_read'),
    path('admin-users-create/', admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),
]