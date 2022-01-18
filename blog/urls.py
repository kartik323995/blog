from django.urls import path, re_path
from django.contrib.auth import views as c_view
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.listview.as_view(),name='blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('register/', views.register, name = 'user-register'),
    path('profile/', views.profile, name = 'user-profile'),
    path('login/', c_view.LoginView.as_view(template_name = 'blog/login.html'), name = 'user-login'),
    path('logout/', c_view.LogoutView.as_view(template_name = 'blog/logout.html'), name = 'user-logout'),
    path('<int:pk>/', views.detail.as_view(), name = 'post-detail'),
    path('new/', views.create.as_view(), name = 'new-post'),
    path('<str:username>/posts/', views.user_posts.as_view(), name = 'user-post'),
    path('<int:pk>/update/', views.update.as_view(), name = 'update-post'),
    path('<int:pk>/delete/', views.delete.as_view(), name = 'delete-post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  