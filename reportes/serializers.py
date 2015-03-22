from rest_framework import serializers

from .models import Reporte

class ReporteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Reporte
