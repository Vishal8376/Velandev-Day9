from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<note_id>',views.delete,name='delete'),
    path('update/<note_id>', views.update, name='update'),
    path('login/', auth_views.LoginView.as_view(template_name='note/login.html'), name='login'),

]