from django.shortcuts import render
from .serializers import BlogSerializer, ImageSerializer
from rest_framework.viewsets import ModelViewSet
from .models import BlogModel, Images
from .serializers import BlogSerializer
from rest_framework.authentication import BasicAuthentication, BaseAuthentication, TokenAuthentication
# Create your views here.


class BlogViewSet(ModelViewSet):
    permission_classes = []
    authentication_classes = []
    model = BlogModel.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        return BlogModel.objects.all()


class ImagesViewSet(ModelViewSet):
    permission_classes = []
    authentication_classes = []
    model = Images.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Images.objects.all()
