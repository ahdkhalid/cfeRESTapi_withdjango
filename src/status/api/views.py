from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View # don't need it now , since rest it is now

from status.models import Status
from .serializers import StatusSerializer


class StatusListSearchAPIView(APIView):
     permission_classes     = []
     authentication_classes = []
     
     def get(self, request, format=None):
         qs = Status.objects.all()
         serializer = StatusSerializer(qs, many=True)
         return Response(serializer.data)  

     def post(self, request, format=None): #to show we can have it too. 
         qs = Status.objects.all()
         serializer = StatusSerializer(qs, many=True)
         return Response(serializer.data)  

# CreateModelMixin --- POST mothod
# UpdateModelMixin --- PUT method
# DestroyModelMixin --- DELETE method
class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
     permission_classes     = []
     authentication_classes = []
     serializer_class       = StatusSerializer
    
     def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter (content__icontains = query)
        return qs
     def post(self, request,*args, **kwargs):
         return self.create(request, *args, **kwargs)

# class StatusCreateAPIView(generics.CreateAPIView):
#      permission_classes     = []
#      authentication_classes = []
#      queryset               = Status.objects.all()
#      serializer_class       = StatusSerializer

class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView): #much cleaner version
     permission_classes     = []
     authentication_classes = []
     queryset               = Status.objects.all()
     serializer_class       = StatusSerializer
     lookup_field           = 'id' # defualt is pk - toward making our own slug   

class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin,generics.RetrieveAPIView):
     permission_classes     = []
     authentication_classes = []
     queryset               = Status.objects.all()
     serializer_class       = StatusSerializer
     lookup_field           = 'id' # defualt is pk - toward making our own slug
     
     def put(self, request,*args, **kwargs):
         return self.update(request, *args, **kwargs)
     def patch(self, request,*args, **kwargs):
         return self.update(request, *args, **kwargs)
     def delete(self, request,*args, **kwargs):
         return self.destroy(request, *args, **kwargs)
    #  def get_object (self, *args, **kwargs):
    #      kwargs = self.kwargs
    #      kw_id = kwargs.get ('id') #if change id, we have to change P<id> in urls.py too
    #      return Status.objects.get(id=kw_id)

# class StatusUpdateAPIView(generics.UpdateAPIView):
#      permission_classes     = []
#      authentication_classes = []
#      queryset               = Status.objects.all()
#      serializer_class       = StatusSerializer
    
# class StatusDeleteAPIView(generics.DestroyAPIView):
#      permission_classes     = []
#      authentication_classes = []
#      queryset               = Status.objects.all()
#      serializer_class       = StatusSerializer
