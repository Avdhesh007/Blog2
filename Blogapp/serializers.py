from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.Serializer):
    author=serializers.CharField(max_length=20)
    date = serializers.DateTimeField()
    heading=serializers.CharField(max_length=50)
    blog=serializers.CharField(max_length=200)

    '''class Meta:
        model=Blog
        fields=('heading','blog','date')'''