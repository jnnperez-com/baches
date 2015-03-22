from .models import Reporte
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)



class ReporteSerializer(ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    #ct_idnci= NCISerializer(many=False, read_only=True)

    class Meta:
        model = Reporte
        fields = ('image','name','owner','date','place')



class SetPassword(serializers.Serializer):
    password1 = serializers.CharField(max_length=36)
    password2 = serializers.CharField(max_length=36)

    def validate(self, attrs):
        if attrs['password1'] == attrs['password2']:
            return attrs
        else:
            raise serializers.ValidationError('los password no son iguales')