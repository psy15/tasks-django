from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, RegisterPage
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('login/',CustomLoginView.as_view(),name='login'),
    # path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register', RegisterPage.as_view(), name='register'),
    path('', TaskListView.as_view(), name='todo'),
    path('task-create/', TaskCreateView.as_view(), name='task_create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]
