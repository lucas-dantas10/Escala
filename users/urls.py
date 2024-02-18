from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("update/<int:pk>", views.MinistroUpdateView.as_view(),
         name="ministro_update"),
    path('login', auth_views.LoginView.as_view(
        template_name='pages/login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]