from django.conf.urls import url
from .views import CreatePost, CreateTag, CreateCategory, PostList, PostDetail

urlpatterns = [
    url(r'^post/crear/$', CreatePost.as_view()),
    url(r'^tag/crear/$', CreateTag.as_view()),
    url(r'^categoria/crear/$', CreateCategory.as_view()),

    url(r'^posts/$', PostList.as_view()),
    url(r'^posts/(?P<slug>[-\w]+)/$', PostDetail.as_view()),
]
