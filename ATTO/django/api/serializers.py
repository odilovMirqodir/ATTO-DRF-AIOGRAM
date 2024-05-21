from rest_framework import serializers
from my_app.models import User, Tarif


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TarifSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = '__all__'
