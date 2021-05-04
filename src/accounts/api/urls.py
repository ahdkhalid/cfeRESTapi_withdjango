from django.conf.urls import url

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token # since we don't have accounts app

from .views import AuthAPIView, RegisterAPIView

app_name = 'accounts'
urlpatterns = [
    url(r'^$', AuthAPIView.as_view(), name = 'login'), #root view
    url(r'^register/$', RegisterAPIView.as_view(), name ='register'), 
    url(r'^jwt/$', obtain_jwt_token),
    url(r'^jwt/refresh/$', refresh_jwt_token),
]
