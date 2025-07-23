
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', LoginView.as_view(template_name='blog/login.html', redirect_authenticated_user=True), name='login'),
]