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
            'id', # ?? tmp for now,
            'user',
            'content',
            'image'
        ]
        read_only_fields=['user']
        # partial = True
