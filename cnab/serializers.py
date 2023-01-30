from rest_framework import serializers
from cnab.models import CnabFile


class CnabFileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    type = serializers.CharField()
    date = serializers.DateField()
    value = serializers.CharField()
    cpf = serializers.CharField()
    credit_card = serializers.CharField()
    hour = serializers.TimeField()
    owner = serializers.CharField()
    store = serializers.CharField()



    
    