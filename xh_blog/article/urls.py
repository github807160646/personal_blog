from django.urls import path
from django.conf.urls import url
from . import  views


urlpatterns = [
    path('index/',views.home,name = 'index'),
    path('detail/<int:id>/',views.detail, name = 'detail'),
    path('archives/',views.archives , name = 'archives'),
    path('aboutme/',views.about_me, name = 'aboutme'),
    path('searchtag/<slug:tag>', views.search_tag,name = 'search_tag'),
    path('search/',views.blog_search ,name ='search'),
    url(r'^feed/$', views.RSSFeed(), name = "RSS"),  #新添加的urlconf, 并将name设置为RSS, 方便在模板中使用url


]