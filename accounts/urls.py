from . import views
from django.urls import path

from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('content',views.gc_content,name="content"),
    path('register',views.gc_register,name="register"),
    path('login',views.gc_login,name="login"),
    path('logout',views.gc_logout,name="logout")


]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)