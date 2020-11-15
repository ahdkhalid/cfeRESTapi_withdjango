from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import View #generic View, all view method inherit from this
import json #from pure python
from cfeapi.mixin import JsonResponseMixin

from .models import Update
# def detail_view(request):
#     return render(request, template,{}) #but we want to return json data instead
#     return HttpResponse(get_template().render({}))

def json_example_view(request):
    # URL - for a rest api
    data ={
        'count': 1000,
        'content': 'some example content'
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(data)

class JsonCBV(View):
    def get(self,request, *args, **kwargs):
        data = {
            'count': 10000,
            'content': 'some example content'
        }
        return JsonResponse(data)

        
class JsonCBV2(JsonResponseMixin, View):
    def get (self, request, *args, **kwargs):
        data = {
        'count': 10000,
        'content': 'some example content'
        }
        return self.render_to_json_response(data)

class SerializedDetailView(View):
    def get (self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data=obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
    def get (self, request, *args, **kwargs):
        json_data=Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')



