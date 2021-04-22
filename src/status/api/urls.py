
from django.conf.urls import url
app_name = 'status'

from .views import (
    StatusAPIView, 
    StatusDetailAPIView,

)


urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusDetailAPIView.as_view(),name='detail'),

]

