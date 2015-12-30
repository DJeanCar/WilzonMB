from django.conf.urls import url
from .views import CreatePost, CreateTag, CreateCategory, PostList, PostDetail, EditPost

urlpatterns = [
    url(r'^post/crear/$', CreatePost.as_view(), name="create_post"),
    url(r'^post/(?P<slug>[-\w]+)/editar/$', EditPost.as_view(), name="edit_post"),
    url(r'^tag/crear/$', CreateTag.as_view()),
    url(r'^categoria/crear/$', CreateCategory.as_view()),

    url(r'^posts/$', PostList.as_view(), name="post_list"),
    url(r'^posts/(?P<slug>[-\w]+)/$', PostDetail.as_view()),
]
