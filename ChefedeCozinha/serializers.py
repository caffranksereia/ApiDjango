from rest_framework import serializers

class CardapioSerializer(serializers.Serializer):
    class Meta:
        model = Cardapio
        fields = ['produto_id','Nome_produto','detalhes']