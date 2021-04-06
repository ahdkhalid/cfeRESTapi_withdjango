from django.conf.urls import url

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token # since we don't have accounts app

from .views import AuthAPIView, RegisterAPIView
urlpatterns = [
    url(r'^$', AuthAPIView.as_view()), #root view
    url(r'^register/$', RegisterAPIView.as_view()), 
    url(r'^jwt/$', obtain_jwt_token),
    url(r'^jwt/refresh/$', refresh_jwt_token),
]
