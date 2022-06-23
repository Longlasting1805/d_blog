from rest_framework import serializers
from .models import blog_model


class blog_serializer(serializers.ModelSerializer):
    class Meta:
        model = blog_model
        fields = ['id', 'author', 'title', 'content', 'date']