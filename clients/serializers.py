from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Client
        fields = ('user_id', 'phone_number', 'description')