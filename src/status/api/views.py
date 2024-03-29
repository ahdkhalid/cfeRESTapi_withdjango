import json
from rest_framework import generics, mixins,permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View # don't need it now , since rest it is now
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer
from accounts.api.permissions import IsOwnerOrReadOnly

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin,generics.RetrieveAPIView):
     permission_classes     = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
     queryset               = Status.objects.all()
     serializer_class       = StatusSerializer
     lookup_field           = 'id' # defualt is pk - toward making our own slug
     
     def put(self, request,*args, **kwargs):
         return self.update(request, *args, **kwargs)
     def patch(self, request,*args, **kwargs):
         return self.update(request, *args, **kwargs)
     def delete(self, request,*args, **kwargs):
         return self.destroy(request, *args, **kwargs)
    #  def perform_update(self,serializer):
    #     serializer.save(updated_by_user =self.request.user)
    #  def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None

class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
     permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
     serializer_class       = StatusSerializer
     search_fields          = ('user__username','content')
     ordering_fields        = ('user__username','timestamp')
     queryset               = Status.objects.all()
    
    #  def get_queryset(self):    #buitin search_fields does the search
    #     qs = Status.objects.all()
    #     query = self.request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter (content__icontains = query)
    #     return qs
     def post(self, request,*args, **kwargs):
         return self.create(request, *args, **kwargs)

     def perform_create(self, serializer):
        serializer.save(user=self.request.user)





# # CreateModelMixin --- POST mothod
# # UpdateModelMixin --- PUT method
# # DestroyModelMixin --- DELETE method

# class StatusAPIView( #Single Endpoint for all
#     mixins.CreateModelMixin, 
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.ListAPIView):
#      permission_classes     = []
#      authentication_classes = []
#      serializer_class       = StatusSerializer
#      passed_id              = None
    
#      def get_queryset(self):
#         request = self.request
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter (content__icontains = query)
#         return qs
#      def get_object(self):
#          request        = self.request
#          passed_id      = request.GET.get('id') or self.passed_id
#          queryset       = self.get_queryset()
#          obj = None
#          if passed_id is not None:
#              obj = get_object_or_404(queryset, id=passed_id)
#              self.check_object_permissions(request, obj)
#          return obj
     
#     #  def perform_destroy(self, instance):
#     #     if instance is not None:
#     #         return instance.delete()
#     #     return None

#      def get(self, request, *args, **kwargs):
#         url_passed_id    = request.GET.get('id', None)
#         json_data        = {}
#         body_            = request.body
#         if is_json(body_):
#             json_data        = json.loads(request.body)
#         new_passed_id    = json_data.get('id', None)
#         #print(request.body)
#         #request.data
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         if passed_id is not None:# or passed_id is not "":
#             return self.retrieve(request, *args, **kwargs) # it will call the overriden get_object method
#         return super().get(request, *args, **kwargs)

#      def post(self, request,*args, **kwargs):
#          return self.create(request, *args, **kwargs)
#      def put(self, request,*args, **kwargs):
#         url_passed_id    = request.GET.get('id', None)
#         json_data        = {}
#         body_            = request.body
#         if is_json(body_):
#             json_data        = json.loads(request.body)
#         new_passed_id    = json_data.get('id', None)
#         #print(request.body)
#         #request.data
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)
     
#      def patch(self, request,*args, **kwargs):
#         url_passed_id    = request.GET.get('id', None)
#         json_data        = {}
#         body_            = request.body
#         if is_json(body_):
#             json_data        = json.loads(request.body)
#         new_passed_id    = json_data.get('id', None)
#         #print(request.body)
#         #request.data
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)
     
#      def delete(self, request,*args, **kwargs):
#         url_passed_id    = request.GET.get('id', None)
#         json_data        = {}
#         body_            = request.body
#         if is_json(body_):
#             json_data        = json.loads(request.body)
#         new_passed_id    = json_data.get('id', None)
#         #print(request.body)
#         #request.data
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.destroy(request, *args, **kwargs)














# class StatusListSearchAPIView(APIView):
#      permission_classes     = []
#      authentication_classes = []
     
#      def get(self, request, format=None):
#          qs = Status.objects.all()
#          serializer = StatusSerializer(qs, many=True)
#          return Response(serializer.data)  

#      def post(self, request, format=None): #to show we can have it too. 
#          qs = Status.objects.all()
#          serializer = StatusSerializer(qs, many=True)
#          return Response(serializer.data)  

# # CreateModelMixin --- POST mothod
# # UpdateModelMixin --- PUT method
# # DestroyModelMixin --- DELETE method
# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#      permission_classes     = []
#      authentication_classes = []
#      serializer_class       = StatusSerializer
    
#      def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter (content__icontains = query)
#         return qs
#      def post(self, request,*args, **kwargs):
#          return self.create(request, *args, **kwargs)

# # class StatusCreateAPIView(generics.CreateAPIView):
# #      permission_classes     = []
# #      authentication_classes = []
# #      queryset               = Status.objects.all()
# #      serializer_class       = StatusSerializer

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView): #much cleaner version
#      permission_classes     = []
#      authentication_classes = []
#      queryset               = Status.objects.all()
#      serializer_class       = StatusSerializer
#      lookup_field           = 'id' # defualt is pk - toward making our own slug   

# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin,generics.RetrieveAPIView):
#      permission_classes     = []
#      authentication_classes = []
#      queryset               = Status.objects.all()
#      serializer_class       = StatusSerializer
#      lookup_field           = 'id' # defualt is pk - toward making our own slug
     
#      def put(self, request,*args, **kwargs):
#          return self.update(request, *args, **kwargs)
#      def patch(self, request,*args, **kwargs):
#          return self.update(request, *args, **kwargs)
#      def delete(self, request,*args, **kwargs):
#          return self.destroy(request, *args, **kwargs)
#     #  def get_object (self, *args, **kwargs):
#     #      kwargs = self.kwargs
#     #      kw_id = kwargs.get ('id') #if change id, we have to change P<id> in urls.py too
#     #      return Status.objects.get(id=kw_id)

# # class StatusUpdateAPIView(generics.UpdateAPIView):
# #      permission_classes     = []
# #      authentication_classes = []
# #      queryset               = Status.objects.all()
# #      serializer_class       = StatusSerializer
    
# # class StatusDeleteAPIView(generics.DestroyAPIView):
# #      permission_classes     = []
# #      authentication_classes = []
# #      queryset               = Status.objects.all()
# #      serializer_class       = StatusSerializer
