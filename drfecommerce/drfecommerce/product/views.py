from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple View set for viewing categories
    """

    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):

        serializer_class = CategorySerializer(self.queryset, many=True)
        return Response(serializer_class.data)


# Create your views here.
