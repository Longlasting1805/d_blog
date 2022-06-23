from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator

from .models import BlogModel
from .serializers import BlogSerializer


# Create your views here.

class BlogView(APIView):

    def get(self, request):
        blog = BlogModel.objects.all()
        page_number = self.request.query_params.get('page_number', 1)
        page_size = self.request.query_params.get('page_size', 1)
        paginator = Paginator(blog, page_size)
        serializer = BlogSerializer(paginator.page(page_number), many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetails(APIView):
    def get_object(self, pk):
        try:
            return BlogModel.objects.get(pk=pk)
        except BlogModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response

    def put(self, request, id):
        blog = self.get_object(id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
