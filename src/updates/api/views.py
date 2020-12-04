import json
from django.views.generic import View
from django.http import HttpResponse

from updates.models import Update as UpdateModel
from updates.forms import UpdateModelForm

from .mixins import CSRFExemptMixin
from cfeapi.mixin import HttpResponseMixin
from .utils import is_json
class UpdateModelDetailAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    '''
    Retrieve, Update, Delete --> OBJECT  
    '''
    is_json=True
    def get_object(self,id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj =None
        ''' Below Handles a Does Not Exist Exception '''
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message':'Update not found'})
            return self.render_to_response(error_data,status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data) 
    def post(self, request, *args, **kwargs ):
        json_data=json.dumps({'message':'Not Allowed, please use the api/updates/ endpoint'})
        return self.render_to_response(json_data,status=403 )   
    def put(self, request, id, *args, **kwargs ):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message':'Invalid data sent, please send using JSON'})
            return self.render_to_response(error_data,status=400)
        
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message':'Update not found'})
            return self.render_to_response(error_data,status=404)
        # print (dir(request)) # to see diff attri and func of request
        #print (request.body)
        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        for key, value in passed_data.items():
            data[key] = value
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400) #bad request
        json_data=json.dumps({'message':'something for now'})
        return self.render_to_response(json_data) 
    def delete(self, request, id, *args, **kwargs ):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message':'Update not found'})
            return self.render_to_response(error_data,status=404)
        deleted_, item_deleted=obj.delete()
        print (deleted_)
        if deleted_ == 1:
            json_data=json.dumps({'message':'Successfully Deleted.'})
            return self.render_to_response(json_data,status=200) 
        error_data = json.dumps({'message':'Could not delete, please try again later'})
        return self.render_to_response(error_data,status=400)

class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    '''
    List view, Create view
    Let's add put and delete too
    One endpoint for complete CRUD -> api/update/
    '''
    is_json=True
    queryset = None
    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.queryset = qs
        return qs
    def get_object(self,id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj =None
        ''' Below Handles a Does Not Exist Exception '''
        if id is None:
            return None
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None    
    def get(self, request, *args, **kwargs ):
        data = json.loads(request.body)
        passed_id = data.get('id', None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({'message':'Object not found'})
                return self.render_to_response(error_data,status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data) 
        else:
            qs = self.get_queryset()
            json_data = qs.serialize()
            return self.render_to_response(json_data) 
    
    def post(self, request, *args, **kwargs ):
        # print(request.POST)
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message':'Invalid data sent, please send using JSON'})
            return self.render_to_response(error_data,status=400)
        data = json.loads(request.body)
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400) #bad request
        data = json.dumps({'message':'Not allowed'})
        return self.render_to_response(data,status=400)   

    def put(self, request, *args, **kwargs ):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message':'Invalid data sent, please send using JSON'})
            return self.render_to_response(error_data,status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({'id':'This is a required field to update an item'})
            return self.render_to_response(error_data,status=400)
        obj = self.get_object(id=passed_id) #get id from data rather than url, since we don't have it in url
        if obj is None:
            error_data = json.dumps({'message':'Object not found'})
            return self.render_to_response(error_data,status=404)
        # print (dir(request)) # to see diff attri and func of request
        #print (request.body)
        data = json.loads(obj.serialize())
        for key, value in passed_data.items():
            data[key] = value
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400) #bad request
        json_data=json.dumps({'message':'something for now'})
        return self.render_to_response(json_data) 
    def delete(self, request, *args, **kwargs ):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message':'Invalid data sent, please send using JSON'})
            return self.render_to_response(error_data,status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({'id':'This is a required field to update an item'})
            return self.render_to_response(error_data,status=400)
        
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({'message':'Update not found'})
            return self.render_to_response(error_data,status=404)
        deleted_, item_deleted=obj.delete()
        print (deleted_)
        if deleted_ == 1:
            json_data=json.dumps({'message':'Successfully Deleted.'})
            return self.render_to_response(json_data,status=200) 
        error_data = json.dumps({'message':'Could not delete, please try again later'})
        return self.render_to_response(error_data,status=400)
