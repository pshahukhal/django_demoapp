from django.conf.urls import url
from blog_app import views

urlpatterns=[
    url(r'^$',views.PostView.as_view(),name="posts_list"),
    url(r'^about/$',views.AboutView.as_view(),name="about"),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name="posts_detail"),
    url(r'^post/new/$',views.PostCreateView.as_view(),name="posts_new"),
    url(r'^post/(?P<pk>\d+)/edit$',views.PostUpdateView.as_view(),name="post_edit"),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.posts_publish, name='posts_publish'),
    url(r'^post/(?P<pk>\d+)/remove$',views.PostDeleteView.as_view()),
    url(r'^drafts/$', views.DraftListView.as_view(), name='posts_draft_list'),
    url(r'^post/(?P<pk>\d+)/add_comment$',views.add_comment,name='add_comment')
]
