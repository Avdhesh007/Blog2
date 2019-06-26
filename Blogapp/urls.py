from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^login/$',views.login,name='login'),
    url(r'logout$',views.logout_user,name='logout'),
    url(r'^blogapi/$',views.blogapi,name='blogapi'),
    url(r'^addblog',views.addblog,name='addblog'),
    url(r'^update',views.updateblog,name='updateblog'),
    url(r'^view',views.viewblog,name='viewblog'),

]