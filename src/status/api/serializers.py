from rest_framework import serializers

from status.models import Status

'''
Serializers -> JSON
Serializers -> Validate data
'''
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields =[
            'user',
            'content',
            'image'
        ]

