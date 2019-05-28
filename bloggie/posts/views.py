from django.shortcuts import render
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

# Create your views here.

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

