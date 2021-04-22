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
    #user            = serializers.SerializerMethodField(read_only=True)
    user            = UserPublicSerializer(read_only=True)
    # user_id         = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    # user_id         = serializers.HyperlinkedRelatedField(
    #                         source='user',  # user foreign key
    #                         lookup_field='username',
    #                         view_name='api-user:detail',
    #                         read_only=True

    #                         )
    # user            = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Status
        fields =[
            'uri',
            # 'user_id',
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
