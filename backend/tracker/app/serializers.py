from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ( 'email', 'password', 'position')