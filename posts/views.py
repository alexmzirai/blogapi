from django.shortcuts import render

from rest_framework import generics
from . import models
from . import serializers

# the views for thr Blog API


class PostList(generics.ListAPIView):
    # we want to list everything
    queryset = models.Post.objects.all()
    # grab the serializer class from serializers.py file
    serializer_class = serializers.PostSerializer

# this turns the api into a CRUD project :-)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

