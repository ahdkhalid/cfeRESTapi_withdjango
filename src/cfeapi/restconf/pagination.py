from rest_framework import pagination

class CustomAPIPagination(pagination.LimitOffsetPagination):#PageNumberPagination):
    #page_size =8
    default_limit   = 10
    max_limit       = 30