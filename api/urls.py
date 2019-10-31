from django.urls import path
from .views import ListTodo, DetailTodo
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('todo/', ListTodo.as_view(), name="todos"),
	path('todo/<int:pk>/', DetailTodo.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)