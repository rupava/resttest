from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_index,name="todo_index"),
    path('edit/', todo_edit, name='edit'),

]