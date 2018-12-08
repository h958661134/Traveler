"""游者 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demo1 import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.homePage,name = 'home'),
    path('demo/', views.demo, name='demo'),
    path('resiger/', views.resiger, name='resiger'),
    path('user/', views.log_in, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/',views.submit,name='submit'),
    path('search/',views.search,name='search'),
    path('success/', views.success, name='success'),

    url(r'^login_ajax/$', views.login_ajax),#显示ajax登录页面
    url(r'^login_ajax_check/$', views.login_ajax_check),#显示ajax登录校验

    # path('')
]

urlpatterns += staticfiles_urlpatterns()