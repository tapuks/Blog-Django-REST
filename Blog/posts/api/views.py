from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from posts.api.permissions import isAdminOrReadonly
from posts.api.serializers import PostSerializer
from posts.models import Post


class PostApiViewsSet(ModelViewSet):
    permission_classes = [isAdminOrReadonly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    filter_backends = [DjangoFilterBackend]
    # FILTRAMOS POR CATEGORIA  .......ttp://127.0.0.1:8000/api/posts?category=2
    # filterset_fields = ['category']
    # FILTRAMOS POR CATEGORIA Y POR EL SLGUG DE LA CATEGORIA .tp://127.0.0.1:8000/api/posts?category__slug=python_3
    filterset_fields = ['category', 'category__slug']


