from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as django_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',django_views.LoginView.as_view(template_name='html/login.html',extra_context={'title': 'Login'}), name='login'),
    path('logout/',django_views.LogoutView.as_view(template_name='html/logout.html',extra_context={'title': 'Logout'}),name='logout'),
    path('todo/',include("todo.urls"),name="todo"),
]
