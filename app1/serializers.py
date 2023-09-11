from rest_framework import serializers
from .models import InfoModel

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoModel
        fields = ('name','surname','date_of_birth','gender','status')
        