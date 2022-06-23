from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator

from .models import blog_model
from .serializers import blog_serializer


# Create your views here.

class blog_view(APIView):

    def get(self, request):
        blog = blog_model.objects.all()
        page_number = self.request.query_params.get('page_number', 1)
        page_size = self.request.query_params.get('page_size', 1)
        paginator = Paginator(blog, page_size)
        serializer = blog_serializer(paginator.page(page_number), many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serializer = blog_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class blog_details(APIView):
    def get_object(self, pk):
        try:
            return blog_model.objects.get(pk=pk)
        except blog_model.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = blog_serializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response

    def put(self, request, id):
        blog = self.get_object(id)
        serializer = blog_serializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
