import objects as objects
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from comments.api.permissions import IsOwnerOrReadAndCreateOnly
from comments.api.serializers import CommentSerializer
from comments.models import Comment


class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    # ORDENAMOS POR FECHA DE COMENTARIO MAS NUEVO
    ordering = ['-created_at']
    # FILTRAMOS POR ID DE POST
    filterset_fields = ['post']