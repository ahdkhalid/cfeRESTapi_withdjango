from rest_framework import serializers

from status.models import Status
from accounts.api.serializers import UserPublicSerializer

'''
Serializers -> JSON
Serializers -> Validate data
'''
class StatusInlineUserSerializer(serializers.ModelSerializer):
    uri             = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status 
        fields =[
            'uri',
            'id',
            'content',
            'image'
        ]

    def get_uri(self, obj):
        return "/api/status/{id}/".format(id=obj.id)



class StatusSerializer(serializers.ModelSerializer):
    uri               = serializers.SerializerMethodField(read_only=True)
    user              = UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields =[
            'uri',
            'id', # ?? tmp for now,
            'user',
            'content',
            'image'
        ]
        read_only_fields=['user']
        # partial = True
    def get_uri(self,obj):
        return 'api/status/{id}/'.format(id=obj.id)
