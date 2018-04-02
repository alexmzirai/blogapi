# serializers are used to convert our data into JSON format
from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # we're exposing all the fields including ID which is the primary key django adds to all fields
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post




