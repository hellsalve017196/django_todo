"""testApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todo_list.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home,name='home_page'),
    url(r'^getting_in', getting_in,name='getting_in'),
    url(r'^sign_up', sign_up, name='sign_up'),
    url(r'^user_list/', user_list, name='user_list'),
    url(r'^create_todo', create_todo, name='create_todo'),
    url(r'^todo_by_user/', todo_by_user, name='todo_list'),
    url(r'^update_todo', update_todo, name='update_todo'),
    url(r'^delete_todo', delete_todo, name='delete_todo'),
]
