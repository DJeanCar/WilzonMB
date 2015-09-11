from django.conf.urls import url
from .views import CreatePost

urlpatterns = [
    url(r'^post/crear/$', CreatePost.as_view()),
]
