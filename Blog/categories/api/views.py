from rest_framework.viewsets import ModelViewSet

from categories.api.permissions import IsAdminOrReadonly
from categories.api.serializers import CategorySerializer
from categories.models import Category


class CategoryApiViewSet(ModelViewSet):
    permission_classes =[IsAdminOrReadonly]
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    # CATEGORIAS QUE PUBLISHED SEA TRUE
    queryset = Category.objects.filter(published=True)
    # POR EJEMPLO JAL HACER UN POST, EN VEZDE PASARLE EL ID LE PASAREMOS EL SLUG
    # lockup_field = 'slug'