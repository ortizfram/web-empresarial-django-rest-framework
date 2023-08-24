from rest_framework import serializers 
from .models import Post
from apps.category.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    # import from django to rest framework JSON
    # reference to model function
    # reference to model function
    thumbnail = serializers.SerializerMethodField()
    video=serializers.CharField(source='get_video')
    category = CategorySerializer()
    class Meta:
        model = Post
        fields =[
            # category is serialized in it's own app below,and above
            'blog_uuid',
            'title',
            'slug',
            'thumbnail',
            'video',
            'description',
            'excerpt',
            'category',
            'published',
            'status',
        ]

    def get_thumbnail(self, post):
        return post.get_thumbnail(post)