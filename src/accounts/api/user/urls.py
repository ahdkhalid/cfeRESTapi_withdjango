from django.conf.urls import url

from .views import UserDetailAPIView, UserStatusAPIView

app_name = 'accounts'
urlpatterns = [
    url(r'^(?P<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<username>\w+)/status/$', UserStatusAPIView.as_view(), name='status-list'),
]