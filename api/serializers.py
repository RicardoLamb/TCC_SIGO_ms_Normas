from rest_framework import serializers
from .models import Normas

class NormasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Normas
        fields = ('id', 'sigla', 'codigo', 'vigencia', 'fonte', 'area', 'titulo', 'descricao', 'consequencias', 'acoes', 'usocorreto', 'descarte', 'riscos', 'status')