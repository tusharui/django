from django.urls import path 
from .views import RegisterView , LoginView ,  TaskListCreateView , TaskDetailView

urlpatternsc=[
    path('register/' ,RegisterView.as_view(), name = 'register' ),
    path('login/' , LoginView.as_view(), name='login'),
    path('',TaskListCreateView.as_view() , name="task-list-create"),
    path('<int:pk>/' , TaskDetailView.as_view(), name='task-detail '),
]
