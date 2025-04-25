from rest_framework.viewsets import ModelViewSet

from core.models import Acessorio
from core.serializers import AcessorioSerializer

class AcessorioViewset(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer