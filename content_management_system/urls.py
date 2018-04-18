"""content_management_system URL Configuration

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
from django.urls import include, re_path
from django.conf.urls import url
from news.views import index as news_index
from news.views import column_detail as news_column_detail
from news.views import article_detail as news_article_detail
urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path(r'^$', 'news.views.index', name='index'),
    # # path('',news_index, name = 'index'),
    # # path('column/',news_column_detail,name='column'),
    # # path('news/',news_article_detail,name='article'),
    # # path('ueditor/', DjangoUeditor_urls),
    # re_path(r'^column/(?P<column_slug>[^/]+)/$', 'news.views.column_detail', name='column'),
    # re_path(r'^news/(?P<article_slug>[^/]+)/$', 'news.views.article_detail', name='article'),
    url(r'^$', news_index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', news_column_detail, name='column'),
    url(r'^news/(?P<article_slug>[^/]+)/$', news_article_detail, name='article'),

    url(r'^admin/', admin.site.urls),
]