from rest_framework.serializers import ModelSerializer
from .models import BlogModel, Images


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    post_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'created_at',
                  'content', 'post_images']
