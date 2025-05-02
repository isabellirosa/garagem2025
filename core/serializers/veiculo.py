from rest_framework.serializers import ModelSerializer

from core.models import Veiculo

class VeiculoSerializer(ModelSerializer):

    class Meta:
        model = Veiculo    
        fields = "__all__"
    
class VeiculoListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Veiculo    
        fields = "__all__"
        depth = 1

class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo    
        fields = ("id", "ano", "preco")
        depth = 1
