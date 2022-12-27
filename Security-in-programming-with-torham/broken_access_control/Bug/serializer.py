from rest_framework import serializers
from Bug.models import Admins


class AdminsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ['id', 'access_level', 'username']

