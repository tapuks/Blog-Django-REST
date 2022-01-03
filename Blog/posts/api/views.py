from rest_framework.viewsets import ModelViewSet

from posts.api.serializers import PostSerializer
from posts.models import Post


class PostApiViewsSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)