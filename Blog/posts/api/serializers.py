
from rest_framework import serializers

from categories.api.serializers import CategorySerializer
from posts.models import Post
from users.api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    # //Traemos los dstos del serializador de user y category, asi se muestran todos
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']






