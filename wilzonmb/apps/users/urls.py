from django.conf.urls import url
from .views import UserRegisterView, UserLoginView


urlpatterns = [
    url(r'^user/register/$', UserRegisterView.as_view()),
    url(r'^user/$', UserLoginView.as_view()),
    url(r'^salir/$', 'apps.users.views.LogOut'),
]
