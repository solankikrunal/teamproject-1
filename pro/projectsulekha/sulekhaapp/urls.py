from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^home/index.html/$', views.index),
    url(r'^home/loginPage.html/', views.login),
    url(r'^login/$', views.loginpost),
    url(r'^home/post.html/', views.post),
    url(r'^login/$', views.login),
    url(r'^logout/$',views.logout),
    url(r'^post/$', views.post),  
    url(r'^postviews/$', views.postview),
]