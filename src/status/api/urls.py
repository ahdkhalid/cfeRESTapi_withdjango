
from django.conf.urls import url

# from .views import StatusListSearchAPIView
from .views import (
    StatusAPIView, 
    # StatusCreateAPIView,
    StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
)


urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    # url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusDetailAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),

#start with
# /api/status -> List
# /api/status/create -> Create
# /api/status/12 -> Detail
# /api/status/12/update -> Update
# /api/status/12/delete -> Delete
]


#End with
# /api/status -> List -> CRUD
# /api/status/12 -> Detail -> CRUD

#finaly
# /api/status -> CRUD and List Search