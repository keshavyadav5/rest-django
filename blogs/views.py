from django.shortcuts import render
from .models import Blog, Comment
from rest_framework import mixins, generics, viewsets
from rest_framework.response import Response
from .serializers import CommentSerializer, BlogSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class Blogsview(generics.ListCreateAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
  # filterset_fields = ['id', 'blog_title']
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  search_fields = ['blog_title']
  ordering_fields = ['blog_title']


class CommentView(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
  lookup_view = 'pk'


class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  lookup_view = 'pk'