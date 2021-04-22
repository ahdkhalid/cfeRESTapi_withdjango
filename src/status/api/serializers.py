from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from status.models import Status
from accounts.api.serializers import UserPublicSerializer

'''
Serializers -> JSON
Serializers -> Validate data
'''

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
    def get_uri(self, obj):
        request = self.context.get('request') 
        return api_reverse("api-status:detail",kwargs={"id":obj.id},request=request)
class StatusInlineUserSerializer(StatusSerializer):
    # uri             = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status 
        fields =[
            'uri',
            'id',
            'content',
            'image'
        ]
# class StatusInlineUserSerializer(serializers.ModelSerializer):
#     uri             = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Status 
#         fields =[
#             'uri',
#             'id',
#             'content',
#             'image'
#         ]

#     def get_uri(self, obj):
#         request = self.context.get('request') 
#         return api_reverse("api-status:detail",kwargs={"id":obj.id},request=request)
